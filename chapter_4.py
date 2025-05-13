import cv2
import numpy as np

img = np.zeros((450,450,3), np.uint8)
# print(img)
# img[:]=0,0,0

cv2.line(img,(0,0),(400,400),(0,150,150),4)
cv2.rectangle(img,(20,20),(70,70),(150,0,150),2)
cv2.rectangle(img,(75,75),(125,125),(150,0,150),2)
cv2.rectangle(img,(130,130),(180,180),(150,0,150),2)
cv2.rectangle(img,(185,185),(235,235),(150,0,150),2)
cv2.rectangle(img,(240,240),(290,290),(150,0,150),2)
cv2.rectangle(img,(295,295),(345,345),(150,0,150),2)
cv2.rectangle(img,(350,350),(400,400),(150,0,150),2)
cv2.circle(img,(27,27),7,(250,150,0),2)
cv2.circle(img,(63,63),7,(250,150,0),2)
cv2.circle(img,(82,82),7,(250,150,0),2)
cv2.circle(img,(118,118),7,(250,150,0),2)
cv2.circle(img,(137,137),7,(250,150,0),2)
cv2.circle(img,(173,173),7,(250,150,0),2)
cv2.putText(img,"paridhi",(300,45),cv2.FONT_HERSHEY_PLAIN,2,(150,0,150),1)
cv2.imshow("image",img)
cv2.waitKey(0)

