import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\HP\PycharmProjects\opencv_python\images333.jpeg")

# Manually enter 4 points from the image (Top-Left, Top-Right, Bottom-Right, Bottom-Left)
pts1 = np.float32([[ 100, 150], [400, 130], [420, 550], [120, 570]])

# Output rectangle size (width, height)
width, height = 300, 500
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Perspective transform
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (width, height))

# Show result
cv2.imshow("Warped", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
