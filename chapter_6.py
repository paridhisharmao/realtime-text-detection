import cv2
import numpy as np

img = cv2.imread(r"C:\Users\HP\PycharmProjects\opencv_python\images_to_text.jpeg")
imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
pink_overlay = np.full_like(img, (203, 192, 255))  # BGR for pink

# Blend the original image and pink overlay
pink_filtered = cv2.addWeighted(img, 1, pink_overlay, 0.2, 0)
imgHor1 = np.hstack((img,img,pink_filtered))
imgHor2 = np.hstack((img,imgGray,img))
imgVer = np.vstack((imgHor1,imgHor2))


cv2.imshow("vertical",imgVer)


cv2.waitKey(0)