#!/usr/bin/python
                                                                                                            

import sys
import numpy as np

current_cluster = None
current_count = 0
current_x = 0
current_y = 0
current_xy=0
current_yy=0
current_xx=0
cluster = None
n=81920


for line in sys.stdin:
    line = line.strip()
    cluster, data = line.split('\t', 1)
    count, x, y = data.split()
                                                                       
    if current_cluster == cluster:
        current_count += int(count)
        current_x += float(x)
        current_y += float(y)
        current_xy +=float(x)*float(y)
        current_yy +=float(y)*float(y)
        current_xx +=float(x)*float(x)

    else:
        if current_cluster: #update weught mean 
            weight=float(current_count)/n
            mean=np.array([current_x/current_count,current_y/current_count])
            sigma=np.zeros((2,2),dtype=float)
            sigma[0,0]=current_xx-2*current_x*mean[0]-mean[0]**2
            sigma[1,1]=current_yy-2*current_y*mean[1]-mean[1]**2
            sigma[0,1]=current_xy-mean[0]*current_y-mean[1]*current_x-mean[0]*mean[1]
            sigma[1,0]=sigma[0,1]
            sigma=sigma/current_count
            print("%f\t%f %f\t%f %f %f %f\n" %(weight,mean[0],mean[1],sigma[0,0],sigma[0,1],sigma[1,0],sigma[1,1]))
        current_cluster = cluster
        current_count = int(count)
        current_x = float(x)
        current_y = float(y)
        current_xy=float(x)*float(y)
        current_yy=float(y)*float(y)
        current_xx=float(x)*float(x)

# do not forget to output the last cluster if needed!                                                                                    
if current_cluster == cluster:
    weight=float(current_count)/n
    mean=np.array([current_x/current_count,current_y/current_count])
    sigma=np.zeros((2,2),dtype=float)
    sigma[0,0]=current_xx-2*current_x*mean[0]-mean[0]**2
    sigma[1,1]=current_yy-2*current_y*mean[1]-mean[1]**2
    sigma[0,1]=current_xy-mean[0]*current_y-mean[1]*current_x-mean[0]*mean[1]
    sigma[1,0]=sigma[0,1]
    sigma=sigma/current_count
    print("%f\t%f %f\t%f %f %f %f\n" %(weight,mean[0],mean[1],sigma[0,0],sigma[0,1],sigma[1,0],sigma[1,1]))       
    
