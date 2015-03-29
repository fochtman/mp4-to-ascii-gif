#!/usr/bin/env python 

# modified from https://github.com/KinmanCovey/ascii-factory

from PIL import Image
import os
import sys
from subprocess import *

def get_shell_cmd_output(cmd_str):
    return Popen(cmd_str, stdout=PIPE, shell=True).communicate()[0]

enclosing_dir = os.path.join(os.path.abspath('.'), sys.argv[1])
os.chdir(enclosing_dir)
txt_dir = 'imgs_txt' 
if not os.path.isdir(txt_dir):
    os.mkdir(txt_dir)


cmd_str = 'ls | wc -l'
number_of_jobs = int(get_shell_cmd_output(cmd_str)) - 1
num_digits = 4

for i in range(number_of_jobs):
    str_i = str(i+1) 
    zeros = (num_digits - len(str_i)) * '0'
    
    filename = zeros + str_i + '.jpg'

    text_file = open(txt_dir + '/' + filename + ".txt", "w")
       
    w, h = image.size
    scale_x = 10 
    scale_y = 20 
        
    obj = image.load()

    r_list = []
    g_list = []
    b_list = []

    r_avg = 0
    g_avg = 0
    b_avg = 0
    i_avg = 0

    r_min = 255
    g_min = 255
    b_min = 255

    count = 0

    for i in range(0, h):
        for j in range(0, w):
            if len(obj[j,i]) == 3:
                r, g, b = obj[j,i]
            elif len(obj[j,i]) == 4:
                r, g, b, a = obj[j,i]
            if r < r_min:
                r_min = r

            if g < g_min:
                g_min = g

            if b < b_min:
                b_min = b

            # Analytical data
            if r > g and r > b:
                r_list.append(r)
            elif g > r and g > b:
                g_list.append(g)
            elif b > r and b > g:
                b_list.append(b)

            count += 1


    #Find the averages
    for i in range(0, len(r_list)):
        r_avg += r_list[i]

    for i in range(0, len(g_list)):
        g_avg += g_list[i]

    for i in range(0, len(b_list)):
        b_avg += b_list[i]

    #print len(r_list)

    i_avg = (r_avg + g_avg + b_avg) / count
    if len(r_list) > 0:
        r_avg = r_avg / len(r_list)
    if len(g_list) > 0:
        g_avg = g_avg / len(g_list)
    if len(b_list) > 0:
        b_avg = b_avg / len(b_list)

    # And here's where the magic happens
    for i in range(0, h):
        for j in range(0, w):
            if i % scale_y == 0 and j % scale_x == 0:
                if len(obj[j,i]) == 3:
                    r, g, b = obj[j,i]
                elif len(obj[j,i]) == 4:
                    r, g, b, a = obj[j,i]
                    
                if r <= r_min + 25 and g <= g_min + 25 and b <= b_min + 25:
                    #sys.stdout.write("#")
                    text_file.write("#")
                elif r <= r_min + 50 and g <= g_min + 50 and b <= b_min + 50:
                    #sys.stdout.write("%")
                    text_file.write(" ")
                elif r <= r_min + 75 and g <= g_min + 75 and b <= b_min + 75:
                    #sys.stdout.write("I")
                    text_file.write("I")
                elif r <= r_min + 100 and g <= g_min + 100 and b <= b_min + 100:
                    #sys.stdout.write("i")
                    text_file.write("i")
                elif r <= r_min + 125 and g <= g_min + 125 and b <= b_min + 125:
                    #sys.stdout.write("!")
                    text_file.write("!")
                elif r <= r_min + 150 and g <= g_min + 150 and b <= b_min + 150:
                    #sys.stdout.write("+")
                    text_file.write("+")
                elif r <= r_min + 175 and g <= g_min + 175 and b <= b_min + 175:
                    #sys.stdout.write(":")
                    text_file.write(":")
                elif r <= r_min + 200 and g <= g_min + 200 and b <= b_min + 200:
                    #sys.stdout.write("-")
                    text_file.write("-")
                elif r <= r_min + 225 and g <= g_min + 225 and b <= b_min + 225:
                    #sys.stdout.write("'")
                    text_file.write("'")
                elif r >= r_min + 250 and g >= g_min + 250 and b >= b_min + 250:
                    #sys.stdout.write(" ")
                    text_file.write(" ")
                elif r > b and g > b and r > r_avg and g > g_avg: # Yellows
                    #sys.stdout.write("`")
                    text_file.write("`")
                elif r > g and b > g and r > r_avg and b > b_avg: # Purps
                    #sys.stdout.write("%")
                    text_file.write(" ")
                elif g > r and b > r and g > g_avg and b > b_avg: # Cyans
                    #sys.stdout.write(";")
                    text_file.write(";")
                elif r > g and r > b and r > r_avg: # Reds 
                    #sys.stdout.write("$")
                    text_file.write("$")
                elif g > r and g > b and g > g_avg: # Greens 
                    #sys.stdout.write(",")
                    text_file.write(",")
                elif b > g and b > r and b > b_avg: # Blues
                    #sys.stdout.write("\"")
                    text_file.write("\"")
                else:
                    #sys.stdout.write(".")
                    text_file.write(" ")
        if i % scale_y == 0:
            #print
            text_file.write("\n")

    text_file.close()



