import pygame

from GameObjects.MoveableObject import MoveableObject

class Player(MoveableObject):
    def __init__(self, health=int, name=str, walkspeed=int, height=int, width=int, x=int, y=int):
        super().__init__(health, name, walkspeed, height, width, x, y)
        sprite: None
        inv: None

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()

    def move_left(self):
        self.setPosX(self.getPosX() - self.getWalkSpeed())

    def move_right(self):
        self.setPosX(self.getPosX() + self.getWalkSpeed())

    def move_up(self):
        self.setPosY(self.getPosY() - self.getWalkSpeed())

    def move_down(self):
        self.setPosY(self.getPosY() + self.getWalkSpeed())

