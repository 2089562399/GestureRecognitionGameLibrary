import random
import pygame

'''墙类'''
class Wall(pygame.sprite.Sprite): # 继承父类pygame.sprite.Sprite
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self) # 调用父类的构造函数
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x 
        self.rect.top = y

'''食物类'''
class Food(pygame.sprite.Sprite):
    # args（arguments），表示位置参数；kwargs（keyword arguments），表示关键字参数
    def __init__(self, x, y, width, height, color, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

'''角色类'''
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, role_image_path,base_speed=[20,20]):
        pygame.sprite.Sprite.__init__(self)
        self.role_name = role_image_path.split('/')[-1].split('.')[0]  # 获取角色名字
        self.base_image = pygame.image.load(role_image_path).convert()  # 获下载角色图片
        self.image = self.base_image.copy()  # 复制角色图片
        self.rect = self.image.get_rect() # 获取图片的矩形信息
        self.rect.left = x
        self.rect.top = y
        self.prev_x = x
        self.prev_y = y
        self.base_speed = base_speed
        self.speed = [0, 0]
        self.is_move = False
        self.tracks = []
        self.tracks_loc = [0, 0]
    '''改变速度方向'''
    def changeSpeed(self, direction):
        if direction[0] < 0:
            # pygame.transform.flip（翻转图像，水平翻转，垂直翻转）：对图像进行水平和垂直翻转
            self.image = pygame.transform.flip(self.base_image, True, False) # 对图像进行水平翻转
        elif direction[0] > 0:
            self.image = self.base_image.copy()  # 不翻转时复制该图像
        elif direction[1] < 0:
            self.image = pygame.transform.rotate(self.base_image, 90)  # 旋转图像
        elif direction[1] > 0:
            self.image = pygame.transform.rotate(self.base_image, -90)
        self.speed = [direction[0] * self.base_speed[0], direction[1] * self.base_speed[1]]
        return self.speed
    '''更新角色位置'''
    def update(self, wall_sprites, gate_sprites):
        if not self.is_move: # 如果角色未移动
            return False
        # 角色先前的位置（与左边和上边的距离）
        x_prev = self.rect.left
        y_prev = self.rect.top
        # 角色的位置加上速度之后的位置
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]
        # pygame.sprite.spritecollide(sprite,sprite_group,bool) 角色和组之间的矩形冲突检测，发生冲突的精灵会作为一个列表is_collide返回。
        is_collide = pygame.sprite.spritecollide(self, wall_sprites, False) # True：会删除组中所有冲突的精灵，False：不会删除冲突的精灵
        if gate_sprites is not None:
            if not is_collide:
                is_collide = pygame.sprite.spritecollide(self, gate_sprites, False)
        if is_collide: # 当未发生碰撞时获取当前位置
            self.rect.left = x_prev
            self.rect.top = y_prev
            return False
        return True
    '''生成随机的方向'''
    def randomDirection(self):
        return random.choice([[-0.5, 0], [0.5, 0], [0, 0.5], [0, -0.5]])