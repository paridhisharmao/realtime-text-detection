import cv2

cap = cv2.VideoCapture(r"C:\Users\HP\OneDrive\Pictures\Camera Roll\WIN_20250508_19_37_13_Pro.mp4")

while True:
    success, img =cap.read()
    cv2.imshow("video".img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
