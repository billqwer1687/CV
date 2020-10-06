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
#while(change):
for k in range(150):
    change = 0
    for i in range(1,513):
        for j in range(1,513):
            if(array[513-i][513-j]>0):
                neighbor = [array[513-i-1][513-j],array[513-i][513-j-1],array[513-i][513-j+1],array[513-i+1][513-j],array[513-i][513-j]]
#                if(min([n for n in neighbor if n>0]) != array[513-i][513-j] ):
#                    change = 1
                array[513-i][513-j] = min([n for n in neighbor if n>0])
#####################################################
group_number = np.amax(array)
group_array = [0]*(group_number+1)
group = [0]*5
t = 0
for i in range(512):
    for j in range(512):
        group_array[array[i+1][j+1]] = group_array[array[i+1][j+1]] + 1
for i in range(1,group_number):
    if(group_array[i]>500):
        group[t] = i
        t=t+1
cen_x = [0]*5
cen_y = [0]*5
group_axis = [[0 for i in range(5)] for j in range(5)]
for k in range(5):
    sum_x = 0
    sum_y = 0
    temp = 0
    for i in range(512):
        for j in range(512):
            if(array[i+1][j+1] == group[k]):
                sum_x = sum_x + j
                sum_y = sum_y + i
                temp = temp + 1
                if(group_axis[k][0]>j or group_axis[k][0] == 0):
                    group_axis[k][0] = j
                if(group_axis[k][1]>i or group_axis[k][1] == 0):
                    group_axis[k][1] = i
                if(group_axis[k][2]<j):
                    group_axis[k][2] = j
                if(group_axis[k][3]<i):
                    group_axis[k][3] = i
    cen_x[k] = int(sum_x/temp)
    cen_y[k] = int(sum_y/temp)
result = cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
for i in range(5):
    cv2.rectangle(result,(group_axis[i][0],group_axis[i][1]),(group_axis[i][2],group_axis[i][3]),(0,255,0),1)
    cv2.line(result,(cen_x[i]-5,cen_y[i]),(cen_x[i]+5,cen_y[i]),(0,0,255),1)
    cv2.line(result,(cen_x[i],cen_y[i]-5),(cen_x[i],cen_y[i]+5),(0,0,255),1)
cv2.imwrite('rec.jpg',result)        
