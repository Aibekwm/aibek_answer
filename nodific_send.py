# в данный момент я использовал программу Tesseract OCR tesseract-ocr-w64-setup-5.3.3.20231005.exe ссылка на Windows
# что бы он работал в питоне надо написать этот команду в терминале pip install pytesseract
# что бы работать с img устоновил эту библиотеку pip install pillow
import pytesseract
from PIL import Image
with Image.open('podpis.jpg') as image:
    podpis = pytesseract.image_to_string(image)
    print(podpis)