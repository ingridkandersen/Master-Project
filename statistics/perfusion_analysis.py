# This script does the perfusion analysis for the Hippocampus, Amygdala and Thalamus (HAT)


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import scipy.stats as stats

input_data = pd.read_csv("dataframe_cbf_volumes.csv")

areas_left = ['Left-Hippocampus-CBF', 'Left-Amygdala-CBF', 'Left-Thalamus-CBF']
areas_right = ['Right-Hippocampus-CBF','Right-Amygdala-CBF', 'Right-Thalamus-CBF']

# 1. Find the total perfusion for Hippocampus (H), Amygdala (A) and Thalamus (T) on both sides for all tps


# ------------------------------------------ Controls -----------------------------


# Read out info 
vals_gr = input_data[input_data['Group']=='Kontroll'] 

result_array_left = [] 
result_array_right = [] 
result_array_laterality = [] 

group_array = [] 
pas_array = []
tp_array = [] 


for i in range(9): 
	pas_nr = i + 1
	vals_pas = vals_gr[vals_gr['Participant'] == pas_nr].reset_index(drop=True)  
	tps = vals_pas['Timepoint'].tolist()

	for i in range(len(vals_pas)):
		cbf_L = 0
		cbf_R = 0
		for a in areas_left: 
			cbf_L += vals_pas.loc[i,a]
		for a in areas_right: 
			cbf_R += vals_pas.loc[i,a]

		group_array.append('Control') 
		pas_array.append(pas_nr) 
		tp_str = tps[i]
		tp_array.append(tp_str) 
		
		result_array_left.append(cbf_L/3)
		result_array_right.append(cbf_R/3)
		result_array_laterality.append((cbf_L/3 - cbf_R/3)/(cbf_L/3 + cbf_R/3))


# ------------------------------------------ ECT ---------------------------------

# Read out info 
vals_gr = input_data[input_data['Group']=='ECT'] 

for i in range(9): 
	pas_nr = i + 1
	vals_pas = vals_gr[vals_gr['Participant'] == pas_nr].reset_index(drop=True)  
	tps = vals_pas['Timepoint'].tolist()

	for i in range(len(vals_pas)):
		cbf_L = 0
		cbf_R = 0
		for a in areas_left: 
			cbf_L += vals_pas.loc[i,a]
		for a in areas_right: 
			cbf_R += vals_pas.loc[i,a]

		group_array.append('ECT') 
		pas_array.append(pas_nr) 
		tp_str = tps[i] 
		tp_array.append(tp_str) 
		
		result_array_left.append(cbf_L/3)
		result_array_right.append(cbf_R/3)
		result_array_laterality.append((cbf_L - cbf_R)/(cbf_L + cbf_R))



# ------------------------------------------ TMS ---------------------------------

# Read out info 
vals_gr = input_data[input_data['Group']=='TMS'] 

for i in range(10): 
	pas_nr = i + 1
	vals_pas = vals_gr[vals_gr['Participant'] == pas_nr].reset_index(drop=True)  
	tps = vals_pas['Timepoint'].tolist()

	for i in range(len(vals_pas)):
		cbf_L = 0
		cbf_R = 0
		for a in areas_left: 
			cbf_L += vals_pas.loc[i,a]
		for a in areas_right: 
			cbf_R += vals_pas.loc[i,a]

		group_array.append('TMS') 
		pas_array.append(pas_nr) 
		tp_str = tps[i] 
		tp_array.append(tp_str) 
		
		result_array_left.append(cbf_L/3)
		result_array_right.append(cbf_R/3)
		result_array_laterality.append((cbf_L - cbf_R)/(cbf_L + cbf_R))


# 2. Make the data into pandas dataframes for easy manipulation 

o_dat = {'Group' : group_array, 'Participant' : pas_array, 'Timepoint' : tp_array, 'Left' : result_array_left, 'Right' : result_array_right, 'Laterality Index' : result_array_laterality}
output_data = pd.DataFrame(o_dat)

output_data.to_csv("perfusion_analysis.csv", index=False)


# 3. Find mean CBF for L and R for the tps, and find laterality index


# --------------------------------------- Controls --------------------------------
mean_dataframe_ctrl = pd.DataFrame(columns=['Tp1','Tp2','Tp4','Tp5'])
mean_gr = output_data[output_data['Group']=='Control']


ctrl_left = []
ctrl_right = []
ctrl_LI = []

for i in range(5): 
	tp_nr = i+1 
	if tp_nr != 3: 
		mean_tp = mean_gr[mean_gr['Timepoint'] == tp_nr]
		mean_left = np.mean(mean_tp['Left'].to_numpy())
		mean_right = np.mean(mean_tp['Right'].to_numpy())

		ctrl_left.append(mean_left) 
		ctrl_right.append(mean_right) 
		ctrl_LI.append((mean_left - mean_right)/(mean_left + mean_right))
		


mean_dataframe_ctrl.loc[len(mean_dataframe_ctrl)] = ctrl_left
mean_dataframe_ctrl.loc[len(mean_dataframe_ctrl)] = ctrl_right
mean_dataframe_ctrl.loc[len(mean_dataframe_ctrl)] = ctrl_LI

print(mean_dataframe_ctrl)



# --------------------------------------- ECT ------------------------------------
mean_dataframe_ect = pd.DataFrame(columns=['Tp1','Tp2','Tp3','Tp4','Tp5',])

mean_gr = output_data[output_data['Group']=='ECT']

ect_left = []
ect_right = []
ect_LI = []

for i in range(5): 
	tp_nr = i+1 
	mean_tp = mean_gr[mean_gr['Timepoint'] == tp_nr]
	mean_left = np.mean(mean_tp['Left'].to_numpy())
	mean_right = np.mean(mean_tp['Right'].to_numpy())

	ect_left.append(mean_left) 
	ect_right.append(mean_right) 
	ect_LI.append((mean_left - mean_right)/(mean_left + mean_right))


mean_dataframe_ect.loc[len(mean_dataframe_ect)] = ect_left
mean_dataframe_ect.loc[len(mean_dataframe_ect)] = ect_right
mean_dataframe_ect.loc[len(mean_dataframe_ect)] = ect_LI

print(mean_dataframe_ect)


# -------------------------------------- TMS ---------------------------------- 
mean_dataframe_tms = pd.DataFrame(columns=['Tp1','Tp2','Tp3','Tp4','Tp5',])

mean_gr = output_data[output_data['Group']=='TMS']

tms_left = []
tms_right = []
tms_LI = []

for i in range(5): 
	tp_nr = i+1 
	mean_tp = mean_gr[mean_gr['Timepoint'] == tp_nr]
	mean_left = np.mean(mean_tp['Left'].to_numpy())
	mean_right = np.mean(mean_tp['Right'].to_numpy())

	tms_left.append(mean_left) 
	tms_right.append(mean_right) 
	tms_LI.append((mean_left - mean_right)/(mean_left + mean_right))


mean_dataframe_tms.loc[len(mean_dataframe_tms)] = tms_left
mean_dataframe_tms.loc[len(mean_dataframe_tms)] = tms_right
mean_dataframe_tms.loc[len(mean_dataframe_tms)] = tms_LI

print(mean_dataframe_tms)



