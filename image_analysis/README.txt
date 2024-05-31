This is the description file for the project. 
Relevant files: 
-> make_folders.sh 
-> dcm_to_nii.sh 
-> freesurfer_recon_pas.sh 
-> freesurfer_recon_long.sh 
-> registration_pas.sh 
-> CBF_calculation.sh 
-> runme.sh 


The main file is runme.sh. It runs all the files necessary to do the analysis for one participant. 
Before running runme.sh, the files dcm_to_nii.sh and make_folders.sh must be run. 
dcm_to_nii.sh converts the DICOM files to NIFTI using the dcm2niix package -> link github here: https://github.com/rordenlab/dcm2niix
make_folders.sh creates all the necessary folders needed for runme.sh. 

dcm-to_nii.sh used the package dcm2niix to convert from DICOM to NIFTI. 
It uses the flags -f to specify filename, and %f to say that filename will be labeled the same as the folder name, which in this case is the F-value 
It then stores the result in the specified folder. As the timepoints have different folder names, these need to be specified when running the script 

runme.sh does complete FreeSurfer and FSL Basil analysis for one subjects. It takes three input arguments: 
1. subject number (F-value) 
2. folder name - tha main folder where the entire analysis is stored. 
	NB: the name of the folder is also an input argument for make_folders.sh 
3. the number of timepoints. This will vary from participant to participant, and must therefore be specified before running. 


The script takes around 24 hours to complete. 


--------------------------- Example of run-through ---------------------------------------

. make_folders.sh test_1
. dcm_to_nii.sh test_1 12345 AB AC AD AE AF 
. runme.sh 12345 test_1 5



