import numbers
import string
from pdf2docx import Converter
import os
import win32com.client as win32
from docx import Document
 
class pdf_convert_extenton:

    def __init__(self, path):
        self.path=path

    def pdf_convert_docx( pdf_path:string, docx_path:string, start:numbers=0, end:numbers=1):
        cv = Converter(pdf_path)# PDF文件路径
        # 转换第一页
        cv.convert(docx_path, start, end) # 输出的Word文档路径
        # 释放资源
        cv.close()

    def convert_to_pdf(input_path, output_path):
        # 创建Word应用程序实例
        word_app = win32.gencache.EnsureDispatch('Word.Application')
        # 设置应用程序可见性为False（不显示Word界面）
        word_app.Visible = False
    
        try:
            # 打开Word文档
            doc = word_app.Documents.Open(input_path)
            # 保存为PDF
            doc.SaveAs(output_path, FileFormat=17)
            doc.Close()
            return True
        except Exception as e:
            print("转换失败：" + str(e))
            return False
        finally:
            # 关闭Word应用程序
            word_app.Quit()
            
        # 输入和输出文件路径
        # input_file = "C:\\mydocs\\光项目商务\\验收报告2020.docx"
        # output_file = "C:\\mydocs\\光项目商务\\验收报告2020.pdf"
        
        # # 调用函数进行转换
        # success = convert_to_pdf(input_file, output_file)
        # if success:
        #     print("转换成功！")
        # else:
        #     print("转换失败！")
