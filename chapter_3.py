import cv2
import numpy as np

img = cv2.imread (r"C:\Users\HP\PycharmProjects\opencv_python\Screenshot (32).png")
print(img.shape)

imgResize = cv2.resize(img,(2000,3000))
imgCropped = img[0:500,500:800]

# cv2.imshow("resized image",imgResize)
cv2.imshow("cropped image",imgCropped)


cv2.waitKey(0)