from flask import Flask, request
from werkzeug.utils import secure_filename
import os
from os.path import abspath, dirname

from pytesseract_extention import pytesseract_extention
from pdf_convert_extention import pdf_convert_extenton
from os_extention import os_extention
from psutil_extention import psutil_extention
from image_extention import image_extention
from pyttsx3_extention import pyttsx3_extention
 
app = Flask(__name__)

tesseract_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract_extention = pytesseract_extention(tesseract_path)
pdf_convert_extention = pdf_convert_extenton("")
pyttsx3_extention =pyttsx3_extention("")
image_extention=image_extention("")

@app.route('/')
def hello_world():
    # string=pytesseract_extention.image_to_string("E:\QQ图片20180326094950.jpg")
    # psutil_extention.showComputerInfo()
    # pyttsx3_extention.convert_void("Hello, World",r"D:\\aaa.mp3");
    
    return 'Hello, World!'

@app.route('/convert')
def hello_world1():
    # pdf_convert_extenton.pdf_convert_docx(r"D:\免费知网使用流程.pdf",r"D:\免费知网使用流程.docx",0,2)
    # pdf_convert_extenton.convert_to_pdf(r"D:\免费知网使用流程.pdf",r"D:\免费知网使用流程.docx")
    # pdf_convert_extenton.convert_to_pdf(r"D:\免费知网使用流程.docx",r"D:\免费知网使用流程.pdf")
    # image_extention.remove_background(r"D:\python_demo\1c4ca.jpg",r"D:\python_demo\1c4ca.png") 
    image_extention.remove_pixels(r"D:\python_demo\1c4ca.jpg", 200, r"D:\python_demo\1c4ca333.png")
    # image_extention.add_mark(r"D:\python_demo\1c4ca.jpg",r"D:\python_demo\qq","hello word hhyu")
    # image_extention.replace_background(r"D:\3eccb.jpg") 
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