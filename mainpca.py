import numpy as np
import matplotlib.pyplot as plt
import time
import cPickle as pickle
from inc_files import *    

img_model_path = 'img_model.p'
vec_model_path = 'vec_model.p'

with open(img_model_path, "rb") as model_file:
    data = pickle.load(model_file)

with open(vec_model_path, "rb") as model_file:
    eigenVectors = pickle.load(model_file)

temp = eigenVectors 
temp_data = data 
matrix = get_image_pix()

x , y = shape(matrix)
print "  >>> original dimensions" , x ,"X", y ," = " , x*y
while True:
    
    pc = raw_input("  >>> How many principle component : ") 

    if pc == "":
        continue
    if pc.lower() == 'exit':
        print '  >>> good bye !!'
        break


    try:
        pc = int(pc)
        start_time =time.time()
        eigenVectors = eigenVectors[:,:pc]

        s = np.dot(transpose(eigenVectors),transpose(data)) 

        data = transpose(s)

        ss= np.dot(data,transpose(eigenVectors)).T + mean_of_matrix(matrix)

        print("  >>> %s seconds" % (time.time() - start_time))
        print "  >>> New dimensions" , pc ,"X", len(eigenVectors) ," = " , pc*len(eigenVectors)

        x , y = shape(ss)

        eigenVectors = temp
        data = temp_data
        approximation = ss.reshape(-1,x,y)
        fig4, axarr = plt.subplots(2,1,figsize=(8,8))
        approximation = approximation.astype('float')

        axarr[0].imshow(matrix,cmap='gray')
        axarr[0].set_title('original')
        axarr[0].axis('off')

        axarr[1].imshow(approximation[0,],cmap='gray')
        axarr[1].set_title(str(pc)+' Component')
        axarr[1].axis('off')
        plt.show()

    except:
        print '  >>> input should be integer only !!'
        