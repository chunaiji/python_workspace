from turtle import width
from PIL import Image
from rembg import new_session, remove

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

    def remove_background(self,image_path,out_path):
        image = image_extention.remove_background_core(image_path)

        with open(out_path,"wb") as out_file:
            out_file.write(image)

        with Image.open(out_path) as image_file:
            out_image= image_extention.fix_black_border(image_file)
            out_image.save(out_path)

    def convert_image(input_path, output_path,suffix='PNG'):
        with Image.open(input_path) as img:
            img.convert('RGB').save(output_path, suffix)

        # 使用函数转换图片
        # convert_image('input.jpg', 'output.png')


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
 
# # 调用函数进行测试
# result = remove_background("input.jpg")
# print(result)