import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

df_abs = pd.read_csv("dataframe_cbf_volumes.csv")

df_change = pd.read_csv("dataframe_change.csv")

# Split up df_change into (tp1, tp3, tp4) and (tp2,tp5) 

use_reg = [1, 3, 4]
not_use_reg = [2, 5]

df_change_regress = df_change[df_change['Timepoint'].isin(use_reg)].reset_index(drop=True)
df_change_other = df_change[df_change['Timepoint'].isin(not_use_reg)].reset_index(drop=True)

# --------------------------------------------- Volumes ----------------------------------------------

# --------------------------------------------- ECT --------------------------------------------------

# Left Hippocampus 
sns.set_theme(style="whitegrid")
sns.relplot(data=df_abs[df_abs['Group']=='ECT'], x='Timepoint', y='Left-Hippocampus', hue='Participant', palette=sns.color_palette('colorblind',n_colors=9), style='Participant', s=100)
plt.ylabel('Volume (mm³)')
plt.xlabel('Timepoint')
plt.title("Volume in Left Hippocampus")
plt.savefig("vol_cbf_15_5/volume_ect_left_hippo.png", bbox_inches='tight')
plt.close()


fig, axs = plt.subplots() 
sns.set_theme(style="whitegrid")
sns.regplot(data=df_change_regress[df_change_regress['Group']=='ECT'], x='Timepoint', y='Left-Hippocampus', ax=axs, color='blue')
sns.scatterplot(data=df_change_other[df_change_other['Group']=='ECT'], x='Timepoint', y='Left-Hippocampus', ax=axs, color='orange', marker="s")
plt.ylabel('Volume change (%)')
plt.xlabel('Timepoint')
plt.ylim(-6,6)
plt.title("Volume change in Left Hippocampus")
plt.savefig("vol_cbf_15_5/volume_ect_left_hippo_change.png", bbox_inches='tight')
plt.close()


# Right Hippocampus 
sns.set_theme(style="whitegrid")
sns.relplot(data=df_abs[df_abs['Group']=='ECT'], x='Timepoint', y='Right-Hippocampus', hue='Participant', palette=sns.color_palette('colorblind',n_colors=9), style='Participant', s=100)
plt.ylabel('Volume (mm³)')
plt.xlabel('Timepoint')
plt.title("Volume in Right Hippocampus")
plt.savefig("vol_cbf_15_5/volume_ect_right_hippo.png", bbox_inches='tight')
plt.close()

fig, axs = plt.subplots() 
sns.set_theme(style="whitegrid")
sns.regplot(data=df_change_regress[df_change_regress['Group']=='ECT'], x='Timepoint', y='Right-Hippocampus', ax=axs, color='blue')
sns.scatterplot(data=df_change_other[df_change_other['Group']=='ECT'], x='Timepoint', y='Right-Hippocampus', ax=axs, color='orange', marker="s")
plt.ylabel('Volume change (%)')
plt.xlabel('Timepoint')
plt.ylim(-6,6)
plt.title("Volume change in Right Hippocampus")
plt.savefig("vol_cbf_15_5/volume_ect_right_hippo_change.png", bbox_inches='tight')
plt.close()

# Right Amygdala 
sns.set_theme(style="whitegrid")
sns.relplot(data=df_abs[df_abs['Group']=='ECT'], x='Timepoint', y='Right-Amygdala', hue='Participant', palette=sns.color_palette('colorblind',n_colors=9), style='Participant', s=100)
plt.ylabel('Volume (mm³)')
plt.xlabel('Timepoint')
plt.title("Volume in Right Amygdala")
plt.savefig("vol_cbf_15_5/volume_ect_right_amygdala.png", bbox_inches='tight')
plt.close()

fig, axs = plt.subplots() 
sns.set_theme(style="whitegrid")
sns.regplot(data=df_change_regress[df_change_regress['Group']=='ECT'], x='Timepoint', y='Right-Amygdala', ax=axs, color='blue')
sns.scatterplot(data=df_change_other[df_change_other['Group']=='ECT'], x='Timepoint', y='Right-Amygdala', ax=axs, color='orange', marker="s")
plt.ylabel('Volume change (%)')
plt.xlabel('Timepoint')
plt.ylim(-6,6)
plt.title("Volume change in Right Amygdala")
plt.savefig("vol_cbf_15_5/volume_ect_right_amygdala_change.png", bbox_inches='tight')
plt.close()

# Right Thalamus 
sns.set_theme(style="whitegrid")
sns.relplot(data=df_abs[df_abs['Group']=='ECT'], x='Timepoint', y='Right-Thalamus', hue='Participant', palette=sns.color_palette('colorblind',n_colors=9), style='Participant', s=100)
plt.ylabel('Volume (mm³)')
plt.xlabel('Timepoint')
plt.title("Volume in Right Thalamus")
plt.savefig("vol_cbf_15_5/volume_ect_right_thalamus.png", bbox_inches='tight')
plt.close()

fig, axs = plt.subplots() 
sns.set_theme(style="whitegrid")
sns.regplot(data=df_change_regress[df_change_regress['Group']=='ECT'], x='Timepoint', y='Right-Thalamus', ax=axs, color='blue')
sns.scatterplot(data=df_change_other[df_change_other['Group']=='ECT'], x='Timepoint', y='Right-Thalamus', ax=axs, color='orange', marker="s")
plt.ylabel('Volume change (%)')
plt.xlabel('Timepoint')
plt.ylim(-6,6)
plt.title("Volume change in Right Thalamus")
plt.savefig("vol_cbf_15_5/volume_ect_right_thalamus_change.png", bbox_inches='tight')
plt.close()


# --------------------------------------------- TMS --------------------------------------------------
# Right Hippocampus 
sns.set_theme(style="whitegrid")
sns.relplot(data=df_abs[df_abs['Group']=='TMS'], x='Timepoint', y='Right-Hippocampus', hue='Participant', palette=sns.color_palette('colorblind',n_colors=10), style='Participant', s=100)
plt.ylabel('Volume (mm³)')
plt.xlabel('Timepoint')
plt.title("Volume in Right Hippocampus")
plt.savefig("vol_cbf_15_5/volume_tms_right_hippo.png", bbox_inches='tight')
plt.close()

fig, axs = plt.subplots() 
sns.set_theme(style="whitegrid")
sns.regplot(data=df_change_regress[df_change_regress['Group']=='TMS'], x='Timepoint', y='Right-Hippocampus', ax=axs, color='blue')
sns.scatterplot(data=df_change_other[df_change_other['Group']=='TMS'], x='Timepoint', y='Right-Hippocampus', ax=axs, color='orange', marker="s")
plt.ylabel('Volume change (%)')
plt.xlabel('Timepoint')
plt.ylim(-6,6)
plt.title("Volume change in Right Hippocampus")
plt.savefig("vol_cbf_15_5/volume_tms_right_hippo_change.png", bbox_inches='tight')
plt.close()

# Right Thalamus 
sns.set_theme(style="whitegrid")
sns.relplot(data=df_abs[df_abs['Group']=='TMS'], x='Timepoint', y='Right-Thalamus', hue='Participant', palette=sns.color_palette('colorblind',n_colors=10), style='Participant', s=100)
plt.ylabel('Volume (mm³)')
plt.xlabel('Timepoint')
plt.title("Volume in Right Thalamus")
plt.savefig("vol_cbf_15_5/volume_tms_right_thalamus.png", bbox_inches='tight')
plt.close()

fig, axs = plt.subplots() 
sns.set_theme(style="whitegrid")
sns.regplot(data=df_change_regress[df_change_regress['Group']=='TMS'], x='Timepoint', y='Right-Thalamus', ax=axs, color='blue')
sns.scatterplot(data=df_change_other[df_change_other['Group']=='TMS'], x='Timepoint', y='Right-Thalamus', ax=axs, color='orange', marker="s")
plt.ylabel('Volume change (%)')
plt.xlabel('Timepoint')
plt.ylim(-6,6)
plt.title("Volume change in Right Thalamus")
plt.savefig("vol_cbf_15_5/volume_tms_right_thalamus_change.png", bbox_inches='tight')
plt.close()

