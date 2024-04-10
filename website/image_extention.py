from turtle import width
from PIL import Image, ImageFilter, ImageEnhance
from rembg import new_session, remove
from tqdm import tqdm
from watermarker.marker import add_mark
import cv2
import numpy as np
from skimage import data_dir, io, transform, color

# 需要下载训练模型  阿里网盘/安装包/u2net 解压到-> C:\Users\XXX\.u2net
# https://blog.csdn.net/starvapour/article/details/108214478 python图片处理常用操作笔记


class image_extention:

    def __init__(self, path):
        self.path = path

    def remove_background1(image_path, output_path):
        input = Image.open(image_path)
        output = remove(input)
        output.save(output_path)
        return output_path

    def remove_background_core(image_path):
        model = 'u2net_human_seg'  # 指定模型类型
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            result = remove(image_data, session=new_session(model))
            return result
    # https://blog.51cto.com/u_16175447/8698505
    # https://juejin.cn/post/7250291603814694970

    def fix_black_border(image):
        width, height = image.size
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]
                if a == 0:
                    pixels[x, y] = (255, 255, 255, 0)
        return image

    # 去除图片背景
    def remove_background(self, image_path, out_path):
        image = image_extention.remove_background_core(image_path)

        with open(out_path, "wb") as out_file:
            out_file.write(image)

        with Image.open(out_path) as image_file:
            out_image = image_extention.fix_black_border(image_file)
            out_image.save(out_path)

    # 转为灰度
    def convert_gray(input_path, output_path):
        # 打开图片
        image = Image.open(input_path)

        # 转换为灰度图
        gray_image = image.convert('L')

        # 保存灰度图
        gray_image.save(output_path)

    def convert_gray_core(self, f, width=256, height=256):
        rgb = io.imread(f)  # 依次读取rgb图片
        gray = color.rgb2gray(rgb)  # 将rgb图片转换成灰度图
        dst = transform.resize(gray, (width, height))  # 将灰度图片大小转换为256*256
        return dst

    # 批量置灰 https://www.osgeo.cn/python-tutorial/skibasic-batch.html
    def convert_gray_dir():
        str = '*.png'  # str=data_dir+'/*.jpg:'+data_dir+'/*.png'
        # 集合处理函数ImageCollection
        coll = io.ImageCollection(
            str, load_func=image_extention.convert_gray_core)
        for i in range(len(coll)):
            io.imsave('xx_' + np.str(i)+'.jpg', coll[i])  # 循环保存图片

    # 压缩图片 调整图片大小
    def thumbnail(input_path, output_path, width=100, height=100):
        # 打开图片
        image = Image.open(input_path)
        image.thumbnail((width, height))  # 将图像缩放至 100x100
        image.save(output_path)

    # 压缩图片 调整图片质量
    def compress(input_path, output_path, quality=20):
        img = Image.open(input_path)
        img.save(output_path, quality)

    # 裁剪
    def compress(input_path, output_path, left=100, upper=100, right=400, lower=400):
        img = Image.open(input_path)
        # 裁剪出一个矩形区域 (left, upper, right, lower)
        cropped_img = img.crop((left, upper, right, lower))
        cropped_img.save(output_path)

    # gif 提取图片 https://baijiahao.baidu.com/s?id=1773831462594773582&wfr=spider&for=pc
    def get_image_from_gif(input_path):
        # 读入一个GIF文件
        im = Image.open(input_path)
        try:
            im.save('picframe{:02d).png'.format(im.tell()))
            while True:
                im.seek(im.tel1()+1)
                im.save('picframe{:02d).png'.format(im.tell()))
        except:
            print("处理结束")

    # 颜色交换
    def exchange(self, input_path, output_path):
        im = Image.open(input_path)
        r, g, b = im.split()
        newg = g.point(lambda i: i * 0.9)  # 将G通道颜色值变为原来的0.9倍
        newb = b.point(lambda i: i < 100)  # 选择B通道值低于100的像素点
        om = Image.merge(im.mode, (r, newg, newb))  # 将3个通道合形成新图像
        # om = Image.merge("RGB", (b, g, r))
        om.save(output_path)

    # 图片分割
    def split(self, input_path, row=2, col=3):
        img = Image.open(input_path)
        # 按矩形分割图像 (2行, 3列)
        rows, cols = img.size[0] // row, img.size[1] // col
        tiles = img.split((rows, cols))
        for i, tile in enumerate(tiles):
            tile.save(f'tile_{i}_{tile.mode}.jpg')

    # 图片增强 https://blog.csdn.net/JBY2020/article/details/125358387 修改亮度没实现
    def contrast(self, input_path, output_path, enhance_num=2):
        img = Image.open(input_path)
        # img_color = ImageEnhance.Color(img)
        # img_brightness = ImageEnhance.Brightness(img)
        om = ImageEnhance.Contrast(img)
        om.enhance(enhance_num).save(output_path)

    # 调整亮度
    def brightness(self, input_path, output_path, enhance_num=1.5):
        img = Image.open(input_path)
        # 调整亮度（增加50%）
        brighter_img = img.point(lambda p: p * enhance_num)
        brighter_img.save(output_path)

    #   轮廓获取 https://blog.csdn.net/JBY2020/article/details/125358387 ****
    #   BLUE：模糊
    #   CONTOUR：轮廓
    #   DETAIL：详情
    #   EDGE_ENHANCE：边缘增强
    #   EDGE_ENHANCE_MORE：边缘更多增强
    #   EMBOSS：浮雕
    #   FIND_EDGES：寻找边缘
    #   SHARPEN：锐化
    #   SMOOTH：平滑
    def filter(self, input_path, output_path, filter=ImageFilter.CONTOUR):
        im = Image.open(input_path)
        om = im.filter(filter)  # 高斯模糊
        om.save(output_path)

    # 图片转换
    def convert_image(self, input_path, output_path, suffix='PNG'):
        with Image.open(input_path) as img:
            img.convert('RGB').save(output_path, suffix)

        # 使用函数转换图片
        # convert_image('input.jpg', 'output.png')

    # 转为卡通
    def convert_cartoon(self, input_path, output_path):
        # 读取单通道黑白图片
        img = cv2.imread(input_path, 0)

        # 拉普拉斯滤波器
        kernal = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
        img = cv2.filter2D(img, -1, kernal)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        # 膨胀两次
        img = cv2.dilate(img, kernel, iterations=2)

        # 腐蚀两次
        img = cv2.erode(img, kernel, iterations=2)

        # 二值化
        ret, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)

        # 输出
        cv2.imwrite(output_path, img)

    # 卡通
    def cartoon_effect(self, input_path, output_path):
        # 读取图片
        image = Image.open(input_path)
        # 将图片转换为灰度图
        gray = image.convert('L')
        # 使用边缘检测来强化图片的轮廓
        edge_enhance = ImageEnhance.Contrast(gray)
        edge_enhanced = edge_enhance.enhance(2)
        # 二值化图片以创建卡通效果
        cartoon = edge_enhanced.convert('1')
        # 增加图片的灰度级别以增加卡通的颜色
        # color_quantized = cartoon.convert('P', palette=Image.ADAPTIVE, colors=16)
        color_quantized = cartoon.convert('P', colors=16)
        color_quantized.save(output_path)

        # 使用函数转换图片
        # cartoon_image = cartoon_effect('input.jpg')
        # cartoon_image.save('output.jpg')

    # 替换图片背景
    def replace_background(self, image_path, output_path, color=(255, 255, 255)):
        # 打开图片
        img = Image.open(image_path)
        # 获取图片的模式，如果是RGBA则说明有透明背景
        if img.mode == 'RGBA':
            # 创建一个白色背景
            background = Image.new('RGBA', img.size, color)
            # 将img与背景合并
            background.paste(img, mask=img.split()[3])
            # 保存新图片
            background.save(output_path)
        else:
            img.save(output_path)

    # 合并图片
    def compound(self, image_path1, image_path2, out_path, image1_alpha=128, image2_alpha=128):
        # 打开第一个图形
        image1 = Image.open(image_path1)
        image1 = image1.convert("RGBA")
        image1_with_alpha = image1.copy()
        # 调整透明度
        image1_with_alpha.putalpha(image1_alpha)

        # 打开第二个图形
        image2 = Image.open(image_path2)

        # 调整第二个图形的尺寸与第一个图形相同
        image2 = image2.resize(image1.size)

        image2 = image2.convert("RGBA")
        image2_with_alpha = image2.copy()
        # 调整透明度
        image2_with_alpha.putalpha(image2_alpha)

        # 创建一个新的图形对象，并将两个图形叠加在一起
        composite_image = Image.alpha_composite(
            image1_with_alpha, image2_with_alpha)

        # 保存叠加后的图形
        composite_image.save(out_path)

    # 去除水印 https://blog.csdn.net/weixin_53170155/article/details/136093323
    def remove_pixels(self, img_path, rgb_sum_threshold, dest_path):
        def is_high_brightness(rgb):
            return sum(rgb) >= rgb_sum_threshold

        with Image.open(img_path) as img:
            width, height = img.size
            for x in tqdm(range(width), desc="Processing Columns"):
                for y in range(height):
                    if is_high_brightness(img.getpixel((x, y))[:3]):
                        img.putpixel((x, y), (255, 255, 255))

        img.save(dest_path)

    # 添加水印 color、size、opacity、space、angle：水印文字的样式包括文字的大小、颜色、透明程度等等
    def add_mark(self, image_path, out_path, mark, opacity=0.2, angle=30, space=30):
        add_mark(file=image_path, out=out_path, mark=mark,
                 opacity=opacity, angle=angle, space=space)

# # 调用函数进行测试
# result = remove_background("input.jpg")
# print(result)
