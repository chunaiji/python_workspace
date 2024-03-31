from flask import Flask
from pytesseract_extention import pytesseract_extention
 
app = Flask(__name__)

tesseract_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract_extention = pytesseract_extention(tesseract_path)

@app.route('/')
def hello_world():
    string=pytesseract_extention.image_to_string("E:\QQ图片20180326094950.jpg")
    return 'Hello, World!'+ " " +string
 
if __name__ == '__main__':
    app.run(debug=True)