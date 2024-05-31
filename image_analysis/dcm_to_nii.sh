# This script converts from dicom to nifti for 1subj 
# Format: 
# dcm2niix -f(filename_will_be_labelled_%x) %f(foldername) -o path/to/nifti/folder path/to/dicom/folder
# Arguments: 
# 1=foldername 2=F_number 3=folder_tp1 4=folder_tp2 ... 

# ------------------------------- Make folders for rawdata Nifti ------------------------------

#mkdir ${1}/rawdata/s${2}

j=4 
while [ ${j} -le ${#} ]
do
	mkdir ${1}/rawdata/F${2}/tp$(( j - 2 ))
	j=$(( $j + 1 ))
done 

# ------------------------------- Convert data from DICOM to NIFTI ----------------------------
declare -a names=("1_T1" "2_T2" "3_3D_ASL" "4_CBF")
declare -a args=("$@")

echo ${args[@]}
echo ${#}
i=4 
while [ ${i} -le ${#} ]
do
	for type in "${names[@]}"; 
	do
		dcm2niix -f %f -o ${1}/rawdata/F${2}/tp$(( i - 2 )) dicoms/F${2}/${args[ ${i} -1 ]}/$type 	
	done
	i=$(( $i + 1 ))
done 



 

 



