# This script does the CBF calculations for the ROIs for 1subj 1tp 


mri_segstats \
--seg $3/recon_results/F${1}/F${1}_${2}/mri/aseg.mgz \
--i $3/registration/F${1}/tp_${2}/asl2struct.nii.gz \
--ctab $FREESURFER_HOME/FreeSurferColorLUT.txt \
--sum $3/CBF_calc/F${1}/CBF_${2}.txt

