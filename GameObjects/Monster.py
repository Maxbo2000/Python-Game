import math

import pygame

from GameObjects.MoveableObject import MoveableObject


class Monster(MoveableObject):
    __SpriteHeight = 60
    __SpriteWidth = 60

    def __init__(self, health=int, name=str, walkspeed=int, x=int, y=int):
        super().__init__(health, name, walkspeed, x, y)
        self.sprite = pygame.transform.scale(pygame.image.load("Graphic/monster.png"), (self.__SpriteHeight, self.__SpriteWidth))
        self.rect = self.sprite.get_rect()

    def get_height(self):
        return self.rect.height

    def get_width(self):
        return self.rect.width

    def draw(self, screen):
        self.setHitbox(pygame.Rect(self.getPosX(), self.getPosY(), self.__SpriteHeight, self.__SpriteWidth))
        screen.blit(self.sprite, (self.getPosX(), self.getPosY()))

    def move(self, player_x: int, player_y: int):
        dx = player_x - self.getPosX()
        dy = player_y - self.getPosY()
        length = math.sqrt(dx**2 + dy**2)
        dx /= length
        dy /= length
        distance = self.getWalkSpeed()  # or any other value you choose
        self.setPosX(self.getPosX() + dx * distance)
        self.setPosY(self.getPosY() + dy * distance)

