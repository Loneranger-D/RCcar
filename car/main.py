import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
IN1_PIN1 = 19
IN2_PIN1 = 16
IN1_PIN2 = 26
IN2_PIN2 = 20
GPIO.setup(IN1_PIN1, GPIO.OUT)
p1 = GPIO.PWM(IN1_PIN1, 50)  # 这里的50是频率为50Hz
p1.start(0)
GPIO.setup(IN2_PIN1, GPIO.OUT)
p2 = GPIO.PWM(IN2_PIN1, 50)
p2.start(0)
GPIO.setup(IN1_PIN2, GPIO.OUT)
p3 = GPIO.PWM(IN1_PIN2, 50)
p3.start(0)
GPIO.setup(IN2_PIN2, GPIO.OUT)
p4 = GPIO.PWM(IN2_PIN2, 50)
p4.start(0)
# 可以通过更改括号内的数值改变电机转动的速度，数值范围0~100
def forward(time_sleep):
    p1.start(50)
    p2.start(0)
    p3.start(50)
    p4.start(0)
    time.sleep(time_sleep)
def reverse(time_sleep):
    p1.start(0)
    p2.start(50)
    p3.start(0)
    p4.start(50)
    time.sleep(time_sleep)
def left(time_sleep):
    p1.start(50)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    time.sleep(time_sleep)
def right(time_sleep):
    p1.start(0)
    p2.start(0)
    p3.start(50)
    p4.start(0)
    time.sleep(time_sleep)
def left_0(time_sleep):
    p1.start(50)
    p2.start(0)
    p3.start(0)
    p4.start(50)
    time.sleep(time_sleep)
def right_0(time_sleep):
    p1.start(0)
    p2.start(50)
    p3.start(50)
    p4.start(0)
    time.sleep(time_sleep)
def stop(time_sleep):
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    time.sleep(time_sleep)
while True:
    cmd = str(input("按以下键后回车（w，前进;x，后退;s，停止）:"))
    direction = cmd
    if direction == "w" or "s" or "a" or "d" or "q" or "e":
        if direction == "w":  # 前进
            forward(1)
            stop(0.1)
        elif direction == "s":  # 后退
            reverse(1)
            stop(0.1)
        elif direction == "a":  # 单轮左转
            left(1)
            stop(0.1)
        elif direction == "d":  # 单轮右转
            right(1)
            stop(0.1)
        elif direction == "q":  # 双轮左转
            left_0(1)
            stop(0.1)
        elif direction == "e":  # 双轮右转
            right_0(1)
            stop(0.1)
        elif direction == "x":  # 停止移动
            stop(0.1)
        else:
            print("命令无法识别")
            break