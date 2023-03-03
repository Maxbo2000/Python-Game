import pygame
import sys

from GameObjects.Monster import Monster
from GameObjects.Player import Player

if __name__ == '__main__':
    print('PyCharm')

pygame.init()
player = Player(100, "test", 2, 40, 80, 0, 0)
monster = Monster(100, "test_Monster", 1, 40, 80, 300, 300)
pygame.display.set_caption("Humans vs Monster")
screen = pygame.display.set_mode([600, 600])

clock = pygame.time.Clock()

while True:
    # Bildschirm schließen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Bewegungssteuerung
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_UP]:
        player.move_up()
    if keys[pygame.K_DOWN]:
        player.move_down()
    if keys[pygame.K_y]:
        monster.move(player.getPosX(), player.getPosY())

    # Bildschirm-Update
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), (player.getPosX(), player.getPosY(), player.getHitBox_H(), player.getHitBox_W()))
    pygame.draw.rect(screen, (255, 0, 0), (monster.getPosX(), monster.getPosY(), monster.getHitBox_H(), monster.getHitBox_W()))
    pygame.display.update()

    # Framerate-Limit
    clock.tick(60)

