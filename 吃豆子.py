import sys
import cfg
import pygame  # 被设计用来写游戏的python模块集合
import modules.Levels as Levels
import time
import hand
import threading # 引入多线程操作的库

'''角色控制'''
def rolecontroller(screen,hero_sprites, handing,i,font):
    # 第2帧画面暂停游戏
    if i == 2:
        # 背景画布
        surface_1=pygame.Surface([580,300])
        surface_1.set_alpha(200)
        surface_1.fill((0,0,0))
        screen.blit(surface_1, [10, 100]) # screen.blit（对像，位置）：绘制到指定位置
        # 显示字体
        font = pygame.font.Font(cfg.FONTPATH, 40)  # 从文件创建新字体对象，设置字体大小为40
        score_text = font.render("Use gestures to started", True, cfg.WHITE)
        screen.blit(score_text,[40,220])
        pygame.display.flip()
        while True:
            if handing.is_start:
                break
    a = handing.direction
    if a == 3:           #右
        for hero in hero_sprites:
            hero.changeSpeed([1, 0])
            hero.is_move = True     
    elif a == 2:         #左
        for hero in hero_sprites:
            hero.changeSpeed([-1, 0])
            hero.is_move = True   
    elif a == 0:         #上
        for hero in hero_sprites:
            hero.changeSpeed([0, -1])
            hero.is_move = True      
    elif a == 1:         #下
        for hero in hero_sprites:
            hero.changeSpeed([0, 1])
            hero.is_move = True     
    return

'''开始游戏'''
def startLevelGame(handing, level, screen, font):   
    clock = pygame.time.Clock()  # 第一次调用，返回的是程序运行的实际时间
    SCORE = 0
    wall_sprites = level.setupWalls(cfg.SKYBLUE)
    gate_sprites = level.setupGate(cfg.WHITE)
    hero_sprites, ghost_sprites = level.setupPlayers(cfg.HEROPATH, [cfg.BlinkyPATH, cfg.ClydePATH, cfg.InkyPATH, cfg.PinkyPATH])
    food_sprites = level.setupFood([255,0,0])
    is_clearance = False
    i = 0
    while True:
        i += 1
        # time.sleep(0.15)                      # 设置间隔几秒一帧画面
        print("第{}帧".format(i))
        pygame.event.get()  # 从事件队列中获取一个事件，并从队列中删除该事件
        
        rolecontroller(screen,hero_sprites, handing,i,font)         # 检测手势

        screen.fill(cfg.BLACK)  # 背景窗口颜色
        # img=pygame.image.load(cfg.BACKGROUND)
        # screen.blit(img,[0,0])
        
        for hero in hero_sprites:
            hero.update(wall_sprites, gate_sprites) 
        hero_sprites.draw(screen)
        for hero in hero_sprites:
            # 查看hero是否与组类food_sprites中的任何内容冲突
            food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)
        SCORE += len(food_eaten)  # 计分：玩家吃到的豆子总数
        wall_sprites.draw(screen)
        gate_sprites.draw(screen)
        food_sprites.draw(screen)
        for ghost in ghost_sprites:
            # 指定幽灵运动路径
            if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]*2:
                ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
                ghost.tracks_loc[1] += 1
            else:
                
                if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                    ghost.tracks_loc[0] += 1
                elif ghost.role_name == 'Clyde':
                    ghost.tracks_loc[0] = 2
                else:
                    ghost.tracks_loc[0] = 0
                ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
                ghost.tracks_loc[1] = 0
            if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]*2:
                ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
            else:
                if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                    loc0 = ghost.tracks_loc[0] + 1
                elif ghost.role_name == 'Clyde':
                    loc0 = 2
                else:
                    loc0 = 0
                ghost.changeSpeed(ghost.tracks[loc0][0: 2])
            ghost.update(wall_sprites, None)
        ghost_sprites.draw(screen)

        font_Score = pygame.font.Font(cfg.FONTPATH, 30)  # 从文件创建新字体对象，设置字体大小为40
        score_text = font_Score.render("Score: %s" % SCORE, True, cfg.WHITE)
        screen.blit(score_text, [0, 0])
        
        if len(food_sprites) == 0:
            is_clearance = True
            break
        if pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False):
            is_clearance = False
            break
        pygame.display.flip()
        clock.tick(10)
    return is_clearance


'''显示文字'''
def showText(screen, font, is_clearance, flag=False):
    clock = pygame.time.Clock()  # 第二次调用，返回的是自第一次调用后,到这次调用的时间间隔
    msg = 'Game Over!' if not is_clearance else 'Congratulations, you won!'
    # 设置字体位置，画布左上角和右下角位置
    positions = [[200, 280], [65, 303], [170, 333]] if not is_clearance else [[145, 233], [65, 303], [170, 333]]

    surface = pygame.Surface((400, 200))
    surface.set_alpha(200)   # 设置背景画布透明度  
    surface.fill((128, 128, 128))   # 设置字体背景颜色
    screen.blit(surface, (100,200))  # 显示背景在上层
    
    texts = [font.render(msg, True, cfg.WHITE)]  # 游戏结束文字
    while True:
        for idx, (text, position) in enumerate(zip(texts, positions)):
            screen.blit(text, position)
        pygame.display.flip()
        clock.tick(10)


'''初始化首界面'''
def initialize():
    pygame.init() # 导入并初始化所有pygame模块
    # pygame.display模块：用于创建、管理游戏窗口
    # pygame.display.update():刷新屏幕内容显示
    screen = pygame.display.set_mode([606, 606])  # 初始化游戏窗口
    pygame.display.set_caption('吃豆人')
    return screen

'''主函数'''
def main(screen,handing):
    # pygame.mixer：用于加载和播放声音的pygame模块
    pygame.mixer.init()  # 初始化混音器模块
    pygame.mixer.music.load(cfg.BGMPATH)  # 载入一个音乐文件用于播放
    pygame.mixer.music.play(-1, 0.0)  # 开始播放音乐流

    # 初始化字体模块
    pygame.font.init()  
    # 1、pygame.font.Font:创建字体对象
    # 2、font.render（文字内容，true，文字颜色，背景颜色）:创建文字对象
    # 3、window.blit(text,位置)：渲染到窗口上  4、刷新屏幕显示
    font = pygame.font.Font(cfg.FONTPATH, 40)  # 从文件创建新字体对象，设置字体大小为40
    level = getattr(Levels, f'Level{1}')() # getattr 返回一个对象（level）属性值。
    is_clearance = startLevelGame(handing, level, screen, font)
    showText(screen, font, is_clearance, True)

'''run'''
if __name__ == '__main__':
    handing = hand.hands()           # 实例化手势识别的对象
    # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在 创建一个线程运行手势识别
    t1 = threading.Thread(target=handing.handcontroller)               
    t1.start()            # 运行手势线程
    main(initialize(),handing)