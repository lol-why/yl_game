import pygame
from funct import load_image, terminate
from param import display
from map import made_map, tiles, player, all_sprites, do_norm_platf


pygame.init()  # инициализация
screen = pygame.display.set_mode((display["width"], display["height"]))  # экран для отрисовки
clock = pygame.time.Clock()  # для фпс
person, end_x, end_y, for_do = made_map("map.txt")  # координаты для камеры
# camera = Camera((end_x, end_y))  # камера
bg = load_image('fon.jpg')  # задний фон
while True:  # Main Game Loop
    # чек кнопок
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:  # Checks Jump
            person.jump()
    # чек смерти
    if person.is_dead:
        terminate()
    # рисует все остальное
    tiles.draw(screen)
    player.draw(screen)
    pygame.display.flip()
    person.update()
    screen.blit(bg, (0, 0))
    clock.tick(60)
