import pandas as pd 
import numpy as np 

input_data = pd.read_csv('dataframe_cbf_volumes.csv')

namelist = ['Group', 'Participant', 'Timepoint', 'Left-Hippocampus', 'Right-Hippocampus', 'Left-Amygdala', 'Right-Amygdala', 'Left-Thalamus', 'Right-Thalamus', 'Left-Caudate', 'Right-Caudate', 'Left-Cerebellum-White-Matter', 'Right-Cerebellum-White-Matter', 'Left-Cerebellum-Cortex', 'Right-Cerebellum-Cortex', 'Left-Pallidum', 'Right-Pallidum', 'Left-Putamen', 'Right-Putamen', 'Left-Accumbens-area', 'Right-Accumbens-area', 'Brain-Stem', 'Left-Hippocampus-CBF', 'Right-Hippocampus-CBF', 'Left-Amygdala-CBF', 'Right-Amygdala-CBF', 'Left-Thalamus-CBF', 'Right-Thalamus-CBF', 'Left-Caudate-CBF', 'Right-Caudate-CBF', 'Left-Cerebellum-White-Matter-CBF', 'Right-Cerebellum-White-Matter-CBF', 'Left-Cerebellum-Cortex-CBF', 'Right-Cerebellum-Cortex-CBF', 'Left-Pallidum-CBF', 'Right-Pallidum-CBF', 'Left-Putamen-CBF', 'Right-Putamen-CBF', 'Left-Accumbens-area-CBF', 'Right-Accumbens-area-CBF', 'Brain-Stem-CBF']

areas = ['Left-Hippocampus', 'Right-Hippocampus', 'Left-Amygdala', 'Right-Amygdala', 'Left-Thalamus', 'Right-Thalamus', 'Left-Caudate', 'Right-Caudate', 'Left-Cerebellum-White-Matter', 'Right-Cerebellum-White-Matter', 'Left-Cerebellum-Cortex', 'Right-Cerebellum-Cortex', 'Left-Pallidum', 'Right-Pallidum', 'Left-Putamen', 'Right-Putamen', 'Left-Accumbens-area', 'Right-Accumbens-area', 'Brain-Stem', 'Left-Hippocampus-CBF', 'Right-Hippocampus-CBF', 'Left-Amygdala-CBF', 'Right-Amygdala-CBF', 'Left-Thalamus-CBF', 'Right-Thalamus-CBF', 'Left-Caudate-CBF', 'Right-Caudate-CBF', 'Left-Cerebellum-White-Matter-CBF', 'Right-Cerebellum-White-Matter-CBF', 'Left-Cerebellum-Cortex-CBF', 'Right-Cerebellum-Cortex-CBF', 'Left-Pallidum-CBF', 'Right-Pallidum-CBF', 'Left-Putamen-CBF', 'Right-Putamen-CBF', 'Left-Accumbens-area-CBF', 'Right-Accumbens-area-CBF', 'Brain-Stem-CBF']

output_data = pd.DataFrame(columns=namelist)


# Controls 
for p in range(1,10): 
	vals_gr = input_data[input_data['Group']=='Kontroll']
	vals_p = vals_gr[input_data['Participant']==p].reset_index(drop=True)
	
	
	tps = vals_p['Timepoint'].tolist()
	
	for i in range(len(vals_p)):
		row_app = ['Kontroll', p, tps[i]]
		for area in areas:
			base = vals_p.loc[:,area].mean() 
			diff_perc = ((vals_p.loc[i,area] - base) / base) * 100
			row_app.append(diff_perc)
		output_data.loc[len(output_data)] = row_app

# ECT 
for p in range(1,10): 
	vals_gr = input_data[input_data['Group']=='ECT']
	vals_p = vals_gr[input_data['Participant']==p].reset_index(drop=True)
	
	tps = vals_p['Timepoint'].tolist()
	
	for i in range(len(vals_p)):
		row_app = ['ECT', p, tps[i]]
		for area in areas:
			base = vals_p.loc[:,area].mean() 
			diff_perc = ((vals_p.loc[i,area] - base) / base) * 100
			row_app.append(diff_perc)
		output_data.loc[len(output_data)] = row_app

# TMS 
for p in range(1,11): 
	vals_gr = input_data[input_data['Group']=='TMS']
	vals_p = vals_gr[input_data['Participant']==p].reset_index(drop=True)

	tps = vals_p['Timepoint'].tolist()
	
	for i in range(len(vals_p)):
		row_app = ['TMS', p, tps[i]]
		for area in areas:
			base = vals_p.loc[:,area].mean() 
			diff_perc = ((vals_p.loc[i,area] - base) / base) * 100
			row_app.append(diff_perc)
		output_data.loc[len(output_data)] = row_app

output_data.to_csv("dataframe_change.csv", index=False)			
print(output_data)	
