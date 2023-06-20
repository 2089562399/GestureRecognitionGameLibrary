
import os
import sys
import cfg
import random
import pygame
import hand
import threading
import time

'''判断游戏是否结束'''
def isGameOver(board, size):
    assert isinstance(size, int)
    num_cells = size * size
    for i in range(num_cells-1):
        if board[i] != i: return False
    return True


'''将空白Cell左边的Cell右移到空白Cell位置'''
def moveR(board, blank_cell_idx, num_cols):
    if blank_cell_idx % num_cols == 0: # 判断当空白图片cell全在最左边位置时，直接返回空白图片的索引
        return blank_cell_idx
    # 替换空白Cell和左边cell的位置索引
    board[blank_cell_idx-1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx-1] 
    return blank_cell_idx - 1 # 返回值：空白Cell的索引
'''将空白Cell右边的Cell左移到空白Cell位置'''
def moveL(board, blank_cell_idx, num_cols):
    # 判断当空白图片cell全在最右边位置时，直接返回空白图片的索引
    if (blank_cell_idx+1) % num_cols == 0: 
        return blank_cell_idx
    # 替换空白Cell和右边cell的位置索引
    board[blank_cell_idx+1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+1]
    return blank_cell_idx + 1 # 返回值：空白Cell的索引
'''将空白Cell上边的Cell下移到空白Cell位置'''
def moveD(board, blank_cell_idx, num_cols):
    # 判断当空白图片索引小于行数时，空白图片在最上层
    if blank_cell_idx < num_cols: return blank_cell_idx
    # 替换空白Cell和上边cell的位置索引
    board[blank_cell_idx-num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx-num_cols]
    return blank_cell_idx - num_cols # 返回值：空白Cell的索引
'''将空白Cell下边的Cell上移到空白Cell位置'''
def moveU(board, blank_cell_idx, num_rows, num_cols):
    # 判断当空白图片索引处于最后一行的索引位置内时
    if blank_cell_idx >= (num_rows-1) * num_cols: 
        return blank_cell_idx
    # 替换空白Cell和下边cell的位置索引
    board[blank_cell_idx+num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+num_cols]
    return blank_cell_idx + num_cols # 返回值：空白Cell的索引


'''获得打乱的拼图'''
def CreateBoard(num_rows, num_cols, num_cells): # 传入行数、列数、和cell数
    board = []
    for i in range(num_cells): 
        board.append(i)  
    # 去掉右下角那块
    blank_cell_idx = num_cells - 1  # 获取空白图的索引
    board[blank_cell_idx] = -1 # 设置-1：最后一个数据
    for i in range(cfg.NUMRANDOM): # 遍历100次进行图片次序的打乱
        # 0: left, 1: right, 2: up, 3: down
        direction = random.randint(0, 3) # 四个方向随机
        if direction == 0: blank_cell_idx = moveL(board, blank_cell_idx, num_cols)
        elif direction == 1: blank_cell_idx = moveR(board, blank_cell_idx, num_cols)
        elif direction == 2: blank_cell_idx = moveU(board, blank_cell_idx, num_rows, num_cols)
        elif direction == 3: blank_cell_idx = moveD(board, blank_cell_idx, num_cols)
    return board, blank_cell_idx


'''随机选取一张图片'''
def GetImagePath(rootdir):
    imagenames = os.listdir(rootdir) # os.listdir () 返回指定的文件夹下包含的图片文件
    assert len(imagenames) > 0 
    return os.path.join(rootdir, random.choice(imagenames)) # 随机选择图片


'''显示游戏结束界面'''
def ShowEndInterface(screen, width, height):
    screen.fill(cfg.BACKGROUNDCOLOR)
    font = pygame.font.Font(cfg.FONTPATH, width//15)
    title = font.render('恭喜! 你成功完成了拼图!', True, (233, 150, 122))
    rect = title.get_rect()
    rect.midtop = (width/2, height/2.5)
    screen.blit(title, rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
        pygame.display.update()


'''显示游戏开始界面'''
def ShowStartInterface(screen, width, height,handing):
    wait_time5 = 0
    wait_time4 = 0
    wait_time3 = 0
    while True:
        time.sleep(0.1)

        # 填充背景色
        screen.fill((180,180,180)) 
        # 创建字体对象
        tfont = pygame.font.Font(cfg.FONTPATH, width//8) 
        cfont = pygame.font.Font(cfg.FONTPATH, width//20)
        title = tfont.render('拼拼乐', True, cfg.BLACK) 
        # 创建文字对象
        content1 = cfont.render('做出你的手势', True, cfg.BLACK)
        content2 = cfont.render('3秒后进入游戏……', True, cfg.BLUE)
        if handing.pattern == 5:
            str_modle = "现在选择的模式为5*5"
            wait_time5 += 0.1
            print(wait_time5)
            wait_time4 = 0
            wait_time3 = 0
            if wait_time5 >= 3:
                return 5
        elif handing.pattern == 4:
            str_modle = "现在选择的模式为4*4"
            wait_time4 += 0.1
            wait_time5 = 0
            wait_time3 = 0
            if wait_time4 >= 3:
                return 4
        elif handing.pattern == 3:
            str_modle = "现在选择的模式为3*3"
            wait_time3 += 0.1
            wait_time5 = 0
            wait_time4 = 0
            if wait_time3 >= 3:
                return 3
        content3 = cfont.render(str_modle,True,cfg.BLUE)    
        # 设置文字位置
        trect = title.get_rect()
        trect.midtop = (width/2, height/10)
        crect1 = content1.get_rect()
        crect1.midtop = (width/2,height/3.3)
        crect2 = content2.get_rect()
        crect2.midtop = (width/2, height/2.8)
        crect3 = content3.get_rect()
        crect3.midtop = (width/2,height/1.6)
        # 显示文字
        screen.blit(title, trect)
        screen.blit(content1, crect1)
        screen.blit(content2, crect2)
        screen.blit(content3, crect3)
        pygame.event.get()
        pygame.display.update()

'''主函数'''
def main(handing):
    # 初始化
    pygame.init()
    clock = pygame.time.Clock()
    # 加载图片
    game_img_used = pygame.image.load(GetImagePath(cfg.PICTURE_ROOT_DIR))
    game_img_used = pygame.transform.scale(game_img_used, cfg.SCREENSIZE)
    game_img_used_rect = game_img_used.get_rect()
    # 设置窗口
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('拼图游戏')
    # 游戏开始界面，返回拼图模式（3，4，5）
    size = ShowStartInterface(screen, game_img_used_rect.width, game_img_used_rect.height,handing)
    assert isinstance(size, int) # 判断变量size是否是int
    num_rows, num_cols = size, size # 设置图片的行数和列数
    num_cells = size * size # 所有的cell数量
    # 取整除，计算分割后每个cell的大小
    cell_width = game_img_used_rect.width // num_cols
    cell_height = game_img_used_rect.height // num_rows
    # 避免初始化为原图
    while True:
        game_board, blank_cell_idx = CreateBoard(num_rows, num_cols, num_cells)
        if not isGameOver(game_board, size):
            break
    # 游戏主循环
    is_running = True
    while is_running:
        # --事件捕获
        for event in pygame.event.get():
            # ----退出游戏
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            # # ----键盘操作
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT or event.key == ord('a'):
            #         blank_cell_idx = moveL(game_board, blank_cell_idx, num_cols)
            #     elif event.key == pygame.K_RIGHT or event.key == ord('d'):
            #         blank_cell_idx = moveR(game_board, blank_cell_idx, num_cols)
            #     elif event.key == pygame.K_UP or event.key == ord('w'):
            #         blank_cell_idx = moveU(game_board, blank_cell_idx, num_rows, num_cols)
            #     elif event.key == pygame.K_DOWN or event.key == ord('s'):
            #         blank_cell_idx = moveD(game_board, blank_cell_idx, num_cols)
            # # ----鼠标操作
            # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #     x, y = pygame.mouse.get_pos()
            #     # 640*640 左上角为（0，0）
            #     x_pos = x // cell_width
            #     y_pos = y // cell_height
            #     idx = x_pos + y_pos * num_cols
            #     if idx == blank_cell_idx-1: # 空白Cell左移
            #         blank_cell_idx = moveR(game_board, blank_cell_idx, num_cols)
            #     elif idx == blank_cell_idx+1:
            #         blank_cell_idx = moveL(game_board, blank_cell_idx, num_cols)
            #     elif idx == blank_cell_idx+num_cols:
            #         blank_cell_idx = moveU(game_board, blank_cell_idx, num_rows, num_cols)
            #     elif idx == blank_cell_idx-num_cols:
            #         blank_cell_idx = moveD(game_board, blank_cell_idx, num_cols)
        
        
        # 获取手势在游戏中映射的位置
        pygame.draw.circle(screen,cfg.BLACK,(640 - handing.x_between_finger_tip,handing.y_between_finger_tip),5,5)
        pygame.display.flip()
        if handing.is_select:
            print(640 - handing.x_between_finger_tip,handing.y_between_finger_tip)
            x = 640 - handing.x_between_finger_tip
            y = handing.y_between_finger_tip
            x_pos = x // cell_width
            y_pos = y // cell_height
            idx = x_pos + y_pos * num_cols
            if idx == blank_cell_idx-1: # 空白Cell左边的图右移，返回移动后空白cell的索引
                blank_cell_idx = moveR(game_board, blank_cell_idx, num_cols)
            elif idx == blank_cell_idx+1: # 空白Cell右边的图左移
                blank_cell_idx = moveL(game_board, blank_cell_idx, num_cols)
            elif idx == blank_cell_idx+num_cols: # 空白Cell下边的图上移
                blank_cell_idx = moveU(game_board, blank_cell_idx, num_rows, num_cols)
            elif idx == blank_cell_idx-num_cols: # 空白Cell上边的图下移
                blank_cell_idx = moveD(game_board, blank_cell_idx, num_cols)
        # --判断游戏是否结束
        if isGameOver(game_board, size):
            game_board[blank_cell_idx] = num_cells - 1
            is_running = False
        # --更新屏幕
        screen.fill(cfg.BACKGROUNDCOLOR)
        for i in range(num_cells):
            if game_board[i] == -1:
                continue
            x_pos = i // num_cols # x 的位置（0--（列-1））
            y_pos = i % num_cols # 获取0到num_cols-1
            # 绘制矩形框（左上角，宽，高）
            rect = pygame.Rect(y_pos*cell_width, x_pos*cell_height, cell_width, cell_height)
            img_area = pygame.Rect((game_board[i]%num_cols)*cell_width, (game_board[i]//num_cols)*cell_height, cell_width, cell_height)
            screen.blit(game_img_used, rect, img_area)
        # 绘制每个cell的边界线
        for i in range(num_cols+1):
            pygame.draw.line(screen, cfg.BLACK, (i*cell_width, 0), (i*cell_width, game_img_used_rect.height))
        for i in range(num_rows+1):
            pygame.draw.line(screen, cfg.BLACK, (0, i*cell_height), (game_img_used_rect.width, i*cell_height))
        pygame.display.update()
        clock.tick(cfg.FPS)
    # 游戏结束界面
    ShowEndInterface(screen, game_img_used_rect.width, game_img_used_rect.height)


'''run'''
if __name__ == '__main__':
    handing = hand.hands()           # 实例化手势识别的对象
    # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在 创建一个线程运行手势识别
    t1 = threading.Thread(target=handing.handcontroller)               
    t1.start()            # 运行手势线程
    time.sleep(5)
    main(handing)