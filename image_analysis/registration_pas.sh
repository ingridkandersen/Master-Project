# This script does the registration of the CBF map to the freesurfer result from 1subj 1tp 


# ----------------------------------- Convert from .mgz to .nii -------------------------

mri_convert $3/recon_results/F${1}/F${1}_${2}/mri/T1.mgz $3/registration/rawdata/F${1}/T1_${2}.nii


# ----------------------------------- Do registration -------------------------------

asl_reg -i $3/rawdata/F${1}/tp_${2}/4_CBF.nii -o $3/nifti/registration/F${1}/tp_${2} -s $3/registration/rawdata/F${1}/T1_${2}.nii





