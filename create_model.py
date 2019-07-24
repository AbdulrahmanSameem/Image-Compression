import cPickle as pickle
from PIL import Image
from math import sqrt
import numpy as np
from numpy import linalg as findEigen
import matplotlib.pyplot as plt
from inc_files import *    

def StandardScalerr(matrix ,std_deviation__,size,mean_of_mat):
    """
        Standardization 
        S = (X - Mu)/ Standard deviation 
    """
    std_deviation__ = map(lambda x : float(x),std_deviation__)
    std_out =[]
    i = 0 
    std = 0
    l = (size)
    for r in range(size):
        for c in range(size):
            try:
                ss = ((float(matrix[c][r])-mean_of_mat[r])/(std_deviation__[i]))
                # ss = round(ss,4)
                std_out.append(ss)
            except:
                std_out.append(0)
        i+=1
    i = 0
    sd = reshape(std_out,l)
    return sd

def std_deviation(mean_of_ma,matrix):
    """
        Find Standard Deviation 
        SQRT((pow(X- Mu)^2)/N)
    """
    row = len(matrix[0])
    col = len(matrix)
    x_mean =[]
    i = 0 
    st = 0.0
    l = len(mean_of_ma)
    for r in range(row):
        for c in range(col):
            st+=pow(float(matrix[c][r])-mean_of_ma[r],2)
        st = sqrt(st/col)
        x_mean.append(st)
    return x_mean

def cov_variance(norm_data,mean_of_mat):
    col = len(norm_data)
    row = len(norm_data[0])
    test = [[0 for x in range(col)] for y in range(row)]
    i = 0 
    sum_of_covar = 0
    freezrow  = 0
    flag = 1
    for r in range(row):
        for c in range(col):
            sum_of_covar+=np.dot(((norm_data[c][freezrow])-mean_of_mat[freezrow]),
                           ((norm_data[c][r])-mean_of_mat[i]))
            freezrow=freezrow
            test[r][c] = sum_of_covar
        i+=1
        sum_of_covar=0
        freezrow=freezrow
    for i in range(col):
        for j in range(i, col):
            test[j][i] = test[i][j]
    return test


def PCA(data):
    mean = mean_of_cov_matrix(data)
    data = np.array(data)
    mean = np.array(mean)
    # R = np.cov(data)
    R = cov_variance(data,mean)

    eigenValues, eigenVectors = findEigen.eig(R)
    idx = eigenValues.argsort()[::-1]
    eigenVectors = eigenVectors[:,idx]
    return data,eigenVectors


img_model_path = 'img_model.p'
vec_model_path = 'vec_model.p'

print "Creating Model ... "
matrix = get_image_pix()
mean_co = mean_of_cov_matrix(matrix)
size =len(mean_co)
final = StandardScalerr(matrix,std_deviation(mean_co,matrix),size,mean_co)

mat , eigenVectors =  PCA(final)

with open(img_model_path, "wb") as model_file:
    pickle.dump(mat, model_file)


with open(vec_model_path, "wb") as model_file:
    pickle.dump(eigenVectors, model_file)

print ".\n.\n.\n.\nModel has been created "
