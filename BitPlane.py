import numpy as np
import cv2
import matplotlib.pyplot as plt 
# Read the image in grayscale
img = cv2.imread('wizard.jpg',0)
cv2.imshow('Orignal Image', img)
cv2.imwrite('Original_Image.jpg', img)
cv2.waitKey(0)

#Iterate over each pixel and change pixel value to binary and store it in the list
lst = []
for i in range(img.shape[0]):
      for j in range(img.shape[1]):
             lst.append(np.binary_repr(img[i][j] , width=8)) #width = no. of bits

# We have a list of string where each string represents binary pixel value
#To extract a bit plane we need to iterate over the strings and store charecters corresponding to to bit plane into list
#Multiply with 2^(n-1) and reshape to reconstuct the bit image

eight_bit_img = (np.array([int(i[0]) for i in lst], dtype = np.uint8) * 128).reshape(img.shape[0],img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst], dtype = np.uint8) * 64).reshape(img.shape[0],img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst], dtype = np.uint8) * 32).reshape(img.shape[0],img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst], dtype = np.uint8) * 16).reshape(img.shape[0],img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst], dtype = np.uint8) * 8).reshape(img.shape[0],img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst], dtype = np.uint8) * 4).reshape(img.shape[0],img.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst], dtype = np.uint8) * 2).reshape(img.shape[0],img.shape[1])
one_bit_img = (np.array([int(i[7]) for i in lst], dtype = np.uint8) * 1).reshape(img.shape[0],img.shape[1])

# Display and save the images corresponding to each bit plane

cv2.imwrite('bit plane7.jpg',cv2.normalize(eight_bit_img, np.zeros(img.shape), 0,255, cv2.NORM_MINMAX))
cv2.imwrite('bit plane6.jpg',cv2.normalize(seven_bit_img, np.zeros(img.shape), 0,255, cv2.NORM_MINMAX))
cv2.imwrite('bit plane5.jpg',cv2.normalize(six_bit_img, np.zeros(img.shape), 0,255, cv2.NORM_MINMAX))
cv2.imwrite('bit plane4.jpg',cv2.normalize(five_bit_img, np.zeros(img.shape), 0,255, cv2.NORM_MINMAX))
cv2.imwrite('bit plane3.jpg',cv2.normalize(four_bit_img, np.zeros(img.shape), 0,255, cv2.NORM_MINMAX))
cv2.imwrite('bit plane2.jpg',cv2.normalize(three_bit_img, np.zeros(img.shape), 0,255, cv2.NORM_MINMAX))
cv2.imwrite('bit plane1.jpg',cv2.normalize(two_bit_img, np.zeros(img.shape), 0,255, cv2.NORM_MINMAX))
cv2.imwrite('bit plane0.jpg',cv2.normalize(one_bit_img, np.zeros(img.shape), 0,255, cv2.NORM_MINMAX))

cv2.waitKey(0)