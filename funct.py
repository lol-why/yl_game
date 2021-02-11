import pygame
import sys
import os


def get_pos(pos):
    return pos[0], pos[1]


def load_image(name):
    fullname = os.path.join(f'data/{name}')
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()



