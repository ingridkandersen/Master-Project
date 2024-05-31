# This script does the longitudinal recon-all for 1 subj 
# Arguments: 1=subj 2=path/folder 3=n_tps
# Each n_tps has its own analysis due to the formulation of the -base analysis 

#--------------------------------------- Make the base ----------------------------

if [ $3 -eq 2 ]
recon-all \
-base $2/recon_results/F${1}/F${1}_base \
-tp $2/recon_results/F${1}/F${1}_1 \
-tp $2/recon_results/F${1}/F${1}_2 \
-all


elif [ $3 -eq 3 ] 
then 
recon-all \
-base $2/recon_results/F${1}/F${1}_base \
-tp $2/recon_results/F${1}/F${1}_1 \
-tp $2/recon_results/F${1}/F${1}_2 \
-tp $2/recon_results/F${1}/F${1}_3 \
-all


elif [ $3 -eq 4 ] 
then 

recon-all \
-base $2/recon_results/F${1}/F${1}_base \
-tp $2/recon_results/F${1}/F${1}_1 \
-tp $2/recon_results/F${1}/F${1}_2 \
-tp $2/recon_results/F${1}/F${1}_3 \
-tp $2/recon_results/F${1}/F${1}_4 \
-all

elif [ $3 -eq 5 ] 
then 

recon-all \
-base $2/recon_results/F${1}/F${1}_base \
-tp $2/recon_results/F${1}/F${1}_1 \
-tp $2/recon_results/F${1}/F${1}_2 \
-tp $2/recon_results/F${1}/F${1}_3 \
-tp $2/recon_results/F${1}/F${1}_4 \
-tp $2/recon_results/F${1}/F${1}_5 \
-all

fi 

# -------------------------------------- Longitudinal analysis -------------------

# Longitudinal analysis: 

for ((tp=1; tp<=$3; tp++)) 
do
recon-all \
-long $2/recon_results/F${1}/F${1}_${tp} \
$2/recon_results/F${1}/F${1}_base \
-all 
done 


