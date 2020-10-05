import cv2
import sys
import numpy as np
im = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
for i in range(512):
    for j in range(512):
        if(im[i][j]<128):
            im[i][j] = 0
        else:
            im[i][j] = 255


array = [[0 for i in range(514)] for j in range(514)]
array = np.array(array)

for i in range(512):
    for j in range(512):
        if(im[i][j] == 255):
            array[i+1][j+1] = 1
temp_group = 1
for i in range(512):
    for j in range(512):
        if(array[i+1][j+1] == 1):
            array[i+1][j+1] = temp_group
            temp_group = temp_group + 1
###################################################
for i in range(1,513):
    for j in range(1,513):
        if(array[i][j]>0):
            neighbor = [array[i-1][j],array[i][j-1],array[i][j+1],array[i+1][j],array[i][j]]
            array[i][j] = min([n for n in neighbor if n>0])
####################################################
change = 1
while(change):
    change = 0
    for i in range(1,513):
        for j in range(1,513):
            if(array[513-i][513-j]>0):
                neighbor = [array[513-i-1][513-j],array[513-i][513-j-1],array[513-i][513-j+1],array[513-i+1][513-j],array[513-i][513-j]]
                if(min([n for n in neighbor if n>0]) != array[513-i][513-j] ):
                    change = 1
                array[513-i][513-j] = min([n for n in neighbor if n>0])
#####################################################
group_number = np.amax(array)
group_array = [0]*(group_number+1)
for i in range(512):
    for j in range(512):
        group_array[array[i+1][j+1]-1] = group_array[array[i+1][j+1]-1] + 1
for i in range(group_number):
    if(group_array[i]>500):
        print(group_array[i])

