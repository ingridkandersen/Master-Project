# This script does the initial recon-all for 1 subj at 1 tp 
# It takes input from the command line and then runs recon-all 

recon-all \
-i $3/rawdata/F${1}/tp${2}/T1.nii \
-s $3/recon_results/F${1}/F${1}_${2} \
-all 



