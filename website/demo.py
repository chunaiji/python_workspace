class MyClass:
    """一个简单的Python类示例"""
 
    def __init__(self, value):
        """类的初始化方法
 
        参数:
        - value: 初始化设置的值
        """
        self.my_attribute = value
 
    def get_value(self):
        """获取属性的方法
 
        返回:
        - self.my_attribute的值
        """
        return self.my_attribute
 
    def set_value(self, value):
        """设置属性的方法
 
        参数:
        - value: 要设置的新值
        """
        self.my_attribute = value
 
# 使用类的示例
# my_instance = MyClass(10)
# print(my_instance.get_value())  # 输出: 10
# my_instance.set_value(20)
# print(my_instance.get_value())  # 输出: 20