import pyttsx3

engine = pyttsx3.init()
class pyttsx3_extention:
    def __init__(self, path):
        self.path=path
        # 初始化tts引擎
        # engine = pyttsx3.init()

        # 设置语速
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 1)

        # 设置音量
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume - 0.75)
        # 设置发音人
        # voices = engine.getProperty('voices')
        # engine.setProperty('voice', voices[0].id)
    
    def convert_void(self,text,out_path='test.mp3'):
        #  self.engine.say(text)
        try:
            engine.say(text)
            # engine.save_to_file(text, out_path)
            engine.runAndWait()
        except Exception as e:
            return False

    def destroy(self):
        self.engine.stop()
    
    # # 要转换成语音的文本
    # text = "Hello, this is a text to speech example."
    
    # # 清除之前的tts设置
    # engine.say(text)
    
    # # 生成语音
    # engine.runAndWait()
    
    # 关闭tts引擎
    # engine.stop()