import pygame
import sys
from GameObjects.Player import Player

if __name__ == '__main__':
    print('PyCharm')


pygame.init()
player = Player(100, "test", 1.00, 10, 10, 40, 80, 0, 0)
pygame.display.set_caption("Humans vs Monster")
screen = pygame.display.set_mode([600, 600])


screen.fill((0, 0, 0))
clock = pygame.time.Clock()
pygame.draw.rect(screen,(255,255,0), (player.getPosY(),player.getPosX(),player.getHitBox_H(),player.getHitBox_W()))
#pygame.draw.rect(screen, (255, 255, 0), (player.getPosX(),player.getPosY(),player.getHitboxW(),player.getHitboxH()))

#Um das Fenster offen zulassen-------------
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
#--------------------------
clock.tick(60)


#print(player.getHealth())