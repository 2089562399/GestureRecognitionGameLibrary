'''配置文件'''
import os  # python环境下对文件，文件夹执行操作的一个模块。

'''定义一些颜色'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
SKYBLUE = (0, 191, 178)
'''游戏素材路径'''
BGMPATH = os.path.join(os.getcwd(), 'resources/sounds/bg.mp3')  # os.getcwd()返回当前的路径
ICONPATH = os.path.join(os.getcwd(), 'resources/images/icon.png')  # os.path.join 拼接文件路径
FONTPATH = os.path.join(os.getcwd(), 'resources/font/ALGER.TTF')
HEROPATH = os.path.join(os.getcwd(), 'resources/images/pacman.png')
BlinkyPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
ClydePATH = os.path.join(os.getcwd(), 'resources/images/Clyde.png')
InkyPATH = os.path.join(os.getcwd(), 'resources/images/Inky.png')
PinkyPATH = os.path.join(os.getcwd(), 'resources/images/Pinky.png')
BACKGROUN = os.path.join(os.getcwd(),'resources/images/wallhaven-rr3k21.jpg')


'''坦克大战'''
'''字体'''
FONTPATH1 = os.path.join(os.getcwd(), 'resources/font/font.ttf')
'''图片'''
BULLET_IMAGE_PATHS = {
    'up': os.path.join(os.getcwd(), 'resources/images/bullet/bullet_up.png'),
    'down': os.path.join(os.getcwd(), 'resources/images/bullet/bullet_down.png'),
    'left': os.path.join(os.getcwd(), 'resources/images/bullet/bullet_left.png'),
    'right': os.path.join(os.getcwd(), 'resources/images/bullet/bullet_right.png')
}
ENEMY_TANK_IMAGE_PATHS = {
    '1': [
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_0.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_1.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_2.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_3.png')
    ],
    '2': [
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_0.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_1.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_2.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_3.png')
    ],
    '3': [
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_0.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_1.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_2.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_3.png')
    ],
    '4': [
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_4_0.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_4_1.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_4_2.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_4_3.png')
    ]
}
PLAYER_TANK_IMAGE_PATHS = {
    'player1': [
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T1_0.png'),
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T1_1.png'),
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T1_2.png')
    ],
    'player2': [
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T2_0.png'),
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T2_1.png'),
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T2_2.png')
    ]
}
FOOD_IMAGE_PATHS = {
    'boom': os.path.join(os.getcwd(), 'resources/images/food/food_boom.png'),
    'clock': os.path.join(os.getcwd(), 'resources/images/food/food_clock.png'),
    'gun': os.path.join(os.getcwd(), 'resources/images/food/food_gun.png'),
    'iron': os.path.join(os.getcwd(), 'resources/images/food/food_iron.png'),
    'protect': os.path.join(os.getcwd(), 'resources/images/food/food_protect.png'),
    'star': os.path.join(os.getcwd(), 'resources/images/food/food_star.png'),
    'tank': os.path.join(os.getcwd(), 'resources/images/food/food_tank.png')
}
HOME_IMAGE_PATHS = [
    os.path.join(os.getcwd(), 'resources/images/home/home1.png'),
    os.path.join(os.getcwd(), 'resources/images/home/home_destroyed.png')
]
SCENE_IMAGE_PATHS = {
    'brick': os.path.join(os.getcwd(), 'resources/images/scene/brick.png'),
    'ice': os.path.join(os.getcwd(), 'resources/images/scene/ice.png'),
    'iron': os.path.join(os.getcwd(), 'resources/images/scene/iron.png'),
    'river1': os.path.join(os.getcwd(), 'resources/images/scene/river1.png'),
    'river2': os.path.join(os.getcwd(), 'resources/images/scene/river2.png'),
    'tree': os.path.join(os.getcwd(), 'resources/images/scene/tree.png')
}
OTHER_IMAGE_PATHS = {
    'appear': os.path.join(os.getcwd(), 'resources/images/others/appear.png'),
    'background': os.path.join(os.getcwd(), 'resources/images/others/background.png'),
    'boom_dynamic': os.path.join(os.getcwd(), 'resources/images/others/boom_dynamic.png'),
    'boom_static': os.path.join(os.getcwd(), 'resources/images/others/boom_static.png'),
    'gameover': os.path.join(os.getcwd(), 'resources/images/others/gameover.png'),
    'logo': os.path.join(os.getcwd(), 'resources/images/others/logo.png'),
    'mask': os.path.join(os.getcwd(), 'resources/images/others/mask.png'),
    'protect': os.path.join(os.getcwd(), 'resources/images/others/protect.png'),
    'tip': os.path.join(os.getcwd(), 'resources/images/others/tip.png'),
    'gamebar': os.path.join(os.getcwd(), 'resources/images/others/gamebar.png')
}
'''声音'''
AUDIO_PATHS = {
    'add': os.path.join(os.getcwd(), 'resources/audios/add.wav'),
    'bang': os.path.join(os.getcwd(), 'resources/audios/bang.wav'),
    'blast': os.path.join(os.getcwd(), 'resources/audios/blast.wav'),
    'fire': os.path.join(os.getcwd(), 'resources/audios/fire.wav'),
    'Gunfire': os.path.join(os.getcwd(), 'resources/audios/Gunfire.wav'),
    'hit': os.path.join(os.getcwd(), 'resources/audios/hit.wav'),
    'start': os.path.join(os.getcwd(), 'resources/audios/start.wav')
}
'''屏幕'''
WIDTH = 630
HEIGHT = 630
BORDER_LEN = 3
GRID_SIZE = 24
PANEL_WIDTH = 150
TITLE = '坦克大战 —— 九歌'
'''关卡'''
LEVELFILEDIR = os.path.join(os.getcwd(), 'modules/levels')

'''屏幕大小'''
SCREENSIZE = (640, 640)
'''图片素材根目录'''
PICTURE_ROOT_DIR = os.path.join(os.getcwd(), 'resources/pictures')
'''字体路径'''
FONTPATH = os.path.join(os.getcwd(), 'resources/font/FZSTK.TTF')
'''定义一些颜色'''
BACKGROUNDCOLOR = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 0)
BLACK = (0, 0, 0)
'''FPS'''
FPS = 40
'''随机打乱拼图次数'''
NUMRANDOM = 100