from PIL import Image
from numpy import *
from pylab import *
from pca_1 import pca
import os
import matplotlib.pyplot as plt


# allfiles = os.listdir(os.getcwd())
# imlist = [filename for filename in allfiles if filename == '00.png']
# im = array(Image.open(imlist[0])) # open one image to get size
# m,n = im.shape[0:2] # get the size of the images
# imnbr = len(imlist) # get the number of images

# # create matrix to store all flattened images
# immatrix = array([array(Image.open(im)).flatten()
#               for im in imlist],'f')

image_file = "00.png"
img = Image.open(image_file).convert('L')
width, height = img.size
m,n = img.size
# width-= width
xx =list(img.getdata())
immatrix = [xx[i*width:(i+1)*width] for i in range((len(xx)+width-1)//width)]

immatrix = array(immatrix)

# perform PCA
V,S,immean = pca(immatrix)


approximation = V.reshape(-1,m,n)

# approximation = dot(approximation,immean)

print immatrix
approximation = approximation.astype('float64')

fig4, axarr = plt.subplots(2,1,figsize=(8,8))
axarr[0].imshow(immatrix,cmap='gray')
axarr[0].set_title('original')
axarr[0].axis('off')

axarr[1].imshow(approximation[0,],cmap='gray')
axarr[1].set_title('% Variation')
axarr[1].axis('off')


plt.show()
