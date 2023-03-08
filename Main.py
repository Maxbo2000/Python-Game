import pygame
import sys

from GameObjects.Monster import Monster
from GameObjects.Player import Player

if __name__ == '__main__':
    print('PyCharm')

pygame.init()

# Initialize font
pygame.font.init()
health_font = pygame.font.Font(None, 30)

player = Player(100, "test", 2, 40, 80, 0, 0)
monster = Monster(100, "test_Monster", 1, 40, 80, 300, 300)
# Test Variable konnte man testen ob der lebensbalken runter geht und es geht
# play = player.setHealth(50)

background = pygame.image.load("Graphic/background.jpg")
playerimage = pygame.image.load("Graphic/human.png")
playerimage = pygame.transform.scale(playerimage, (60, 60))

monsterimage = pygame.image.load("Graphic/monster.png")
monsterimage = pygame.transform.scale(monsterimage, (40, 40))

# Set up the screen
screen_width, screen_height = 862, 488
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Humans vs Monster")

clock = pygame.time.Clock()

# Set up the health bar
health_bar_width, health_bar_height = 100, 10
health_bar = pygame.Rect(10, 10, health_bar_width, health_bar_height)

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
    if player.getPosX() > screen_width - playerimage.get_width():
        player.setPosX(screen_width - playerimage.get_width())
    if player.getPosY() < 0:
        player.setPosY(0)
    if player.getPosY() > screen_height - playerimage.get_height():
        player.setPosY(screen_height - playerimage.get_height())

    # Handle monster movement
    monster.move(player.getPosX(), player.getPosY())
    if monster.getPosX() < 0:
        monster.setPosX(0)
    if monster.getPosX() > screen_width - monsterimage.get_width():
        monster.setPosX(screen_width - monsterimage.get_width())
    if monster.getPosY() < 0:
        monster.setPosY(0)
    if monster.getPosY() > screen_height - monsterimage.get_height():
        monster.setPosY(screen_height - monsterimage.get_height())

    # Update health bar
    health_bar.width = player.getHealth() * health_bar_width // 100

    screen.blit(background, (0, 0))
    screen.blit(playerimage, (player.getPosX(), player.getPosY()))
    screen.blit(monsterimage, (monster.getPosX(), monster.getPosY()))
    pygame.draw.rect(screen, (255, 255, 255), health_bar)
    pygame.draw.rect(screen, (0, 0, 0), health_bar, 2)
    health_text = health_font.render(f"{player.getHealth()} / 100", True, (255, 255, 255))
    screen.blit(health_text, (health_bar.x + 5, health_bar.y + health_bar_height + 5))
    pygame.display.update()

    # Framerate limit
    clock.tick(60)
