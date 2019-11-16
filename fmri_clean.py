import argparse
import glob
import numpy as np
import nibabel as nb
import pathlib as pal
import pandas as pd
import warnings
from sklearn.decomposition import PCA
from nilearn.image import clean_img
from nilearn.input_data import NiftiMasker
from nilearn import datasets

warnings.filterwarnings("ignore", category=DeprecationWarning)


def remove_frames(img_data,confounds_file):

        #Load the confound file
        vols_to_scrub = np.array(pd.read_csv(confounds_file,sep='\t')['scrub'].values)
        indices_vols_to_scrub  = np.where(vols_to_scrub  == 1 )[0]

        #Delete the volumes
        tseries_scrubbed = np.delete(img_data,indices_vols_to_scrub,3)

        print(len(indices_vols_to_scrub)," volumes are being scrubbed")

        return tseries_scrubbed



def scrub_encode(scrub_paramters):

    frames = 0
    scrub_vol = []

    for vol in scrub_paramters.values:
        if vol == 1:
            scrub_vol_str = "scrub_vol"+str(frames)
            scrub_vol.append(scrub_vol_str)
        else:
            scrub_vol.append(0)
        frames+=1

    scrub_confounds = pd.get_dummies(scrub_vol,drop_first= False)

    scrub_confounds.drop(columns = 0 ,inplace=True)

    return scrub_confounds


def pca_motion(motion_parameters):

    pca = PCA(n_components=0.95)
    confounds = pca.fit_transform(motion_parameters.values)

    motion_confounds = pd.DataFrame(confounds)

    motion_confounds.columns = ["motion_pca_"+str(col+1) for col in motion_confounds.columns]

    return motion_confounds


def load_confounds(confounds,scrubbing):

    if not isinstance(confounds, pd.DataFrame):
        confounds = pd.read_csv(confounds ,delimiter='\t',encoding='utf-8')

    avgs_confound = confounds[['wm_avg', 'vent_avg']]

    #Run PCA on motion parameters
    motion_parameters = confounds[['motion_tx', 'motion_ty', 'motion_tz', 'motion_rx', 'motion_ry','motion_rz']]
    motion_confounds = pca_motion(motion_parameters)


    #Get column vectors from scrub labels
    if(scrubbing == True):
        scrub_paramters = confounds[['scrub']]
        scrub_confounds = scrub_encode(scrub_paramters)
        confounds_light = pd.concat([motion_confounds,avgs_confound,scrub_confounds], axis=1)

    else:
        confounds_light = pd.concat([motion_confounds,avgs_confound], axis=1)


    return confounds_light



def clean_nii(fmri_path,output,scrubbing):

    #Generate confounds
    confounds_file = fmri_path.replace(".nii.gz", "_confounds.tsv.gz")
    confounds_light = load_confounds(confounds_file,scrubbing)

    #Load Mask
    # parcellations = datasets.fetch_atlas_basc_multiscale_2015(version='sym')
    # networks_122 = parcellations['scale122']
    # masker = NiftiMasker()

    #clean nifti
    img_data_clean = clean_img(fmri_path,confounds=confounds_light.values)

    #Save file
    #img_4d = nb.load(fmri_path)
    #print(img_data_clean.get_data())
    #nii_img = nb.Nifti1Image(img_data_clean, img_data_clean.get_affine(), img_data_clean.get_header())

    #Save Nifti image
    fmri_path_out = str(output)+"/"+fmri_path.split("/")[-1].split(".nii.gz")[0]+"_clean.nii.gz"
    print("Saving file:",fmri_path_out.split("/")[-1], "\n")
    nb.save(img_data_clean, fmri_path_out)

    confounds_light.to_csv(str(output)+"/confounds_light.csv",index=False)

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("preproc_dir", type=str,
                        help="resmaple folder from NIAK output directory")
    parser.add_argument("output_dir", type=str,
                        help="output directory for scrubbed data")
    parser.add_argument("--scrub", type=bool, default=True,
                        help="If set to True, volumes will be scrubbed. Default is False.")
    parser.add_argument("--n_conf", type=float, default=0.9,
                        help="Number of components to use from confounds if int, if -1 all\
                              confounds are used, if float between 0 and 1: number of components\
                              explaining this proportion of the variance in the confounds.")


    #curr = os.getcwd()    
    args = parser.parse_args()
    input_dir = pal.Path(args.preproc_dir)
    output_dir = pal.Path(args.output_dir)

    fmri_files = glob.glob(str(input_dir)+"/*.nii.gz")

    for file in fmri_files:
        print("\nFile being processed:",file.split("/")[-1])
        clean_nii(file,output_dir,scrubbing=args.scrub)
