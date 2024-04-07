from turtle import width
from PIL import Image
from rembg import new_session, remove
from tqdm import tqdm
from watermarker.marker import add_mark

# 需要下载训练模型  阿里网盘/安装包/u2net 解压到-> C:\Users\XXX\.u2net
class image_extention:

    def __init__(self, path):
        self.path=path

    def remove_background1(image_path,output_path):
        input=Image.open(image_path)
        output=remove(input)
        output.save(output_path)
        return output_path

    def remove_background_core(image_path):
        model = 'u2net_human_seg' # 指定模型类型
        with open(image_path,"rb") as image_file:
            image_data= image_file.read()
            result= remove(image_data,session=new_session(model))
            return result
    # https://blog.51cto.com/u_16175447/8698505
    # https://juejin.cn/post/7250291603814694970
    def fix_black_border(image):
        width ,height=image.size
        pixels=image.load()
        for x in range(width):
            for y in range(height):
                r,g,b,a=pixels[x,y]
                if a==0:
                    pixels[x,y]=(255,255,255,0)
        return image

    # 去除图片背景
    def remove_background(self,image_path,out_path):
        image = image_extention.remove_background_core(image_path)

        with open(out_path,"wb") as out_file:
            out_file.write(image)

        with Image.open(out_path) as image_file:
            out_image= image_extention.fix_black_border(image_file)
            out_image.save(out_path)

    # 转为灰度
    def covert_gray(input_path, output_path):
        # 打开图片
        image = Image.open(input_path)
        
        # 转换为灰度图
        gray_image = image.convert('L')
        
        # 保存灰度图
        gray_image.save(output_path)

    # gif 提取图片
    def get_image_from_gif(input_path):
        #读入一个GIF文件
        im = Image.open(input_path)
        try:
            im.save('picframe{:02d).png'.format(im.tell()))
            while True:
                im.seek(im.tel1 ()+1)
                im.save('picframe{:02d).png'.format(im.tell()))
        except:
            print("处理结束")

    # 图片转换
    def convert_image(input_path, output_path,suffix='PNG'):
        with Image.open(input_path) as img:
            img.convert('RGB').save(output_path, suffix)

        # 使用函数转换图片
        # convert_image('input.jpg', 'output.png')

    # 替换图片背景
    def replace_background(image_path, color=(255, 255, 255)):
        # 加载图片
        img = Image.open(image_path)
        
        # 将图片转换为RGBA，以便处理透明度
        img = img.convert("RGBA")
        
        # 分离通道
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # 如果该像素是完全透明的，则保留完全透明
            if item[0] == 0:
                newData.append((0, 0, 0, 0))
            else:
                # 如果不是完全透明的，则替换背景色
                newData.append((color[0], color[1], color[2], item[3]))
        
        # 更新图片数据
        img.putdata(newData)
        img.save(r"D:\wewew.png")
        return img

    # 合并图片
    def compound(image_path1,image_path2,out_path):
        # 打开第一张图片
        img1 = Image.open(image_path1)
        # 打开第二张图片
        img2 = Image.open(image_path2)
        # 确保两张图片大小相同，如果不同，需要先调整大小
        img2 = img2.resize(img1.size)
        # 将两张图片合成
        img1.paste(img2, mask=img2)
        # 保存合成的图片
        img1.save(out_path)

    # 去除水印 https://blog.csdn.net/weixin_53170155/article/details/136093323
    def remove_pixels(self,img_path, rgb_sum_threshold, dest_path):
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
    def add_mark(self,image_path,out_path,mark,opacity=0.2,angle=30,space=30):
        add_mark(file = image_path, out = out_path,mark = mark, opacity=opacity, angle=angle, space=space)
 
# # 调用函数进行测试
# result = remove_background("input.jpg")
# print(result)