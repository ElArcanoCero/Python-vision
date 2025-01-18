import numpy as np
import cv2

img1 = cv2.imread('/Users/Arcano/Desktop/img4.png', 0) # Leemos la imagene
img2 = cv2.imread('/Users/Arcano/Desktop/img4.png', 0) # Leemos la imagene
img3 = cv2.imread('/Users/Arcano/Desktop/img4.png', 0) # Leemos la imagene  

fil, colmn = img1.shape[:2]  # Obtenemos sus dimensiones height alto width ancho


for i in range(0, fil-1):
    for j in range(0, colmn-1):
        k1 = np.array([ [img1[i-1,j-1], img1[i-1,j], img1[i-1,j+1]],
                        [img1[i,j-1],   img1[i,j],   img1[i,j+1]],
                        [img1[i+1,j-1], img1[i+1,j], img1[i+1,j+1]]])
        img2[i,j] = int(np.median(k1)) 
  
hist, bins = np.histogram(img2.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()// cdf.max()
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255//(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img3 = cdf[img2] 

for i in range(0, fil-1):
    for j in range(0, colmn-1):
        if img3[i,j]<= 1 :
            k1 = np.array([ [img2[i-1,j-1], img2[i-1,j], img2[i-1,j+1]],
                            [img2[i,j-1],   img2[i,j],   img2[i,j+1]],
                            [img2[i+1,j-1], img2[i+1,j], img2[i+1,j+1]]])
            img2[i,j] = round(np.median(k1)) 
           
        if img3[i,j]>= 254 :
            k1 = np.array([ [img2[i-1,j-1], img2[i-1,j], img2[i-1,j+1]],
                            [img2[i,j-1],   img2[i,j],   img2[i,j+1]],
                            [img2[i+1,j-1], img2[i+1,j], img2[i+1,j+1]]])
            img2[i,j] = round(np.median(k1))  
        k1 = np.array([ [img2[i-1,j-1], img2[i-1,j], img2[i-1,j+1]],
                        [img2[i,j-1],   (img2[i,j]),   img2[i,j+1]],
                        [img2[i+1,j-1], img2[i+1,j], img2[i+1,j+1]]])
        pro = round(np.mean(k1))
        if img2[i,j] >= pro + 30 :
            img2[i,j] = pro - 30   
        if img2[i,j] <= pro - 30 :    
            img2[i,j] = pro + 30
            
cv2.imshow('riudo gaussiano', img1)
cv2.imshow('imagen 2', img2)
cv2.imshow('imagen 3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()


