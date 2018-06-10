#!/usr/bin/python
                                                                                                            
import sys
from numpy import *
import math
import numpy as np
from numpy.linalg import inv
import pydoop.hdfs as hdfs


def norm_pdf_multivariate(x, mu, sigma):
    size = len(x)
    if size == len(mu) and (size, size) == sigma.shape:
        det = linalg.det(sigma)
        if det == 0:
            raise NameError("The covariance matrix can't be singular")
        norm_const = 1.0/ ( math.pow((2*pi),float(size)/2) * math.pow(det,1.0/2) )
        x_mu = matrix(x - mu)
        inverse = inv(sigma)        
        result = math.pow(math.e, -0.5 * (x_mu * inverse * x_mu.T))
        return norm_const * result
    else:
        raise NameError("The dimensions of the input don't match")

#import pydoop.hdfs as hdfs
k=5

#using Hadoop system file
#with hdfs.open('/Users/ming/centroids.txt') as fp:

weights=[]
means=[]
sigmas=[]
with hdfs.open('/Users/user06/parameters.txt') as file:
  for line in file:
    params = line.strip().split("\t")
    weights.append(float(params[0]))
    means.append(np.array(params[1].split(),float))
    sigmas.append(np.array(params[2].split(),float))				
    		
    
for line in sys.stdin:
    line = line.strip()
    point = np.array(line.split(),float)
    p=weights[0] * norm_pdf_multivariate(point,means[0],sigmas[0].reshape((2,2)))
    nearest=0
    for i in range(1,k):
      q=weights[i] * norm_pdf_multivariate(point,means[i],sigmas[i].reshape((2,2)))
      if(q>=p):
           p=q
           nearest=i
    print('%d\t%d %f %f' %(nearest, 1, point[0], point[1]))