import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"E:\Softwares\Tessaract for DecodeLabs\tesseract.exe"

image_path = "sample_image.png"

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)[1]

cv2.imwrite("processed.png", gray)

text = pytesseract.image_to_string(Image.open("processed.png"))

print("\nRecognized Text:\n")
print(text)