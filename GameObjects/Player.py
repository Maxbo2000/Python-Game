import pygame

from GameObjects.MoveableObject import MoveableObject


class Player(MoveableObject):
    useMirrored = bool
    __SpriteHeight = 60
    __SpriteWidth = 60

    def __init__(self, health=int, name=str, walkspeed=int, x=int, y=int):
        super().__init__(health, name, walkspeed, x, y)
        self.sprite = pygame.transform.scale(pygame.image.load("Graphic/human.png"),
                                             (self.__SpriteHeight, self.__SpriteWidth))
        self.spriteMirrored = pygame.transform.flip(self.sprite, True, False)
        self.rect = self.sprite.get_rect()

    def get_height(self):
        return self.rect.height

    def get_width(self):
        return self.rect.width

    def draw(self, screen):
        self.setHitbox(pygame.Rect(self.getPosX(), self.getPosY(), self.__SpriteHeight, self.__SpriteWidth))
        if self.useMirrored:
            screen.blit(self.spriteMirrored, (self.getPosX(), self.getPosY()))
            return
        screen.blit(self.sprite, (self.getPosX(), self.getPosY()))

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.useMirrored = True
            self.move_left()
        if keys[pygame.K_d]:
            self.useMirrored = False
            self.move_right()
        if keys[pygame.K_w]:
            self.move_up()
        if keys[pygame.K_s]:
            self.move_down()

    def move_left(self):
        self.setPosX(self.getPosX() - self.getWalkSpeed())

    def move_right(self):
        self.setPosX(self.getPosX() + self.getWalkSpeed())

    def move_up(self):
        self.setPosY(self.getPosY() - self.getWalkSpeed())

    def move_down(self):
        self.setPosY(self.getPosY() + self.getWalkSpeed())
