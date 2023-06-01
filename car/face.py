from aip import AipFace
from picamera import PiCamera
import urllib.request
import RPi.GPIO as GPIO
import base64
import time
import cv2 as cv

import car_move
car = car_move.Car()


from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
def printf(words):
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial)

    with canvas(device) as draw:
        
        #draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((20, 30), str(words), fill="white")
        
def printf2(words1,words2):
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial)

    with canvas(device) as draw:
        
        #draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((20, 20), str(words1), fill="white")
        draw.text((20, 40), str(words2), fill="white")
        
#百度人脸识别API账号信息
APP_ID = '20427201'
API_KEY = 'V8TPVN8tSDS1q3Hcfay7Dm6s'
SECRET_KEY ='bsKWOCnAPv70AGz0vmT3rmON73vmAkew'


client = AipFace(APP_ID, API_KEY, SECRET_KEY)#创建一个客户端用以访问百度云
#图像编码方式
IMAGE_TYPE='BASE64'
camera = PiCamera()#定义一个摄像头对象
#用户组
GROUP = '01'
 
#照相函数
def getimage():
    camera.resolution = (1024,768)#摄像界面为1024*768
    camera.start_preview()#开始摄像
    time.sleep(1)
    camera.capture('faceimage.jpg')#拍照并保存
    time.sleep(1)
#对图片的格式进行转换
def transimage():
    f = open('faceimage.jpg','rb')
    img = base64.b64encode(f.read())
    return img
#上传到百度api进行人脸检测



def go_api(image):
    result = client.search(str(image, 'utf-8'), IMAGE_TYPE, GROUP);#在百度云人脸库中寻找有没有匹配的人脸
    
    if result['error_msg'] == 'SUCCESS':#如果成功了
        name = result['result']['user_list'][0]['user_id']#获取名字
        score = result['result']['user_list'][0]['score']#获取相似度
        curren_time = time.asctime(time.localtime(time.time()))#获取当前时间
        if score > 40:#如果相似度大于80
 
            str1 = str("Welcome ! " + str(name))
            printf(str1)
            time.sleep(1.5)
            printf2('sign up','successfully')
            time.sleep(1.5)
            printf('you can leave')
            
            
            
        else:
            
            
            printf2('sorry','I don`t know you')
            time.sleep(1.5)
            
            name = 'Unknow'
            img1 = cv.imread('faceimage.jpg')
            cv.imwrite('messigray'+str(curren_time)+'.jpg',img1)
            
            return 0
        
 
        #将人员出入的记录保存到Log.txt中
        f = open('Log.txt','a')
        f.write("Person: " + name + "     " + "Time:" + str(curren_time)+'\n')
        f.close()
        return 1

    #else:
        #print(str(result['error_code'])+' ' + str(result['error_code']))
        #return 0
#主函数
if __name__ == '__main__':
    #servo_init()    #舵机复位，初始化一次就够了
    while True:
        
        print('准备开始，请面向摄像头 ^_^')
        
        printf2('Hello','smell please~')
        res = -1

        # if True:
        #     getimage()#拍照
        #     img = transimage()  #转换照片格式
        #     res = go_api(img)   #将转换了格式的图片上传到百度云
        #     if(res == 1):   #是人脸库中的人
        #         #bt_open()
        #         print("欢迎回家，门已打开")
        #     elif(res == -1):
        #         print("我没有看见你,我要关门了")
        #         time.sleep(2)
        #         #bt_close()    
        #     else:
        #         print("关门")
        #         #bt_close()
        #     time.sleep(0.5)
        #     print('好了')
        #     time.sleep(2)
        #     car.leftFront()
        #     time.sleep(0.4)
        #     car.front()
        #     time.sleep(0.3)
            
            
        #     car.setup()
        #     time.sleep(4)            
            


