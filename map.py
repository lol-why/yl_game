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


class Dash(pygame.sprite.Sprite):
    def __init__(self, player_image, pos_x, pos_y):
        super().__init__(player, all_sprites)
        self.is_dead = False
        self.image = load_image(player_image)
        self.velocity = 5
        self.pos_y = pos_y * 20
        self.down_pos = pos_x * 20
        self.jumping = 0
        self.y_velocity = 0
        self.rect = self.image.get_rect().move(
            self.pos_y, pos_x * 20
        )

    def update(self):
        self.rect[0] += self.velocity
        self.rect[1] -= self.y_velocity
        if self.jumping == 1:
            self.jumping = 2
        if 2 <= self.jumping < 6:
            self.jumping += 1
        if self.jumping == 6:
            self.y_velocity = 0
            self.jumping += 1
            print(self.rect[0], self.rect[1])
            print(self.down_pos)
        if 6 <= self.jumping < 12:
            self.jumping += 1
            self.y_velocity = -20
        if self.jumping == 12:
            self.jumping = self.y_velocity = 0

    def jump(self):
        if self.jumping == 0:
            self.jumping = 1
            self.y_velocity = 20


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, kind):
        super().__init__(tiles, all_sprites)
        pos_x = pos_x * 20
        pos_y = pos_y * 20
        self.image = images[kind]
        self.rect = self.image.get_rect().move(
            pos_y, pos_x
        )


def made_map(maptxt):
    person, x, y = None, None, None
    platform_height = {}
    with open(f'data/{maptxt}', 'r') as st_map:
        map1 = st_map.readlines()
    for x in range(len(map1)):
        can_be = []
        for y in range(len(map1[x])):
            try:
                if map1[x][y] == '@':
                    player.add(Dash("dash.png", x, y))
                    person = Dash("dash.png", x, y)
                else:
                    tiles.add(Tile(x, y, spec[map1[x][y]]))
                    # its all for jumping
                    if spec[map1[x][y]] == 'block':
                        try:
                            for plat in platform_height:
                                if y in platform_height[plat]:
                                    raise ValueError
                            can_be.append(y)
                        except ValueError:
                            pass
            except KeyError:
                pass
        if len(can_be) != 0:
            platform_height[x + 1] = can_be
    return person, x, y, platform_height


def do_norm_platf(first_l):  # platforms and their coord
    norm_plat = {}
    for i in first_l:
        for j in first_l[i]:
            norm_plat[j] = i

    return norm_plat
