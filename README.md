# FlameMaster
scripts and case setup to generate a UFPV table.


This workflow is fully automated.'driver_v#'.py is the code that modifies/executes/copies the requried files for running FlameMaster
depending on the location on the S-Curve.
All the Listtools scripts are in scripts_syms folder where it can be modified to obtain the desired output.
The script full_run.zsh is used to run the solution for the full S-shaped curve.


TO generate the dataset, the first initial solution must be run with arclength = True to determine the locations of chi values for upper,middle and lower branches. 

The values can be updated in the respective driver_v# codes.
