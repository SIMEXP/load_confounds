import argparse
import glob
import numpy as np
import nibabel as nb
import pathlib as pal
import pandas as pd
import warnings

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


    
def clean_nii(fmri_path,output,scrubbing):
    
    img_4d = nb.load(fmri_path)
    confounds_file = fmri_path[0:fmri_path.index('.nii.gz')]
    confounds_file += "_confounds.tsv.gz"

    img_data = img_4d.get_data().astype(np.float32)


    #Scrub Image
    if(scrubbing == True):
        img_data = scrub(img_data,confounds_file)


     #Load Mask
    parcellations = datasets.fetch_atlas_basc_multiscale_2015(version='sym')
    networks_122 = parcellations['scale122']


    #Regress Confounds




    #Save Nifti image
    nii_img = nb.Nifti1Image(img_data, img_4d.get_affine(), img_4d.get_header())

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


    #curr = os.getcwd()    
    args = parser.parse_args()
    input_dir = pal.Path(args.preproc_dir)
    output_dir = pal.Path(args.output_dir)
    
    fmri_files = glob.glob(str(input_dir)+"/*.nii.gz")

    for file in fmri_files:
        print("\nFile being scrubbed:",file.split("/")[-1])
        clean_nii(file,output_dir,scrubbing=args.scrub)
    
