import pygame
import cfg
import 吃豆子 as eat
import random,time,os
import cv2
import hand
import threading
import 坦克大战 as tank
import kitten as kit
import Game3

# 设置常量
# 颜色
GREEN = (50,180,200)
BLACK =(0,0,0)
GRAY = (150,140,200)
BACKGROUND = (222,222,222)
# 游戏图标位置及大小
GAME1_X = 60
GAME_Y = 200
GAME2_X = 450
GAME_W = 150
GAME_H = 150
ALPHA = 100
a = False
b = False
# 窗口大小
W,H = 800,600
# 自定义敌机出现的时间
CREATE_ENEMY = pygame.USEREVENT

# 初始化
pygame.init()
pygame.mixer.init()
# 创建游戏窗口
SCREEN = pygame.display.set_mode((W,H))
SCREEN.fill((222,222,222))
# 设置游戏名称
pygame.display.set_caption("menu")
# 设置系统时钟
CLOCK = pygame.time.Clock()
pygame.time.set_timer(CREATE_ENEMY,1000) # 间隔2秒调用事件CREATE_ENEMY


# # 添加背景音乐
# pygame.mixer.music.load("sounds\\enviro.mp3")
# pygame.mixer.music.set_volume(0.4)
# pygame.mixer.music.play(-1,0)

    
def get_input():
    global ipt
    while True:
        # ipt = input(ipt)
        time.sleep(3)

def enter_game(): 
    handing = hand.hands()           # 实例化手势识别的对象
    # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在 创建一个线程运行手势识别
    t1 = threading.Thread(target=handing.handcontroller)               
    t1.start()            # 运行手势线程
    while True:
        # 设置刷新率
        CLOCK.tick(60)
        ipt = handing.index
        
        # 显示字体
        font = pygame.font.Font(cfg.FONTPATH, 50)  # 从文件创建新字体对象，设置字体大小为40
        score_text = font.render("You can choose a game", True, cfg.BLACK)
        SCREEN.blit(score_text,[100,100])
        pygame.display.flip()

        i_1 = pygame.image.load("resources\\Myimage\\002.png")
        i_1 = pygame.transform.scale(i_1,(GAME_W,GAME_H))
        SCREEN.blit(i_1,[GAME1_X, GAME_Y])
        # 显示字体
        font = pygame.font.Font(cfg.FONTPATH, 30)  # 从文件创建新字体对象，设置字体大小为40
        score_text = font.render("Gjigsaw puzzle", True, cfg.BLACK)
        SCREEN.blit(score_text,[GAME1_X-20,360])
        pygame.display.flip()
        
        i_1 = pygame.image.load("resources\\Myimage\\001.png")
        i_1 = pygame.transform.scale(i_1,(GAME_W,GAME_H))
        SCREEN.blit(i_1,[300, GAME_Y])
        # 显示字体
        font = pygame.font.Font(cfg.FONTPATH, 30)  # 从文件创建新字体对象，设置字体大小为40
        score_text = font.render("Pac-Man", True, cfg.BLACK)
        SCREEN.blit(score_text,[320,360])
        pygame.display.flip()

        i_1 = pygame.image.load("resources\\Myimage\\004.png")
        i_1 = pygame.transform.scale(i_1,(GAME_W,GAME_H))
        SCREEN.blit(i_1,[540, GAME_Y])
        # 显示字体
        font = pygame.font.Font(cfg.FONTPATH, 30)  # 从文件创建新字体对象，设置字体大小为40
        score_text = font.render("More...", True, cfg.BLACK)
        SCREEN.blit(score_text,[540+20,360])
        pygame.display.flip()
                
        # 玩家操作
        pygame.event.get()
        
        # 实现选择的
        if ipt == 1:
            # 加入变化代码
            # 背景画布
            surface_3=pygame.Surface([GAME_W,GAME_H])
            surface_3.set_alpha(ALPHA)
            surface_3.fill(GREEN)
            SCREEN.blit(surface_3, [GAME1_X, GAME_Y]) # screen.blit（对像，位置）：绘制到指定位置
            # pygame.display.update()

        elif ipt == 2:
            # 加入变化代码
            # 背景画布
            surface_3=pygame.Surface([GAME_W,GAME_H])
            surface_3.set_alpha(ALPHA)
            surface_3.fill(GREEN)
            SCREEN.blit(surface_3, [300, GAME_Y]) # screen.blit（对像，位置）：绘制到指定位置
            # pygame.display.flip()

        elif ipt == 3:
            # 加入变化代码
            # 背景画布
            surface_3=pygame.Surface([GAME_W,GAME_H])
            surface_3.set_alpha(ALPHA)
            surface_3.fill(GREEN)
            SCREEN.blit(surface_3, [540, GAME_Y]) # screen.blit（对像，位置）：绘制到指定位置
            # pygame.display.flip()

        # 进入游戏
        if handing.is_start:
            if ipt == 1:
                print(ipt)
                time.sleep(1.5)
                Game3.main(handing)    

            elif ipt == 2:
                time.sleep(1.5)
                eat.main(SCREEN,handing)

            elif ipt == 3:
                # 显示字体
                font = pygame.font.Font(cfg.FONTPATH, 30)  # 从文件创建新字体对象，设置字体大小为40
                score_text = font.render("!!!Sorry, there aren't more game", True, cfg.RED)
                score_text1 = font.render("Please choose other games", True, cfg.RED)
                SCREEN.blit(score_text,[100,450])
                SCREEN.blit(score_text1,[150,500])
                pygame.display.flip()
                time.sleep(1.5)
                # tank.main(cfg)
                continue
        pygame.display.update()


if __name__ == "__main__":
    enter_game()
