import pygame
from random import randint
import sys
import os

pygame.init()

score = 0
total = 0

font = pygame.font.SysFont('f', 50)


# Jumping Variables
yVel = 0
jumping = 0
# if ghoul)
is_dead = False


display = {
    "width": 1280,
    "height": 720
}

character = {
    "width": 20,
    "height": 20,
    "x": 200,
    "y": 580,
    "velocity": 50
}

platform = {
    'y': 580,
    "x": 700,
    "pass": 0,
    "length": 20,
    "amount": 2,
    "distanceApart": 50
}
spike = {
    "height": -15,
    "y": 600,
    "x": 700,
    "pass": 0,
    "length": 20,
    "amount": 2,
    "distanceApart": 50
}


class Dash:
    def __init__(self):
        pass


test = 0
screen = pygame.display.set_mode((display["width"], display["height"]))


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


def nextSection():
    spike["x"] = 700
    spike['pass'] += spike['amount']
    spike['amount'] = randint(1, 4)
    spike['distanceApart'] = randint(2, 4) * 10
    return


def start_screen():
    intro_text = []

    fon = pygame.transform.scale(load_image('start.png'), (display["width"], display["height"]))
    screen.blit(fon, (0, 0))
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    clock = pygame.time.Clock()
    while True:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                terminate()
            elif even.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(60)


def triangleDraw(num):  # Draws the triangles
    pygame.draw.polygon(displ,
                        (0, 0, 0),
                        ((spike["x"] + spike['distanceApart'] * num, spike["y"]),
                         (spike['x'] + spike['distanceApart'] * num + spike["length"], spike['y']),
                         (spike['x'] + spike['length'] / 2 + spike['distanceApart'] * num,
                          spike['y'] + spike['height'])))


def jump():  # Start Jumping
    global yVel
    global jumping
    if jumping == 0:
        jumping = 1
        yVel = 10
        character['y'] = character['y'] - yVel
        if character['y'] > platform['y']:
            jumping = 0
        yVel -= 0.5


def cJump():  # Continue Jump
    global yVel
    global jumping
    if jumping == 0:
        if character['y'] > platform['y']:
            pass
        else:
            jumping = 1
    if jumping == 1:
        character['y'] = character['y'] - yVel
        if character['y'] > platform['y']:
            jumping = 2
        yVel -= 0.5
    elif 2 <= jumping < 5:
        jumping += 1
    else:
        jumping = 0


def next_step():
    cJump()
    pygame.draw.rect(displ, (255, 0, 0),
                     (character["x"],
                      character["y"],
                      character["width"],
                      character["height"]))
    pygame.display.update()
    spike['x'] -= 5


# Launching the window, setting it to the dimensions of the `display` dictionary.
displ = pygame.display.set_mode((display["width"], display["height"]))


while True:  # Main Game Loop
    pygame.time.delay(10)
    displ.fill((255, 255, 255))
    for i in range(spike['amount']):  # Spike Drawing
        triangleDraw(i)
    for event in pygame.event.get():  # Quit statement
        if event.type == pygame.QUIT:
            break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:  # Checks if need to Jump
            jump()
    if spike['x'] + spike['distanceApart'] * spike['amount'] < character['x']:  # checks to start next section
        nextSection()
    if spike['pass'] < 100:  # Win Statement
        text_surface2 = font.render("Percentage {0}%".format(spike['pass']), False, (0, 0, 0))
        displ.blit(text_surface2, (300, 10))
    else:
        text_surface2 = font.render("YOU WIN", False, (255, 0, 0))
        displ.blit(text_surface2, (300, 10))
        break
    for i in range(spike['amount']):  # Checks if death occurs
        if spike['x'] + spike['distanceApart'] * i <= character['x'] <= spike['x'] \
                + spike['distanceApart'] * i + spike['length']:

            posOnSpike = abs(character['x'] - (spike['x'] + spike['length'] / 2))
            test = 1

            if posOnSpike * 2 + spike['y'] > character['y'] > spike['y'] \
                    or posOnSpike * 2 + spike['y'] > character['y'] + character['height'] > spike['y']:
                text_surface2 = font.render("YOU LOSE", False, (255, 0, 0))
                displ.blit(text_surface2, (300, 60))
                is_dead = True

        else:
            pass
    # Drawing Stuff
    next_step()
    if is_dead:
        break
