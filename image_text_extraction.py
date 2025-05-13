import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ensure this is correct


# Load image and preprocess
img = cv2.imread(r"C:\Users\HP\PycharmProjects\opencv_python\The_river_effect_in_justified_text.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OCR (text recognition)
text = pytesseract.image_to_string(gray)

print("Detected Text:", text)