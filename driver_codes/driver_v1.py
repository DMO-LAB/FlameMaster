import pandas as pd
import subprocess as sp
import numpy as np
import os
import glob
import shutil


#Block 1
df = pd.read_csv('~/Documents/DMO/Spring_2023/Updated_UFPV/Update_table_incorrect/CH4_init/syms.out',header=1,sep='\t')
df_sort = (np.sort(df['chi_st']))
src_dir = './Output'
res_name = 'syms_driver1.out'
current_dir = './'
line_number = 39
for i in range(0,29):
    new_value = 'Scalar DissipationRate = ' + str(df_sort[i])
    with open('FlameMaster.input', 'r') as file:
        content = file.readlines()

    content[line_number - 1] = new_value + '\n'

    with open('FlameMaster.input', 'w') as file:
        file.writelines(content)
    
    # sp.run("source ~/FlameMaster/Bin/bin/Source.zsh")
  
    dest_dir ='output_'+str(df_sort[i])
    res_out = 'syms_driver1_'+str(df_sort[i])
    dat_out = './results'
    os.mkdir(dest_dir)
    sp.run('./run_driver1.zsh')
    #sp.run('./pp.zsh')
    for file_path in glob.glob(os.path.join(src_dir, "*")):
        shutil.move(file_path, dest_dir)
    for res_path in glob.glob(os.path.join(current_dir,res_name)):
        shutil.move(res_path,dat_out)
        os.rename(os.path.join(dat_out, os.path.basename(res_path)),os.path.join(dat_out,res_out))


# max_chi = 758.238
# rounded_num = round(max_chi / 100) * 100

# folder_path = "./middle_steady"
# file_name = 'CH4_p01_0chi560.878tf0314to1355Tst1792'
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
# source_file_path = os.path.join('/Users/ori/Desktop/Updated_UFPV/CH4_init/OutMethane',file_name)
# input_file_path = '/Users/ori/Desktop/Updated_UFPV/middle_steady/FlameMaster.input'
# run_script = 'run.zsh'
# destination_file_path = folder_path
# shutil.copy(source_file_path, destination_file_path)
# shutil.copy(input_file_path,destination_file_path)

# print("Files for middle branch copied successfully.")

# print('Starting Middle Steady Solution')

