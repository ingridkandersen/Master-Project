The files in this folder perform all the statistical analyses for the dataset 

1. volumes.sh 
Extracts all the volumetric data from the aseg.stats files for each timepoint 
Could probably be more efficient to type via some for loop, but it was sufficient for the small dataset. 

2. create_dataframe.py 
Creates a large dataframe consisting of all volumetric and CBF values for all ROIs for all participants and timepoints (so very large)
Must be made before any other scrips are run; it is my Rome and all scripts lead back to this somehow 

3. calculate_change.py
Calculates the change in percent for all values compared to a base (mean of all timepoints for that participant.)
Example: participant X has N timepoints. The relative hippocampal volume at tp1 = (X_1 - ((X_1 + ... + X_N))/N)/((X_1 + ... + X_N)/N)

4. total_headsize.py 
Performs the analysis on total headsize, and plots the boxplot 

5. statistical_analysis.py 
Performs statistical analyses (students t-test) on the volumetric data, and makes a CSV file 

6. plotting_roi.py 
Plots the areas with significance (p<0.05) in the volumetric data 

7. perfusion_analysis.py 
Performs the the analysis for the perfusion data 
Combines Hippocampus, Amygdala and Thalamus (HAT), calculates mean and laterality index for the smaller tables 

8. ttest_cbf.py 
Performs the statistical analyses on the perfusion data. 
