import cv2
def empty(a):
    pass
path = (r"C:\Users\HP\PycharmProjects\opencv_python\images.color.jpeg")
img = cv2.imread(path)

cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars", 640,240)
cv2.createTrackbar("Hue_min","trackbars",0,179,empty)
cv2.createTrackbar("Hue_max","trackbars",179,179,empty)
cv2.createTrackbar("sat_min","trackbars",0,255,empty)
cv2.createTrackbar("sat_max","trackbars",255,255,empty)
cv2.createTrackbar("val_min","trackbars",0,255,empty)
cv2.createTrackbar("val_max","trackbars",255,255,empty)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

h_min=

cv2.imshow("orignal",img)
cv2.imshow("HSV",imgHSV)
cv2.waitKey(0)