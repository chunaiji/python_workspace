from pdf2docx import Converter
from docx2pdf import convert
import pythoncom
import win32com.client as win32
from docx import Document
 
class pdf_convert_extenton:

    def __init__(self, path):
        self.path=path

    # input_path = "C:\\mydocs\\光项目商务\\验收报告2020.docx"
    # output_path = "C:\\mydocs\\光项目商务\\验收报告2020.pdf"
    def pdf_convert_docx(input_path, output_path, start, end):
        try:
            cv = Converter(input_path)# PDF文件路径
            # 转换第一页
            cv.convert(output_path, start, end) # 输出的Word文档路径
            return True
        except Exception as e:
            print("转换失败：" + str(e))
            return False
        finally:
            # 释放资源
            cv.close()
        

    # input_path = "C:\\mydocs\\光项目商务\\验收报告2020.docx"
    # output_path = "C:\\mydocs\\光项目商务\\验收报告2020.pdf"
    def convert_to_pdf(input_path, output_path):
        try:
            pythoncom.CoInitialize()
            convert(input_path,output_path)
            return True
        except Exception as e:
            print("转换失败：" + str(e))
            return False
        finally:
            # 关闭Word应用程序
            pythoncom.CoUninitialize()
            
        # 输入和输出文件路径
        # input_file = "C:\\mydocs\\光项目商务\\验收报告2020.docx"
        # output_file = "C:\\mydocs\\光项目商务\\验收报告2020.pdf"
        
        # # 调用函数进行转换
        # success = convert_to_pdf(input_file, output_file)
        # if success:
        #     print("转换成功！")
        # else:
        #     print("转换失败！")
