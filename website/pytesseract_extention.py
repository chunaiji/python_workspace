import pytesseract
from PIL import Image

class pytesseract_extention:

    def __init__(self, path):
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 请根据实际安装位置修改
        pytesseract.pytesseract.tesseract_cmd = path  # 请根据实际安装位置修改
 
    def image_to_string(self,image_path,lang='eng'):
        # 打开图片
        image = Image.open(image_path)
        # OCR识别
        text = pytesseract.image_to_string(image, lang)
        return text