from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from os.path import abspath, dirname
from flask_cors import CORS
import datetime

from pytesseract_extention import pytesseract_extention
from pdf_convert_extention import pdf_convert_extenton
from os_extention import os_extention
from psutil_extention import psutil_extention
from image_extention import image_extention
from pyttsx3_extention import pyttsx3_extention
from image_extention_component import image_extention_component

app = Flask(__name__)
CORS(app)

tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract_extention = pytesseract_extention(tesseract_path)
pdf_convert_extention = pdf_convert_extenton("")
pyttsx3_extention = pyttsx3_extention("")
image_extention = image_extention("")


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
    # image_extention.remove_pixels(r"D:\python_demo\1c4ca.jpg", 200, r"D:\python_demo\1c4ca333.png")  不满意
    # image_extention.add_mark(r"D:\python_demo\1c4ca.jpg",r"D:\python_demo\qq","hello word hhyu")
    # image_extention.replace_background(r"D:\3eccb.jpg")
    # image_extention.convert_cartoon(r"D:\python_demo\1c4ca.jpg",r"D:\python_demo\1c4ca.png") 不满意
    # image_extention.contrast(r"D:\python_demo\1c4ca.jpg",r"D:\python_demo\1c4ca.png")
    # image_extention.cartoon_effect(r"D:\python_demo\1c4ca.jpg",r"D:\python_demo\1c4ca.png")
    # image_extention.filter(r"D:\python_demo\1c4ca.jpg",r"D:\python_demo\1c4ca.png")
    # image_extention.contrast(r"D:\python_demo\1c4ca.jpg",r"D:\python_demo\qq1c4ca.png")
    # image_extention.replace_background(r"D:\python_demo\1c344ca.png",r"D:\python_demo\replace.png", color=(255, 255, 255))
    image_extention.compound(r"D:\python_demo\33333.jpg",
                             r"D:\python_demo\1c4ca.jpg", r"D:\python_demo\reployyyace.png")

    return 'Hello, World!'


@app.route('/image/init')
def init_image():
    file = request.args.get('file')
    file_path = os.path.join(dirname(abspath(__file__)), file)
    paths = image_extention_component.component(file_path)
    return jsonify({'code': 200,  'data': paths})


@app.route('/image/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'code': -1,  'data': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'code': -1,  'data': 'No selected file'})

    if file:
        filename = secure_filename(file.filename)
        current_date = datetime.date.today()
        dir_path = dirname(abspath(__file__)) + \
            str("\\path\\upload\\")+str(current_date)+str("\\")

        os_extention.check(dir_path)
        file_path = os.path.join(dir_path, str(filename))
        out_put=str(current_date)+str("\\")+str(filename)
        file.save(file_path)
        return jsonify({'code': 200,  'data': out_put,'message':'File uploaded successfully'})


if __name__ == '__main__':
    app.run(debug=True)
