#!/usr/bin/python
                                                                                                            

import numpy as np
import sys
import os
#import pydoop.hdfs as hdfs

k=5
eps=0.00001
#initial centroids from kmeans
filename="/home/sam/Dropbox/UMB/Spyder-workspace/Homework3/initCenters.txt"
centroids=[]
with open(filename) as file:
  for line in file:
    centers = line.strip().split()
    centroids.append([float(centers[0]), float(centers[1])])
				
#initial gaussian paraemters
filename="/home/sam/Dropbox/UMB/Spyder-workspace/Homework3/five.txt"
n=0
C0=[];C1=[];C2=[];C3=[];C4=[]
#assign centers to inputs
with open(filename) as file:
  for line in file:
    point = line.strip().split()
    n+=1
    x = float(point[0])
    y = float(point[1])
    dist = (x - centroids[0][0]) * (x - centroids[0][0]) + (y - centroids[0][1]) * (y - centroids[0][1])
    nearest = 0
    for i in range(1, k):
        d = (x - centroids[i][0]) * (x - centroids[i][0]) + (y - centroids[i][1]) * (y - centroids[i][1])
        if (d < dist):
            dist = d
            nearest = i
    locals()["C"+str(nearest)].append([x, y])

#initial weights,sigmas and means for each Gaussian
#w=np.zeros((1,k),float)	
mean=np.zeros((k,2), dtype=float)
output=open("/home/sam/Dropbox/UMB/Spyder-workspace/Homework3/parameters.txt", "w+")
#sigma0=sigma1=sigma2=sigma3=sigma4=np.zeros((2,2),dtype=float)
for i in range(0,k):
  sigma=np.zeros((2,2),float)
  C=np.matrix(locals()["C"+str(i)])
  #w[0,i]=(float(np.shape(C)[0])/n) #initial weight
  w=(float(np.shape(C)[0])/n)
  mean[i,:]=np.mean(np.matrix(C),axis=0) #initial mean
  m=mean[i,:]
  for j in range(0,np.shape(C)[0]):
     sigma+=np.dot((C[j,:]-m).T,C[j,:]-m)
  sigma=sigma/np.shape(C)[0]
  #locals()["sigma"+str(i)]=sigma#initial sigma
  output.write("%f\t%f %f\t%f %f %f %f\n" %(w,mean[i,0],mean[i,1],sigma[0,0],sigma[0,1],sigma[1,0],sigma[1,1]))
output.close()		
#write initials to a parameters.py


#iteration = 0
#while True:
#    os.system("hdfs dfs -rm -r -f /Users/user06/output")
#    os.system("hdfs dfs -put -f parameters.txt /Users/user06/parameters.txt")
#    os.system("mapred streaming -input /Users/user06/GMMs -output /Users/user06/output -file /home/user06/GMMs/mapper.py -mapper /ho\
#    me/user06/GMMs/mapper.py -file /home/user06/GMMs/reducer.py -reducer /home/user06/GMMs/reducer.py")
#    os.system("hdfs dfs -get -f /Users/user06/output/part-00000 .")
#    
#    iteration += 1
#    print 'iteration', iteration
#    os.system("cat parameters.txt")
#    print
#    os.system("cat part-00000")
#    if filecmp.cmp("parameters.txt", "part-00000"):
#        break
#    else:
#        os.system("mv part-00000 parameters.txt")










