import os
import sys
from subprocess import *

def get_shell_cmd_output(cmd_str):
    return Popen(cmd_str, stdout=PIPE, shell=True).communicate()[0]

enclosing_dir = os.path.join(os.path.abspath('.'), sys.argv[1])
os.chdir(enclosing_dir)
txt_dir = 'ascii_imgs'

if not os.path.isdir(txt_dir):
    os.mkdir(txt_dir)

font_path = '/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf'
num_digits = 4

for i in range(int(get_shell_cmd_output('ls | wc -l')) - 1):
    str_i = str(i+1) 
    zeros = (num_digits - len(str_i)) * '0'
    f0 = zeros + str_i + '.jpg.txt'
    lines = open(f0, 'r').readlines()
    f = open(f0, 'w+')
    for i in range(len(lines)):
        x = list(lines[i])
        if i == 0:
            x[0] = '`'
            x[len(x)-2] = '`'
        if i == len(lines) - 1:
            x[0] = '`'
            x[len(x)-3] = 'T'
            x[len(x)-2] = 'F'
        f.write(''.join(x))
    f.close()
   
    file_path = txt_dir + '/' + str_i + '.jpg'
    cmd_str = 'cat {0} | convert -font {1} text:- -trim +repage {2}'.format(f0, font_path, file_path)
    os.system(cmd_str)

os.chdir(txt_dir)
os.system('convert *.jpg final.gif')
