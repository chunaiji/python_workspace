from flask import Flask, request
from werkzeug.utils import secure_filename
import os
from os.path import abspath, dirname

from pytesseract_extention import pytesseract_extention
from pdf_convert_extention import pdf_convert_extenton
from os_extention import os_extention
from psutil_extention import psutil_extention
 
app = Flask(__name__)

tesseract_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract_extention = pytesseract_extention(tesseract_path)
pdf_convert_extention = pdf_convert_extenton("")

@app.route('/')
def hello_world():
    string=pytesseract_extention.image_to_string("E:\QQ图片20180326094950.jpg")
    psutil_extention.showComputerInfo()
    return 'Hello, World!'+ " " +string

@app.route('/convert')
def hello_world1():
    # pdf_convert_extenton.pdf_convert_docx(r"D:\免费知网使用流程.pdf",r"D:\免费知网使用流程.docx",0,2)
    pdf_convert_extenton.convert_to_pdf(r"D:\免费知网使用流程.pdf",r"D:\免费知网使用流程.docx")
    # pdf_convert_extenton.convert_to_pdf(r"D:\免费知网使用流程.docx",r"D:\免费知网使用流程.pdf")
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
 
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
 
    if file:
        filename = secure_filename(file.filename)
        # print(abspath(__file__))
        print(dirname(abspath(__file__)))
        dir_path=dirname(abspath(__file__))+str("\\path\\to\\upload1\\")
        os_extention.check(dir_path)
        file_path=dir_path+str(filename)
        print(file_path)
        file.save(file_path)
        return 'File uploaded successfully', 200
 
if __name__ == '__main__':
    app.run(debug=True)