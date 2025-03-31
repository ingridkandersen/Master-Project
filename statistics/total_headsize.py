# This script plots and calculates necessary values for the total intracranial size across the groups 

import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import scipy.stats as stats

input_data = pd.read_csv("dataframe_cbf_volumes.csv")


controls = input_data[input_data['Group'] == 'Kontroll'] 
ect = input_data[input_data['Group'] == 'ECT'] 
tms = input_data[input_data['Group'] == 'TMS'] 

grp_lst = []
head_vals = []


# Find mean headsize for the participant 
for i in range(1,10):
	vals_p = controls[controls['Participant'] == i].reset_index(drop=True) 
	head_size = vals_p.loc[:,'EstimatedTotalIntraCranialVol'].mean()
	head_vals.append(head_size) 
	grp_lst.append('Control')
for i in range(1,10):
	vals_p = ect[ect['Participant'] == i].reset_index(drop=True) 
	head_size = vals_p.loc[:,'EstimatedTotalIntraCranialVol'].mean()
	head_vals.append(head_size) 
	grp_lst.append('ECT')
for i in range(1,11):
	vals_p = tms[tms['Participant'] == i].reset_index(drop=True) 
	head_size = vals_p.loc[:,'EstimatedTotalIntraCranialVol'].mean()
	head_vals.append(head_size) 
	grp_lst.append('TMS')

# Make dataframe 
lib = {'Group' : grp_lst, 'Total Volume' : head_vals}
output_data = pd.DataFrame(lib)

# Plot boxplot of headsixe for the groups 

plt.figure(1)
sns.set_theme(style="whitegrid")
sns.boxplot(data=output_data, x='Group', y='Total Volume')
plt.ylabel('Volume (mm³)')
plt.xlabel('Group')
#plt.ylim(20,65)
plt.title("Estimated total intracranial volume across groups")
plt.savefig("boxplot_total_vol.png", bbox_inches='tight')
plt.show()


# Calculate mean and std values for total cranial headsize 
control_headsize = controls['EstimatedTotalIntraCranialVol'].to_numpy()
ect_headsize = ect['EstimatedTotalIntraCranialVol'].to_numpy()
tms_headsize = tms['EstimatedTotalIntraCranialVol'].to_numpy()

print(np.mean(control_headsize))
print(np.std(control_headsize)) 

print(np.mean(ect_headsize))
print(np.std(ect_headsize)) 

print(np.mean(tms_headsize))
print(np.std(tms_headsize)) 





