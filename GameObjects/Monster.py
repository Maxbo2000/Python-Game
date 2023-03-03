import math

from GameObjects.MoveableObject import MoveableObject

class Monster(MoveableObject):
    def __init__(self, health=int, name=str, walkspeed=int, height=int, width=int, x=int, y=int):
        super().__init__(health, name, walkspeed, height, width, x, y)
        sprite: None

    def move(self, player_x: int, player_y: int):
        dx = player_x - self.getPosX()
        dy = player_y - self.getPosY()
        length = math.sqrt(dx**2 + dy**2)
        dx /= length
        dy /= length
        distance = self.getWalkSpeed()  # or any other value you choose
        self.setPosX(self.getPosX() + dx * distance)
        self.setPosY(self.getPosY() + dy * distance)

