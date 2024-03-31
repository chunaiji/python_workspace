from flask import Flask
from pytesseract_extention import pytesseract_extention
from pdf_convert_extention import pdf_convert_extenton
 
app = Flask(__name__)

tesseract_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract_extention = pytesseract_extention(tesseract_path)
pdf_convert_extention = pdf_convert_extenton("")

@app.route('/')
def hello_world():
    string=pytesseract_extention.image_to_string("E:\QQ图片20180326094950.jpg")
    return 'Hello, World!'+ " " +string

@app.route('/convert')
def hello_world1():
    pdf_convert_extenton.pdf_convert_docx(r"D:\免费知网使用流程.pdf",r"D:\免费知网使用流程.docx",0,2)
    #pdf_convert_extenton.convert_to_pdf(r"D:\免费知网使用流程.docx",r"D:\免费知网使用流程.pdf")
    return 'Hello, World!'
 
if __name__ == '__main__':
    app.run(debug=True)