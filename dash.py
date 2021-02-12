import pygame
from param import spike, platform
from funct import load_image


class Dash(pygame.sprite.Sprite):
    def __init__(self, player_image, spr_group):
        super().__init__(spr_group)
        self.is_dead = False
        self.image = load_image(player_image)
        self.width = 40
        self.height = 40
        self.pos_x = 200
        self.pos_y = 580
        self.velocity = 50
        self.jumping = 0
        self.y_velocity = 0
        self.rect = self.image.get_rect().move(
            -spike["height"] * self.pos_x + 15, -spike["height"] * self.pos_y + 5)

    def jump(self):
        if self.jumping == 0:
            if self.pos_y <= platform['y']:
                self.jumping = 1
        if self.jumping == 1:
            self.pos_y -= self.y_velocity
            if self.pos_y > platform['y']:
                self.jumping = 2
            self.y_velocity -= 0.5
        elif 2 <= self.jumping < 5:
            self.jumping += 1
        else:
            self.jumping = 0
