import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import scipy.stats as stats


# 1. Read input data 
input_data = pd.read_csv("perfusion_analysis.csv")


# 2. Calculate t_stat and p_val across tps and groups  
# Read all groups 
ctrl = input_data[input_data['Group'] == 'Control'].reset_index(drop=True)
ect = input_data[input_data['Group'] == 'ECT'].reset_index(drop=True)
tms = input_data[input_data['Group'] == 'TMS'].reset_index(drop=True)

# Control 
ctrl_tp1 = ctrl[ctrl['Timepoint'] == 1].reset_index(drop=True)
ctrl_tp1_left = ctrl_tp1['Left'].to_numpy()
ctrl_tp1_right = ctrl_tp1['Right'].to_numpy()
ctrl_tp1_left_short = np.delete(ctrl_tp1['Left'].to_numpy(), [0,8])
ctrl_tp1_right_short = np.delete(ctrl_tp1['Right'].to_numpy(), [0,8])


ctrl_tp4 = ctrl[ctrl['Timepoint'] == 4].reset_index(drop=True)
ctrl_tp4_left = ctrl_tp4['Left'].to_numpy()
ctrl_tp4_right = ctrl_tp4['Right'].to_numpy()

# ECT 
ect_tp1 = ect[ect['Timepoint'] == 1].reset_index(drop=True)
ect_tp1_left = ect_tp1['Left'].to_numpy()
ect_tp1_right = ect_tp1['Right'].to_numpy()
ect_tp1_left_short = np.delete(ect_tp1['Left'].to_numpy(), [0,4,8])
ect_tp1_right_short = np.delete(ect_tp1['Right'].to_numpy(), [0,4,8])

ect_tp4 = ect[ect['Timepoint'] == 4].reset_index(drop=True)
ect_tp4_left = ect_tp4['Left'].to_numpy()
ect_tp4_right = ect_tp4['Right'].to_numpy()

# TMS 
tms_tp1 = tms[tms['Timepoint'] == 1].reset_index(drop=True)
tms_tp1_left = tms_tp1['Left'].to_numpy()
tms_tp1_right = tms_tp1['Right'].to_numpy()
tms_tp1_left_short = np.delete(tms_tp1['Left'].to_numpy(), [8,9])
tms_tp1_right_short = np.delete(tms_tp1['Right'].to_numpy(), [8,9]) 

tms_tp4 = tms[tms['Timepoint'] == 4].reset_index(drop=True)
tms_tp4_left = tms_tp4['Left'].to_numpy()
tms_tp4_right = tms_tp4['Right'].to_numpy()


# stats on ECT/TMS vs. Control 
t_stat_ect_tp1_left, p_val_ect_tp1_left = stats.ttest_ind(ect_tp1_left, ctrl_tp1_left, equal_var=False)
t_stat_ect_tp1_right, p_val_ect_tp1_right = stats.ttest_ind(ect_tp1_right, ctrl_tp1_right, equal_var=False)
t_stat_tms_tp1_left, p_val_tms_tp1_left = stats.ttest_ind(tms_tp1_left, ctrl_tp1_left, equal_var=False) 
t_stat_tms_tp1_right, p_val_tms_tp1_right = stats.ttest_ind(tms_tp1_right, ctrl_tp1_right, equal_var=False) 

# stats across time for each group 
t_stat_ctrl_tp4_left, p_val_ctrl_tp4_left = stats.ttest_rel(ctrl_tp4_left, ctrl_tp1_left_short)
t_stat_ctrl_tp4_right, p_val_ctrl_tp4_right = stats.ttest_rel(ctrl_tp4_right, ctrl_tp1_right_short)
t_stat_ect_tp4_left, p_val_ect_tp4_left = stats.ttest_rel(ect_tp4_left, ect_tp1_left_short)
t_stat_ect_tp4_right, p_val_ect_tp4_right = stats.ttest_rel(ect_tp4_right, ect_tp1_right_short)
t_stat_tms_tp4_left, p_val_tms_tp4_left = stats.ttest_rel(tms_tp4_left, tms_tp1_left_short)
t_stat_tms_tp4_right, p_val_tms_tp4_right = stats.ttest_rel(tms_tp4_right, tms_tp1_right_short)



# Print the results
#ECT/TMS vs. controls
print(t_stat_ect_tp1_left)
print(p_val_ect_tp1_left)
print(t_stat_ect_tp1_right)
print(p_val_ect_tp1_right)
print(t_stat_tms_tp1_left)
print(p_val_tms_tp1_left)
print(t_stat_tms_tp1_right)
print(p_val_tms_tp1_right)

# scan 4 vs. scan 1 
print(t_stat_ctrl_tp4_left)
print(p_val_ctrl_tp4_left)
print(t_stat_ctrl_tp4_right)
print(p_val_ctrl_tp4_right)
print(t_stat_ect_tp4_left)
print(p_val_ect_tp4_left)
print(t_stat_ect_tp4_right)
print(p_val_ect_tp4_right)
print(t_stat_tms_tp4_left)
print(p_val_tms_tp4_left)
print(t_stat_tms_tp4_right)
print(p_val_tms_tp4_right)





# 3. Calculate change in percent 

input_relative = pd.DataFrame(columns=['Group', 'Participant', 'Timepoint', 'Left', 'Right'])

# Controls 
for p in range(1,10): 
	vals_gr = input_data[input_data['Group']=='Control']
	vals_p = vals_gr[vals_gr['Participant']==p].reset_index(drop=True)
	tps = vals_p['Timepoint'].tolist()
	for i in range(len(vals_p)):
		row_app = ['Control', p, tps[i]]
		base_left = vals_p.loc[:,'Left'].mean() 
		diff_perc_left = ((vals_p.loc[i,'Left'] - base_left) / base_left) * 100
		row_app.append(diff_perc_left)
		base_right = vals_p.loc[:,'Right'].mean() 
		diff_perc_right  = ((vals_p.loc[i,'Right'] - base_right ) / base_right ) * 100
		row_app.append(diff_perc_right)
		input_relative.loc[len(input_relative)] = row_app

# ECT 
for p in range(1,10): 
	vals_gr = input_data[input_data['Group']=='ECT']
	vals_p = vals_gr[vals_gr['Participant']==p].reset_index(drop=True)
	tps = vals_p['Timepoint'].tolist()
	for i in range(len(vals_p)):
		row_app = ['ECT', p, tps[i]]
		base_left = vals_p.loc[:,'Left'].mean() 
		diff_perc_left = ((vals_p.loc[i,'Left'] - base_left) / base_left) * 100
		row_app.append(diff_perc_left)
		base_right = vals_p.loc[:,'Right'].mean() 
		diff_perc_right  = ((vals_p.loc[i,'Right'] - base_right ) / base_right ) * 100
		row_app.append(diff_perc_right)
		input_relative.loc[len(input_relative)] = row_app

# TMS 
for p in range(1,11): 
	vals_gr = input_data[input_data['Group']=='TMS']
	vals_p = vals_gr[vals_gr['Participant']==p].reset_index(drop=True)
	tps = vals_p['Timepoint'].tolist()
	for i in range(len(vals_p)):
		row_app = ['TMS', p, tps[i]]
		base_left = vals_p.loc[:,'Left'].mean() 
		diff_perc_left = ((vals_p.loc[i,'Left'] - base_left) / base_left) * 100
		row_app.append(diff_perc_left)
		base_right = vals_p.loc[:,'Right'].mean() 
		diff_perc_right  = ((vals_p.loc[i,'Right'] - base_right ) / base_right ) * 100
		row_app.append(diff_perc_right)
		input_relative.loc[len(input_relative)] = row_app

input_relative.to_csv("perfusion_HAT_change.csv", index=False)


# 4. Plot stuff 


# ---------- Boxplots for tp1 across groups ------------


tp1_dat = input_data[input_data['Timepoint'] == 1].reset_index(drop=True)
tp4_dat = input_data[input_data['Timepoint'] == 4].reset_index(drop=True)


sns.set_theme(style="whitegrid")
sns.boxplot(data=tp1_dat, x='Group', y='Left')
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Group')
plt.ylim(20,65)
plt.title("Perfusion left HAT at Scan 1")
plt.savefig("boxplot_hat_left_tp1", bbox_inches='tight')


sns.set_theme(style="whitegrid")
sns.boxplot(data=tp1_dat, x='Group', y='Right')
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Group')
plt.ylim(20,65)
plt.title("Perfusion right HAT at Scan 1")
plt.savefig("boxplot_hat_right_tp1", bbox_inches='tight')


sns.set_theme(style="whitegrid")
sns.boxplot(data=tp4_dat, x='Group', y='Left')
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Group')
plt.ylim(20,65)
plt.title("Perfusion left HAT at Scan 4")
plt.savefig("boxplot_hat_left_tp4", bbox_inches='tight')


sns.set_theme(style="whitegrid")
sns.boxplot(data=tp4_dat, x='Group', y='Right')
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Group')
plt.ylim(20,65)
plt.title("Perfusion right HAT at Scan 4")
plt.savefig("boxplot_hat_right_tp4", bbox_inches='tight')


# ----------------- Variation across groups - regression plots --------------

# --------------------------------- Control ---------------------------

# Plot change in perfusion left and right HAT - Control 


sns.set_theme(style="whitegrid")
sns.relplot(data=ctrl, x='Timepoint', y='Left', hue='Participant', palette=sns.color_palette('colorblind',n_colors=9), style='Participant', s=100)
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Timepoint')
plt.ylim(20,65)
plt.title("Perfusion Left HAT - Control ")
plt.savefig("vol_cbf_15_5/control_hat_left.png", bbox_inches='tight')
plt.close()

sns.set_theme(style="whitegrid")
sns.relplot(data=ctrl, x='Timepoint', y='Right', hue='Participant', palette=sns.color_palette('colorblind',n_colors=9), style='Participant', s=100)
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Timepoint')
plt.ylim(20,65)
plt.title("Perfusion Right HAT - Control ")
plt.savefig("vol_cbf_15_5/control_hat_right.png", bbox_inches='tight')
plt.close()

# Plot relative change in perfusion left and right HAT - Control 
fig,axs=plt.subplots()
sns.set_theme(style="whitegrid")
sns.regplot(data=input_relative[input_relative['Group'] == 'Control'], x='Timepoint', y='Left', ax=axs, color='blue')
plt.ylabel('Perfusion (%)')
plt.xlabel('Timepoint')
plt.ylim(-26,26)
plt.title("Relative perfusion Left HAT - Control ")
plt.savefig("vol_cbf_15_5/control_hat_left_rel.png", bbox_inches='tight')
plt.close()

fig,axs=plt.subplots()
sns.set_theme(style="whitegrid")
sns.regplot(data=input_relative[input_relative['Group'] == 'Control'], x='Timepoint', y='Right', ax=axs, color='blue')
plt.ylabel('Relative perfusion (%)')
plt.xlabel('Timepoint')
plt.ylim(-26,26)
plt.title("Perfusion Right HAT - Control ")
plt.savefig("vol_cbf_15_5/control_hat_right_rel.png", bbox_inches='tight')
plt.close()


# --------------------------------- ECT ---------------------------

# Plot change in perfusion left and right HAT - ECT 

sns.set_theme(style="whitegrid")
sns.relplot(data=ect, x='Timepoint', y='Left', hue='Participant', palette=sns.color_palette('colorblind',n_colors=9), style='Participant', s=100)
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Timepoint')
plt.ylim(20,65)
plt.title("Perfusion Left HAT - ECT ")
plt.savefig("vol_cbf_15_5/ect_hat_left.png", bbox_inches='tight')
plt.close()

sns.set_theme(style="whitegrid")
sns.relplot(data=ect, x='Timepoint', y='Left', hue='Participant', palette=sns.color_palette('colorblind',n_colors=9), style='Participant', s=100)
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Timepoint')
plt.ylim(20,65)
plt.title("Perfusion Right HAT - ECT ")
plt.savefig("vol_cbf_15_5/ect_hat_right.png", bbox_inches='tight')
plt.close()

# Plot relative change in perfusion left and right HAT - ECT 

fig,axs=plt.subplots()
sns.set_theme(style="whitegrid")
sns.regplot(data=input_relative[input_relative['Group'] == 'ECT'], x='Timepoint', y='Left', ax=axs, color='blue')
plt.ylabel('Perfusion (%)')
plt.xlabel('Timepoint')
plt.ylim(-26,26)
plt.title("Relative perfusion Left HAT - ECT ")
plt.savefig("vol_cbf_15_5/ect_hat_left_rel.png", bbox_inches='tight')
plt.close()

fig,axs=plt.subplots()
sns.set_theme(style="whitegrid")
sns.regplot(data=input_relative[input_relative['Group'] == 'ECT'], x='Timepoint', y='Right', ax=axs, color='blue')
plt.ylabel('Relative perfusion (%)')
plt.xlabel('Timepoint')
plt.ylim(-26,26)
plt.title("Perfusion Right HAT - ECT ")
plt.savefig("vol_cbf_15_5/ect_hat_right_rel.png", bbox_inches='tight')
plt.close()

# --------------------------------- TMS ---------------------------

# Plot change in perfusion left and right HAT - TMS 

sns.set_theme(style="whitegrid")
sns.relplot(data=tms, x='Timepoint', y='Left', hue='Participant', palette=sns.color_palette('colorblind',n_colors=10), style='Participant', s=100)
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Timepoint')
plt.ylim(20,65)
plt.title("Perfusion Left HAT - TMS ")
plt.savefig("vol_cbf_15_5/tms_hat_left.png", bbox_inches='tight')
plt.close()

sns.set_theme(style="whitegrid")
sns.relplot(data=tms, x='Timepoint', y='Left', hue='Participant', palette=sns.color_palette('colorblind',n_colors=10), style='Participant', s=100)
plt.ylabel('Perfusion (mL/100g/min)')
plt.xlabel('Timepoint')
plt.ylim(20,65)
plt.title("Perfusion Right HAT - TMS ")
plt.savefig("vol_cbf_15_5/tms_hat_right.png", bbox_inches='tight')
plt.close()

# Plot relative change in perfusion left and right HAT - TMS 

fig,axs=plt.subplots()
sns.set_theme(style="whitegrid")
sns.regplot(data=input_relative[input_relative['Group'] == 'TMS'], x='Timepoint', y='Left', ax=axs, color='blue')
plt.ylabel('Perfusion (%)')
plt.xlabel('Timepoint')
plt.ylim(-26,26)
plt.title("Relative perfusion Left HAT - TMS ")
plt.savefig("vol_cbf_15_5/tms_hat_left_rel.png", bbox_inches='tight')
plt.close()

fig,axs=plt.subplots()
sns.set_theme(style="whitegrid")
sns.regplot(data=input_relative[input_relative['Group'] == 'TMS'], x='Timepoint', y='Right', ax=axs, color='blue')
plt.ylabel('Relative perfusion (%)')
plt.xlabel('Timepoint')
plt.ylim(-26,26)
plt.title("Perfusion Right HAT - TMS ")
plt.savefig("vol_cbf_15_5/tms_hat_right_rel.png", bbox_inches='tight')
plt.close()




