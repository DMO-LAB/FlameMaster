import pandas as pd
import subprocess as sp
import numpy as np
import os
import glob
import shutil
max_chi = 757.277
rounded_num = round(max_chi / 100) * 100
output_dir = "./OutMethane"
src_dir = './Output'
res_name = 'syms.out'
current_dir = './'
line_number=79
start1 = 700
end1 = 100
step1 = -100

start2 = 100
end2 = 60
step2 = -10

# read the file content and split it into lines
with open('FlameMaster.input', 'r') as file:
    content = file.read()
lines = content.split('\n')

# insert the new lines at the desired location
insert_index = 79  # index where the new lines should be inserted
new_lines = []
for i in range(start1, end1, step1):
    new_lines.append('Scalar DissipationRate = ' + str(i))
for i in range(start2, end2, step2):
    new_lines.append('Scalar DissipationRate = ' + str(i))
lines[insert_index:insert_index] = new_lines

# write the updated content back to the file
with open('FlameMaster.input', 'w') as file:
    file.write('\n'.join(lines))

sp.run('./run_driver2.zsh')
