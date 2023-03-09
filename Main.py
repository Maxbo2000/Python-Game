import pygame
import sys

from GameObjects.HealthBar import HealthBar
from GameObjects.Monster import Monster
from GameObjects.Player import Player

if __name__ == '__main__':
    print('PyCharm')

pygame.init()


#health, name, walkspeed, x, y
player = Player(100, "test", 2, 0, 0)
monster = Monster(100, "test_Monster", 1, 300, 300)
# Test Variable konnte man testen ob der lebensbalken runter geht und es geht
#play = player.setHealth(50)

#Set the background
background = pygame.image.load("Graphic/background.jpg")

# Set up the screen
screen_width, screen_height = 862, 488
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Humans vs Monster")

clock = pygame.time.Clock()

# Set up the health bar
#x, y, height, width
healthBar = HealthBar(10, 10, 10, 100)

#Method for Collision checking
def checkCollision():
    if player.getHitbox().colliderect(monster.getHitbox()):
        player.setHealth(player.getHealth() - 10)
        player.setPosX(player.getPosX() + 20)
        monster.setHealth(player.getHealth() - 30)
        monster.setPosX(player.getPosX() - 20)

#main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player movement
    player.handle_keys()
    if player.getPosX() < 0:
        player.setPosX(0)
    if player.getPosX() > screen_width - player.get_width():
        player.setPosX(screen_width - player.get_width())
    if player.getPosY() < 0:
        player.setPosY(0)
    if player.getPosY() > screen_height - player.get_height():
        player.setPosY(screen_height - player.get_height())

    # Handle monster movement
    monster.move(player.getPosX(), player.getPosY())
    if monster.getPosX() < 0:
        monster.setPosX(0)
    if monster.getPosX() > screen_width - monster.get_width():
        monster.setPosX(screen_width - monster.get_width())
    if monster.getPosY() < 0:
        monster.setPosY(0)
    if monster.getPosY() > screen_height - monster.get_height():
        monster.setPosY(screen_height - monster.get_height())

    screen.blit(background, (0, 0))
    player.draw(screen)
    monster.draw(screen)
    healthBar.draw(screen, player)
    #Checkes if objects collided with eachother
    checkCollision()

    #Use this to draw hitboxes on screen for debugging purposes
    pygame.draw.rect(screen, (255, 0, 0), player.getHitbox(), 2)
    pygame.draw.rect(screen, (255, 0, 0), monster.getHitbox(), 2)

    pygame.display.update()

    # Framerate limit
    clock.tick(60)