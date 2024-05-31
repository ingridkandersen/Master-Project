# This script runs all the FreeSurfer and FSL BASIL analyses. 
# It needs arguments: 
# 1=subj (F-value) 2=name of main folder 3=n_tps 

# ------------------------------------------ Start softwares -------------------------------------
export FREESURFER_HOME=$HOME/freesurfer
export SUBJECTS_DIR=$HOME/master_project/$2/recon_results
source $FREESURFER_HOME/SetUpFreeSurfer.sh
#cd $HOME/master_project/

FSLDIR=~/fsl/
PATH=${FSLDIR}/share/fsl/bin:${PATH}
export FSLDIR PATH
. ${FSLDIR}/etc/fslconf/fsl.sh
echo "FSL successfully started" 
# ---------------------------------------- Make folders for the subject -------------------------
# Recon-all 
mkdir ${2}/recon_results/F${1}

# Registration 
mkdir $2/registration/F${1}

for ((tp=1; tp<=${3}; tp++)) 
do
mkdir $2/registration/F${1}/tp${tp} 
done 

mkdir $2/registration/rawdata/F${1}


# CBF calculations 
for ((tp=1; tp<=${3}; tp++)) 
do
mkdir $2/CBF_calc/F${1}  
done 
# ---------------------------------------- FreeSurfer recon-all ---------------------------------
# Initial recon-all
for ((tp=1; tp<=${3}; tp++)) 
do
. freesurfer_recon_pas.sh $1 ${tp} $2
done 


# Longitudinal recon-all 
. freesurfer_recon_long_4tp.sh $1 $2 $3

# -------------------------------------- Registration of CBF map to T1 --------------------------
# Registration 
for ((tp=1; tp<=${3}; tp++)) 
do
. registration_pas.sh $1 ${tp} $2
done 

# --------------------------------------- Calculate CBF values in all regions -------------------
# Calculate CBF
for ((tp=1; tp<=${3}; tp++)) 
do
. CBF_calculation.sh $1 ${tp} $2
done 
