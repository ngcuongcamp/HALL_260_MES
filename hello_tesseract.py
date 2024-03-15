import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"./libs/Tesseract-OCR/tesseract.exe"

# image = cv2.imread(r"./tesseract_test\anh\2.png")
# height, width = image.shape[:2]
# gray = cv2.resize(image, (width * 3, height * 3))
# gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
# threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# # processed = cv2.medianBlur(gray, 3)
# cv2.imshow("image", gray)
# cv2.waitKey(0)
# text = pytesseract.image_to_string(gray)
# print(text)


image = cv2.imread(r"./tesseract_test\anh\2.png")
height, width = image.shape[:2]

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (width * 3, height * 3))
blur = cv2.GaussianBlur(gray, (3, 3), 0)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# imgTH = cv2.morphologyEx(blur, cv2.MORPH_TOPHAT, kernel)
threshold_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

cv2.imshow("origin", blur)
cv2.imshow("processed", threshold_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Nhận dạng văn bản từ ảnh
text = pytesseract.image_to_string(gray)
print(text)
