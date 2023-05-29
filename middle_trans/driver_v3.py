import pandas as pd
import subprocess as sp
import numpy as np
import os
import glob
import shutil
start1 = 700
end1 = 100
step1 = -100

start2 = 100
end2 = 60
step2 = -10
i_values = []
# iterate over the values of i and append them to the list
for i in range(start1, end1, step1):
    i_values.append(i)
for i in range(start2, end2, step2):
    i_values.append(i)
src_dir = './Output'
res_name = 'syms_driver3.out'
current_dir = './'
line_number = 39
line_number_sp = 23
ip_path = './initial_profiles'
ip_files = os.listdir(ip_path)

for i ,a,in enumerate(i_values):
    if a <=90:
        sp_name = f'CH4_p01_0chi000{a}tf0320to1350'
        new_ip = f'StartProfilesFile is ./CH4_p01_0chi000{a}tf0320to1350'
    else:
        sp_name = f'CH4_p01_0chi00{a}tf0320to1350'
        new_ip = f'StartProfilesFile is ./CH4_p01_0chi00{a}tf0320to1350'
    tpath = os.path.join(ip_path,sp_name)
    shutil.copy(tpath,current_dir)
    new_value = 'Scalar DissipationRate = ' + str(a-1)
    with open('FlameMaster.input', 'r') as file:
        content = file.readlines()

    content[line_number - 1] = new_value + '\n'
    content[line_number_sp -1] = new_ip +'\n'

    with open('FlameMaster.input', 'w') as file:
        file.writelines(content)
    
    # sp.run("source ~/FlameMaster/Bin/bin/Source.zsh")
    dest_dir ='output_'+str(a-1)
    res_out = 'syms_'+str(a-1)
    dat_out = './results'
    os.mkdir(dest_dir)
    sp.run('./run_driver3.zsh')
    for file_path in glob.glob(os.path.join(src_dir, "*")):
        shutil.move(file_path, dest_dir)
    for res_path in glob.glob(os.path.join(current_dir,res_name)):
        shutil.move(res_path,dat_out)
        os.rename(os.path.join(dat_out, os.path.basename(res_path)),os.path.join(dat_out,res_out))

    new_value = 'Scalar DissipationRate = ' + str(a+1)
    with open('FlameMaster.input', 'r') as file:
        content = file.readlines()

    content[line_number - 1] = new_value + '\n'

    with open('FlameMaster.input', 'w') as file:
        file.writelines(content)
    
    # sp.run("source ~/FlameMaster/Bin/bin/Source.zsh")
    dest_dir ='output_'+str(a+1)
    res_out = 'syms_driver3_'+str(a+1)
    dat_out = './results'
    os.mkdir(dest_dir)
    sp.run('./run_driver3.zsh')
    for file_path in glob.glob(os.path.join(src_dir, "*")):
        shutil.move(file_path, dest_dir)
    for res_path in glob.glob(os.path.join(current_dir,res_name)):
        shutil.move(res_path,dat_out)
        os.rename(os.path.join(dat_out, os.path.basename(res_path)),os.path.join(dat_out,res_out))