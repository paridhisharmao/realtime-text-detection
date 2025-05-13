import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    text = pytesseract.image_to_string(gray, lang='eng')

    text = text.replace('\n', ' ').replace('\r', ' ').replace('\x0c', ' ')
    text = re.sub(r'[^a-zA-Z0-9.,:;!?()\'" ]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    print("Cleaned Text:", text)

    cv2.putText(gray, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 150, 0), 2, cv2.LINE_AA)
    cv2.imshow("Webcam OCR", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
