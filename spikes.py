import pygame
from funct import load_image


class Spike(pygame.sprite.Sprite):
    def __init__(self, spike_image, spike_group):
        super().__init__(spike_group)
        self.image = load_image(spike_image)
        self.height = -30
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.passs = 0
        self.length = 20
        self.amount = 2
        self.distanceApart = 50
