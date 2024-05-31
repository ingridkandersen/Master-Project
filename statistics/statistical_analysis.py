# This script does the statistical analysis of the data 

import pandas as pd 
import numpy as np 
import scipy.stats as stats

input_data = pd.read_csv('dataframe_cbf_volumes.csv')


areas_vol = ['Left-Hippocampus', 'Right-Hippocampus', 'Left-Amygdala', 'Right-Amygdala', 'Left-Thalamus', 'Right-Thalamus', 'Left-Caudate', 'Right-Caudate', 'Left-Cerebellum-White-Matter', 'Right-Cerebellum-White-Matter', 'Left-Cerebellum-Cortex', 'Right-Cerebellum-Cortex', 'Left-Pallidum', 'Right-Pallidum', 'Left-Putamen', 'Right-Putamen', 'Left-Accumbens-area', 'Right-Accumbens-area', 'Brain-Stem'] 

areas_cbf = ['Left-Hippocampus-CBF', 'Right-Hippocampus-CBF', 'Left-Amygdala-CBF', 'Right-Amygdala-CBF', 'Left-Thalamus-CBF', 'Right-Thalamus-CBF', 'Left-Caudate-CBF', 'Right-Caudate-CBF', 'Left-Cerebellum-White-Matter-CBF', 'Right-Cerebellum-White-Matter-CBF', 'Left-Cerebellum-Cortex-CBF', 'Right-Cerebellum-Cortex-CBF', 'Left-Pallidum-CBF', 'Right-Pallidum-CBF', 'Left-Putamen-CBF', 'Right-Putamen-CBF', 'Left-Accumbens-area-CBF', 'Right-Accumbens-area-CBF', 'Brain-Stem-CBF']


# ----------------------------------------------------- Controls -------------------------------------------------
vals_gr = input_data[input_data['Group']=='Kontroll']
vals_tp1 = vals_gr[input_data['Timepoint']==1].reset_index(drop=True)
vals_tp2 = vals_gr[input_data['Timepoint']==2].reset_index(drop=True)
vals_tp4 = vals_gr[input_data['Timepoint']==4].reset_index(drop=True)


# Do paired t-test and make pretty columns for pretty table <3 

# Volumes <3
control_vol_pval = []
control_vol_tval = []
control_vol_1_means = []
control_vol_1_stds = []
control_vol_4_means = []

control_vol_rel_pval = []
control_vol_rel_tval = []
control_vol_rel_1_means = []
control_vol_rel_1_stds = []
control_vol_rel_4_means = []
control_vol_rel_4_stds = []

for i, a in enumerate(areas_vol):
	
	tp1 = np.delete(vals_tp1[a].to_numpy(), [0,8])
	tp4 = vals_tp4[a].to_numpy()
	total_vols_tp1 = np.delete(vals_tp1['EstimatedTotalIntraCranialVol'].to_numpy(), [0,8]) 
	total_vols_tp4 = vals_tp4['EstimatedTotalIntraCranialVol'].to_numpy()
	
	
	# Calculate relative volume 
	tp1_rel = tp1/total_vols_tp1
	tp4_rel = tp4/total_vols_tp4
	
	# t-test 
	t_stat, p_value = (stats.ttest_rel(tp4, tp1))
	control_vol_pval.append(p_value) 
	control_vol_tval.append(t_stat)
	
	# t-test relative 
	t_stat_rel, p_value_rel = (stats.ttest_rel(tp4_rel, tp1_rel))
	control_vol_rel_pval.append(p_value_rel) 
	control_vol_rel_tval.append(t_stat_rel)
	
	#Calculate % volume change from tp1 to tp4
	control_percent_change = ((np.mean(tp4) - np.mean(tp1))/np.mean(tp1))*100 


	# mean and std 
	control_vol_1_means.append(np.mean(tp1))
	control_vol_1_stds.append(np.std(tp1))
	control_vol_4_means.append(control_percent_change)
	
	# relative mean and std 
	control_vol_rel_1_means.append(np.mean(tp1_rel))
	control_vol_rel_1_stds.append(np.std(tp1_rel))
	control_vol_rel_4_means.append(np.mean(tp4_rel))
	control_vol_rel_4_stds.append(np.std(tp4_rel))
	


# ----------------------------------------------------- ECT -------------------------------------------------
vals_gr = input_data[input_data['Group']=='ECT']
vals_tp1 = vals_gr[input_data['Timepoint']==1].reset_index(drop=True)
vals_tp2 = vals_gr[input_data['Timepoint']==2].reset_index(drop=True)
vals_tp4 = vals_gr[input_data['Timepoint']==4].reset_index(drop=True)

# Do paired t-test and make pretty columns for pretty table <3 

# Volumes <3 
ect_vol_pval = []
ect_vol_tval = []
ect_vol_1_means = []
ect_vol_1_stds = []
ect_vol_4_means = []

ect_vol_rel_pval = []
ect_vol_rel_tval = []
ect_vol_rel_1_means = []
ect_vol_rel_1_stds = []
ect_vol_rel_4_means = []
ect_vol_rel_4_stds = []

for a in areas_vol:
	
	tp1 = np.delete(vals_tp1[a].to_numpy(), [0,4,8])
	tp4 = vals_tp4[a].to_numpy()
	total_vols_tp1 = np.delete(vals_tp1['EstimatedTotalIntraCranialVol'].to_numpy(), [0,4,8]) 
	total_vols_tp4 = vals_tp4['EstimatedTotalIntraCranialVol'].to_numpy()
	
	# Calculate relative volume 
	tp1_rel = tp1/total_vols_tp1#_new
	tp4_rel = tp4/total_vols_tp4#_new
	
	# t-test 
	t_stat, p_value = (stats.ttest_rel(tp4, tp1))
	ect_vol_pval.append(p_value) 
	ect_vol_tval.append(t_stat)
	
	# t-test relative 
	t_stat_rel, p_value_rel = (stats.ttest_rel(tp4_rel, tp1_rel))
	ect_vol_rel_pval.append(p_value_rel) 
	ect_vol_rel_tval.append(t_stat_rel)
	
	#Calculate % volume change from tp1 to tp4
	ect_percent_change = ((np.mean(tp4) - np.mean(tp1))/np.mean(tp1))*100 
	
	# mean and std 
	ect_vol_1_means.append(np.mean(tp1))
	ect_vol_1_stds.append(np.std(tp1))
	ect_vol_4_means.append(ect_percent_change)

	# relative mean and std 
	ect_vol_rel_1_means.append(np.mean(tp1_rel))
	ect_vol_rel_1_stds.append(np.std(tp1_rel))
	ect_vol_rel_4_means.append(np.mean(tp4_rel))
	ect_vol_rel_4_stds.append(np.std(tp4_rel))
	
	

# ----------------------------------------------------- TMS -------------------------------------------------
vals_gr = input_data[input_data['Group']=='TMS']
vals_tp1 = vals_gr[input_data['Timepoint']==1].reset_index(drop=True)
vals_tp2 = vals_gr[input_data['Timepoint']==2].reset_index(drop=True)
vals_tp4 = vals_gr[input_data['Timepoint']==4].reset_index(drop=True)


# 1. Do paired t-test and make pretty columns for pretty table <3 

# Volumes <3 
tms_vol_pval = []
tms_vol_tval = []
tms_vol_1_means = []
tms_vol_1_stds = []
tms_vol_4_means = []
tms_vol_4_stds = []

tms_vol_rel_pval = []
tms_vol_rel_tval = []
tms_vol_rel_1_means = []
tms_vol_rel_1_stds = []
tms_vol_rel_4_means = []
tms_vol_rel_4_stds = []

for a in areas_vol:
	
	tp1 = np.delete(vals_tp1[a].to_numpy(), [8,9])
	tp4 = vals_tp4[a].to_numpy()
	total_vols_tp1 = np.delete(vals_tp1['EstimatedTotalIntraCranialVol'].to_numpy(), [8,9]) 
	total_vols_tp4 = vals_tp4['EstimatedTotalIntraCranialVol'].to_numpy()
	
	# Calculate relative volume 
	tp1_rel = tp1/total_vols_tp1#_new
	tp4_rel = tp4/total_vols_tp1#_new
	
	# t-test 
	t_stat, p_value = (stats.ttest_rel(tp4, tp1))
	tms_vol_pval.append(p_value) 
	tms_vol_tval.append(t_stat)
	
	# t-test relative 
	t_stat_rel, p_value_rel = (stats.ttest_rel(tp4_rel, tp1_rel))
	tms_vol_rel_pval.append(p_value_rel) 
	tms_vol_rel_tval.append(t_stat_rel)

	#Calculate % volume change from tp1 to tp4
	tms_percent_change = ((np.mean(tp4) - np.mean(tp1))/np.mean(tp1))*100 

	# mean and std 
	tms_vol_1_means.append(np.mean(tp1))
	tms_vol_1_stds.append(np.std(tp1))
	tms_vol_4_means.append(tms_percent_change)


	# relative mean and std 
	tms_vol_rel_1_means.append(np.mean(tp1_rel))
	tms_vol_rel_1_stds.append(np.std(tp1_rel))
	tms_vol_rel_4_means.append(np.mean(tp4_rel))
	tms_vol_rel_4_stds.append(np.std(tp4_rel))





# Make dataframe - volumes 
data_vol = {'Areas' : areas_vol, 'Controls tp1 mean' : control_vol_1_means, 'Controls tp1 stds' : control_vol_1_stds,'Controls percent change' : control_vol_4_means, 'Controls t-value' : control_vol_tval, 'Controls p-value' : control_vol_pval, 'Controls relative tp1 mean' : control_vol_rel_1_means, 'Controls relative tp1 stds' : control_vol_rel_1_stds,'Controls relative tp4 mean' : control_vol_rel_4_means, 'Controls relative tp4 stds' : control_vol_rel_4_stds, 'Controls relative t-value' : control_vol_rel_tval, 'Controls relative p-value' : control_vol_rel_pval, 'ECT tp1 mean' : ect_vol_1_means, 'ECT tp1 stds' : ect_vol_1_stds,  'ECT percent change' : ect_vol_4_means, 'ECT t-value' : ect_vol_tval, 'ECT p-value' : ect_vol_pval, 'ECT relative tp1 mean' : ect_vol_rel_1_means, 'ECT relative tp1 stds' : ect_vol_rel_1_stds,'ECT relative tp4 mean' : ect_vol_rel_4_means, 'ECT relative tp4 stds' : ect_vol_rel_4_stds, 'ECT relative t-value' : ect_vol_rel_tval, 'ECT relative p-value' : ect_vol_rel_pval, 'TMS tp1 mean' : tms_vol_1_means, 'TMS tp1 stds' : tms_vol_1_stds, 'TMS percent change' : tms_vol_4_means, 'TMS t-value' : tms_vol_tval, 'TMS p-value' : tms_vol_pval, 'TMS relative tp1 mean' : tms_vol_rel_1_means, 'TMS relative tp1 stds' : tms_vol_rel_1_stds,'TMS relative tp4 mean' : tms_vol_rel_4_means, 'TMS relative tp4 stds' : tms_vol_rel_4_stds, 'TMS relative t-value' : tms_vol_rel_tval, 'TMS relative p-value' : tms_vol_rel_pval}
vol_df = pd.DataFrame(data_vol)
print(vol_df)

vol_df.to_csv("statistical_analysis_volumes.csv", index=False)




