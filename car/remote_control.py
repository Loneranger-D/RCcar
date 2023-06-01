import pygame
import car_move


############################
####初始化云台


import Steering_Module 
import time
steer=Steering_Module.Steering(14,0,160,15,60,160,80,110) #初始位置为36和160，此时云台是正对前方，通过调试得到这两个值
steer.setup()
#time.sleep(2)




############################






# 定义一些寒色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# 这是一个简单的类，将帮助我们打印到屏幕上。它与操纵杆无关，只是输出信息。
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# 设置屏幕得到宽度和长度 [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# 保持循环直到用户点击关闭按钮
done = False

# 被用来管理屏幕更新的速度
clock = pygame.time.Clock()

# 初始化joystick
pygame.joystick.init()

# 准备好打印
textPrint = TextPrint()

# -------- 程序主循环 -----------
while done == False:
    # 事件处理的步骤
    for event in pygame.event.get():  # 用户要做的事情（键盘事件...）
        if event.type == pygame.QUIT:  # 如果用户触发了关闭事件
            done = True  # 设置我们做了这件事的标志，所以我们就可以退出循环了

        #   可能的joystick行为: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    # 绘制的步骤
    # 首先，用白色清除屏幕。不要放其它的绘图指令
    # 在这条上面的指令，将会被擦除
    screen.fill(WHITE)
    textPrint.reset()

    # 得到joystick的数量
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # 在每个joystick中：
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        textPrint.print(screen, "Joystick {}".format(i))
        textPrint.indent()

        # 从操作系统中获取控制器/joystick的名称
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name))

        # 通常轴成对运行，一个轴向上/向下，另一个轴向左/右。
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes))
        textPrint.indent()
        
        #####
        car = car_move.Car()
        # lastact用于判定每帧输出指令是否与上一帧相同
        lastact = 10
        # actstop用于判定无输出时令小车静止不动
        actstop0 = 1
        actstop1 = 1
        
        #####
        
        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis))
            
            ####下面开始操作
            servo_y = 0
            servo_x = 0
            
            # i 为0时控制左右方向移动
            if i == 0 :
                if axis >= 0.2 and lastact != 0:
                    car.rightFront()
                    lastact=0
                    #time.sleep(0.01)
                    pass
                elif axis <= -0.2 and lastact != 1:
                    car.leftFront()
                    lastact=1
                    #time.sleep(0.01)
                    pass
                else :
                    actstop0 = 0
                
            # i 为1时控制前后方向移动
            elif i == 1 :
                if axis >= 0.2 and lastact != 3:
                    car.rear()
                    lastact=3
                    #time.sleep(0.01)
                    pass
                elif axis <= -0.5 and lastact != 4 :
                    car.front()
                    lastact=4
                    #time.sleep(0.01)
                    pass
                else :
                    actstop1 = 0
                    
            
            
            
            
            elif i == 3 :
                if axis >= 0.2 :
                    servo_x = 1
                    
                    pass
                elif axis <= -0.2 :
                    servo_x = -1
                    pass
                
                
                pass
            elif i == 4 :
                if axis >= 0.2 :
                    servo_y = -1
                    
                    pass
                elif axis <= -0.2 :
                    servo_y = 1
                    pass
                pass
            # 云台双向控制
            if servo_y == 1 and servo_x == 1 :
                for i in range(0,100):
                    steer.Up()
                    steer.Right()
                    pass
            if servo_y == 1 and servo_x == -1 :
                for i in range(0,100):
                    steer.Up()
                    steer.Left()
                    
                pass
            if servo_y == -1 and servo_x == 1 :
                for i in range(0,100):
                    steer.Down()
                    steer.Right()
                pass
            if servo_y == -1 and servo_x == -1 :
                for i in range(0,100):
                    steer.Down()
                    steer.Left()
                pass
            if servo_y == 1 and servo_x == 0 :
                for i in range(0,100):
                    steer.Up()
                pass
            if servo_y == -1 and servo_x == 0 :
                for i in range(0,100):
                    steer.Down()
                pass
            if servo_y == 0 and servo_x == 1 :
                for i in range(0,100):
                    steer.Right()
                pass
            if servo_y == 0 and servo_x == -1 :
                for i in range(0,100):
                    steer.Left()
                pass
            
            if actstop0 == 0 and actstop1 == 0 :
                car.setup()










        textPrint.unindent()

        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.print(screen, "Button {:>2} value: {}".format(i, button))
            
            
            ###########
            if i == 10 :
                if button == 1:
                    steer.specify(80,110)
            
            
        textPrint.unindent()

        # 帽子开关。完全或完全没有方向，不像操纵杆。
        # 值在数组中返回
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats))
        textPrint.indent()

        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()

        textPrint.unindent()

    # 所有绘图的指令必须在这一条前面

    # 向前运行，并更新屏幕
    pygame.display.flip()

    # 限制每秒20帧
    clock.tick(20)

# 关闭窗口并退出.
# 如果你忘记这行，程序会被挂起，如果它从IDLE中运行的话
# （通常在IDLE中运行，需要两条退出语句）
# pygame.quit()
# sys.exit()
pygame.quit()
