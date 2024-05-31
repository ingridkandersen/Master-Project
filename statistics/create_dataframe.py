#This script creates the dataframe with both volume and CBF data   

import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 


# Read the data using pandas. 
# There is a different spacing between each column, hence the "\s+". 
# Column 5 contains the mean values 

group = []
part = [] 
tps = []

control_participants = ['FXXXXX','FYYYYY','FZZZZZ']
control_n_tps_range = [3,4,5] #This is n_tps+1 

ect_participants = ['FXXXXX','FYYYYY','FZZZZZ'] 
ect_n_tps_range = [3,4,5]    

tms_participants = ['FXXXXX','FYYYYY','FZZZZZ']
tms_n_tps_range = [3,4,5]


# ----------------------------------------------- Creating Dataframe with CBF -------------------------------

cbf_names_frame = pd.read_csv("Kontroll/CBF_calc/FXXXXX/CBF_1.txt", skiprows=55, sep="\s+", usecols=[4], header=None)

cbf_names_list = cbf_names_frame[4].tolist() #4 because it is column 4 in the original frame 

cbf_names = [n + '-CBF' for n in cbf_names_list]

df_cbf = pd.DataFrame(columns=cbf_names)

#print(len(cbf_names_list)) #42 



# ----------------------------------------------- Finding CBF --------------------------------

# Looping though Controls 
# All controls skips 15 day follow-up (if-else)
for index, F in enumerate(control_participants): 
	for i in range(1,control_n_tps_range[index]): 
		string_path = "/Kontroll/CBF_calc/" + F + "/CBF_" + str(i) + ".txt"
		control = pd.read_csv(string_path, skiprows=54, sep="\s+", usecols=[5], header=None)
		group.append('Kontroll')
		part.append(int(index+1))
		if i <3: 
			tps.append(int(i)) 
		else:
			tps.append(int(i+1))
		
		cbf_values_list = []
		for i in range(42): 
			cbf_values_list.append(float(control.iloc[i]))
		df_cbf.loc[len(df_cbf)] = cbf_values_list

print(df_cbf)


# Looping thorugh ECT  
for index, F in enumerate(ect_participants): 
	for i in range(1,ect_n_tps_range[index]): 
		string_path = "/home/fundect/ECT/CBF_calc/" + F + "/CBF_" + str(i) + ".txt"
		ect = pd.read_csv(string_path, skiprows=54, sep="\s+", usecols=[5], header=None)
		group.append('ECT')
		part.append(int(index+1))
		# Exceptions - skipped scans for singular participants 
		if F == 'FXXXXX' and i >=4: 
			tps.append(int(i+1))
		elif F == 'FYYYYY' and i >=3: 
			tps.append(int(i+1))
		else:
			tps.append(int(i)) 	
		
		cbf_values_list = []
		for i in range(42): 
			cbf_values_list.append(float(ect.iloc[i]))
		df_cbf.loc[len(df_cbf)] = cbf_values_list


# Looping thorugh TMS 
for index, F in enumerate(tms_participants): 
	for i in range(1,tms_n_tps_range[index]): 
		string_path = "TMS/CBF_calc/" + F + "/CBF_" + str(i) + ".txt"
		tms = pd.read_csv(string_path, skiprows=54, sep="\s+", usecols=[5], header=None)
		group.append('TMS')
		part.append(int(index+1))
		# Exceptions 
		if F == 'FXXXXX' and i >=3: 
			tps.append(int(i+1))
		else:
			tps.append(int(i)) 
		cbf_values_list = []
		for i in range(42): 
			cbf_values_list.append(float(tms.iloc[i]))
		df_cbf.loc[len(df_cbf)] = cbf_values_list


# ----------------------------------- Reading volume data from csv ----------------------

volumes1 = pd.read_csv("asegstats.txt", sep="\s+")
volumes = volumes1.iloc[:,volumes1.columns != 'Measure:volume']
print(volumes)

print(df_cbf)
# --------------------------- Creating Pandas dataframe with all the data -----------------
data = {'Group' : group, 'Participant' : part, 'Timepoint' : tps}
info = pd.DataFrame(data)
print(info)

df = pd.concat([info, df_cbf, volumes], axis=1)

df.to_csv("dataframe_cbf_volumes.csv", index=False)
print(df) 






