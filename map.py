from funct import load_image
import pygame

pygame.init()
all_sprites = pygame.sprite.Group()
tiles = pygame.sprite.Group()
player = pygame.sprite.Group()
images = {
    'block': load_image("block.png"),
    'spike': load_image("spike.png"),
    'empty': load_image("empty.png"),
    'player': load_image("dash.png")
}

spec = {
    '.': 'empty',
    '*': 'empty',
    '#': 'block',
    '?': 'spike',
}


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, kind):
        super().__init__(tiles, all_sprites)
        pos_x = pos_x * 20
        pos_y = pos_y * 20
        self.image = images[kind]
        self.rect = self.image.get_rect().move(
            pos_y, pos_x
        )


class Dash(pygame.sprite.Sprite):
    def __init__(self, player_image, pos_x, pos_y):
        super().__init__(player, all_sprites)
        self.is_dead = False
        self.image = load_image(player_image)
        self.velocity = 10
        self.pos_y = pos_y * 20
        self.down_pos = pos_x * 20
        self.jumping = 0
        self.y_velocity = 0
        self.rect = self.image.get_rect().move(
            self.pos_y - 80, pos_x * 20
        )

    def update(self):
        self.rect[0] += self.velocity
        self.rect[1] -= self.y_velocity
        if self.jumping == 1:
            self.jumping = 2
        if 2 <= self.jumping < 6:  # 4 steps too
            self.jumping += 1
        if self.jumping == 6:  # 1 step for x
            self.y_velocity = 0
            self.jumping += 1
            print(self.rect[0], self.rect[1])
        if 6 <= self.jumping < 12:  # 4 steps, 10 px
            self.jumping += 1
            self.y_velocity = -20
        if self.jumping == 12:
            self.jumping = self.y_velocity = 0
        ##################
        if self.rect[0] in platforms:
            if self.rect[1] == 600:
                self.is_dead = True

        # 1 jump = +40 -- x, +-80 -- y #

    def jump(self):
        if self.jumping == 0:
            self.jumping = 1
            self.y_velocity = 20


"""
1 block = (20px; 20px)
vel = 5px
1 jump = (40px; 80px-+)
"""


def made_map(maptxt):
    person, x, y = None, None, None
    can_be = []
    with open(f'data/{maptxt}', 'r') as st_map:
        map1 = st_map.readlines()
    for x in range(len(map1)):
        for y in range(len(map1[x])):
            try:
                if map1[x][y] == '@':
                    player.add(Dash("dash.png", x, y))
                    person = Dash("dash.png", x, y)
                else:
                    tiles.add(Tile(x, y, spec[map1[x][y]]))
                    # its all for jumping
                    if spec[map1[x][y]] == 'spike':
                        can_be.append(y)
            except KeyError:
                pass
    return person, x, y, can_be


def norm_coords(arr):
    for i in range(len(arr)):
        arr[i] *= 20
    return arr


platforms = norm_coords(made_map("map.txt")[3])  # blocks with their coord(first -- y * 20, second -- x * 20)
print(platforms)

