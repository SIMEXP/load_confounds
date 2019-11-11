import argparse
import glob
import numpy as np
import nibabel as nb
import pathlib as pal
import pandas as pd
import warnings
from sklearn.decomposition import PCA
from nilearn.input_data import NiftiLabelsMasker
from nilearn import datasets

warnings.filterwarnings("ignore", category=DeprecationWarning)

def scrub(img_data,confounds_file):

        #Load the confound file
        vols_to_scrub = np.array(pd.read_csv(confounds_file,sep='\t')['scrub'].values)
        indices_vols_to_scrub  = np.where(vols_to_scrub  == 1 )[0]

        #Delete the volumes
        tseries_scrubbed = np.delete(img_data,indices_vols_to_scrub,3)

        print(len(indices_vols_to_scrub)," volumes are being scrubbed")
        return tseries_scrubbed



def clean_nii(fmri_path,output,scrubbing,n_conf=0.9):
    # n_conf : int or float in ]0;1[, if int : number of components
    #          from the pca of the confounds to use,
    #          -1 to use all confounds, 0 to use none.
    #          Float between 0 and 1 to use the number
    #          of components that explain this proportion 
    #          of the variance

    img_4d = nb.load(fmri_path)
    confounds_file = fmri_path.replace(".nii.gz", "_confounds.tsv.gz")

    img_data = img_4d.get_data().astype(np.float32)


    #Scrub Image
    if(scrubbing == True):
        img_data = scrub(img_data,confounds_file)

    nii_img = nb.Nifti1Image(img_data, img_4d.get_affine(), img_4d.get_header())

     #Load Mask
    parcellations = datasets.fetch_atlas_basc_multiscale_2015(version='sym')
    networks_122 = parcellations['scale122']
    masker = NiftiLabelsMasker(labels_img=networks_122, standardize=True, memory='nilearn_cache')

    #Regress Confounds
    confounds = None
    if n_conf != 0:
        confounds = pd.read_csv(confounds_file ,delimiter='\t',encoding='utf-8')
        if n_conf != -1:
            pca = PCA(n_components=n_conf)
            confounds = pca.fit_transform(confounds)
    img_data_regressed = masker.fit_transform(nii_img, confounds=confounds)
    nii_img = nb.Nifti1Image(img_data_regressed, img_4d.get_affine(), img_4d.get_header())

    #Save Nifti image
    fmri_path_out = str(output)+"/"+fmri_path.split("/")[-1].split(".nii.gz")[0]+"_scrubbed.nii.gz"
    print("Saving file:",fmri_path_out.split("/")[-1], "\n")
    nb.save(nii_img, fmri_path_out)

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("preproc_dir", type=str,
                        help="resmaple folder from NIAK output directory")
    parser.add_argument("output_dir", type=str,
                        help="output directory for scrubbed data")
    parser.add_argument("--scrub", type=bool, default=False,
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
