import pygame
from funct import load_image, terminate
from random import randint
import sys
from param import spike, display, character, platform

pygame.init()

score = 0
total = 0

font = pygame.font.SysFont('f', 50)
all_sprites = pygame.sprite.Group
player_image = load_image("dash.png")

# if ghoul)
is_dead = False


screen = pygame.display.set_mode((display["width"], display["height"]))
displ = pygame.display.set_mode((display["width"], display["height"]))


def nextSection():
    spike["x"] = 700
    spike['pass'] += spike['amount']
    spike['amount'] = randint(1, 4)
    spike['distanceApart'] = randint(2, 4) * 10
    return


def triangleDraw(num):  # Draws the triangles
    pygame.draw.polygon(
        displ,
        (0, 0, 0),
        ((spike["x"] + spike['distanceApart'] * num, spike["y"]),
         (spike['x'] + spike['distanceApart'] * num + spike["length"], spike['y']),
         (spike['x'] + spike['length'] / 2 + spike['distanceApart'] * num,
          spike['y'] + spike['height'])))


# Jumping Variables
yVel = 0
jumping = 0


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
        character['y'] -= yVel
        if character['y'] > platform['y']:
            jumping = 2
        yVel -= 0.5
    elif 2 <= jumping < 5:
        jumping += 1
    else:
        jumping = 0


def print_progress():
    if spike['pass'] < 100:  # Win Statement
        text_surface_2 = font.render("Percentage {0}%".format(spike['pass']), False, (0, 0, 0))
        displ.blit(text_surface_2, (300, 10))
    else:
        text_surface_2 = font.render("YOU WIN", False, (255, 0, 0))
        displ.blit(text_surface_2, (300, 10))


def next_step():
    cJump()
    pygame.draw.rect(displ, (255, 0, 0),
                     (character["x"],
                      character["y"],
                      character["width"],
                      character["height"]))
    pygame.display.update()
    spike['x'] -= 5


def check_next_ses(charar_x):
    if spike['x'] + spike['distanceApart'] * spike['amount'] < charar_x:
        return True
    return False


bg = load_image('fon.jpg')

while True:  # Main Game Loop
    pygame.time.delay(10)
    for i in range(spike['amount']):  # Spike Drawing
        triangleDraw(i)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:  # Checks Jump
            jump()
    if check_next_ses(character['x']):
        nextSection()
    print_progress()
    for i in range(spike['amount']):  # Checks if death occurs
        if spike['x'] + spike['distanceApart'] * i <= character['x'] <= spike['x'] \
                + spike['distanceApart'] * i + spike['length']:

            posOnSpike = abs(character['x'] - (spike['x'] + spike['length'] / 2))
            if posOnSpike * 2 + spike['y'] > character['y'] > spike['y'] \
                    or posOnSpike * 2 + spike['y'] > character['y'] + character['height'] > spike['y']:
                text_surface2 = font.render("YOU LOSE", False, (255, 0, 0))
                displ.blit(text_surface2, (300, 60))
                is_dead = True
    # Drawing Stuff
    next_step()
    if is_dead:
        terminate()
    screen.blit(bg, (0, 0))