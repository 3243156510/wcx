class Point:
    def __init__(self,row, col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(row=self.row, col=self.col)
#初始化框架
import pygame
import random
import time
#初始化窗口
pygame.init()
w = 800      #宽度
h = 600      #长度
#设置行和列
ROW = 30     #行
COL = 40     #列
#显示游戏窗口
size = (w,h)
screen = pygame.display.set_mode(size)    #跟显示相关
pygame.display.set_caption("王常枭的贪吃蛇")  #设置窗口标题   caption = 标题
bj_color = (255,255,255)         #bj_color = 背景颜色
ss_color = (200,200,200)         #ss_color = 蛇身颜色
head = Point(row = int(ROW/2),col = int(COL/2))   #head = 蛇头
head_color = (0,128,128)
sankes = [
    Point(row = head.row, col = head.col + 1),
    Point(row = head.row, col = head.col + 2),
    Point(row = head.row, col = head.col + 3),
]
#枭
bg = pygame.image.load("F:/0python文件/贪吃蛇/背景图片1.png")
screen.blit(bg, (0, 0))
pygame.display.update()
time.sleep(5)
#背景音乐
pygame.mixer.init()
pygame.mixer.music.load("F:/0python文件/音乐.mp3")
pygame.mixer.music.play(-1,0)

#生成食物
def gen_food():
    while 1:
        swzb = Point(row = random.randint(0,ROW - 1),col = random.randint(0,COL - 1))  #swzb = 食物坐标
        #是否跟蛇碰上了
        peng = False       #peng = 碰上
        if head.row == swzb.row and head.col == swzb.col:
            peng = True
        #蛇身子
        for sanke in sankes:
            if sanke.row == swzb.row and sanke.col == swzb.col:
                peng = True
                break
        if not peng:
            break
    return swzb
#定义坐标
food = gen_food()   #food = 食物
food_color = (255,255,0)
direct = "left"
def rect(point,color):
    cell_width = w/COL
    cell_height = h/ROW
    left = point.col*cell_width
    top = point.row*cell_height
    pygame.draw.rect(
        screen,color,
        (left,top,cell_width, cell_height))
#游戏的循环
a = True
clock = pygame.time.Clock()
while a:
    #处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        elif event.type == pygame.KEYDOWN:     #键盘操作
            if event.key == 119 or event.key == 273:
                if direct == "left" or direct == "right":
                    direct = "up"
            if event.key == 115 or event.key == 274:
                if direct == "left" or direct == "right":
                    direct = "down"
            if event.key == 97 or event.key == 276:
                if direct == "up" or direct == "down":
                    direct = "left"
            if event.key == 275 or event.key == 100:
                if direct == "up" or direct == "down":
                    direct = "right"
    #吃食物
    eat = False
    if head.row == food.row and head.col == food.col:
        eat = True
    #重新产生食物
    if eat:
        food = gen_food()
    #处理身子
    #1把原来的头，插入到snakes的头上
    sankes.insert(0,head.copy())
    #2把sankes的最后一个删掉
    if not eat:
        sankes.pop()
    #移动
    if direct == "left":
        head.col -= 1
    elif direct == "right":
        head.col += 1
    elif direct == "up":
        head.row -= 1
    elif direct == "down":
        head.row += 1
    #检测
    dead = False
    swyy = False
    # 1.撞墙
    if head.col < 0 or head.row < 0 or head.col >= COL or head.row >= ROW:
        dead = True
    # 2.撞自己
    for snake in sankes:
        if head.col == snake.col and head.row == snake.row:
            dead = True
            break
        #死亡音乐
        if dead:
            pygame.mixer.music.load("F:/0python文件/死亡音乐2.mp3")
            pygame.mixer.music.play(0,0)
            time.sleep(3)
            #Game over
            time.sleep(2)

            go = pygame.image.load("F:/0python文件/贪吃蛇/结束.png")
            screen.blit(go, (0, 0))
            pygame.display.update()
            time.sleep(2)
            swyy = True
            break
    if dead and swyy:
        print('死了')
        quit = True
        break
    #渲染--画出来
    pygame.draw.rect(screen,(bj_color),(0,0,w,h))        #1-往哪画  2-颜色  背景
    rect(head,head_color)     #蛇头
    rect(food,food_color)     #食物
    for sanke in sankes:      #蛇身
        rect(sanke,ss_color)
    #设置帧频
    clock.tick(20)      #0tick = 设置帧频
    pygame.display.flip()  # 让出控制权

