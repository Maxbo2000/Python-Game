from pygame import Rect


class MoveableObject:
    def __init__(self, health, name, walkspeed, hitbox_x, hitbox_y, height, width):
        self.__Health = health
        self.__Name = name
        self.__WalkSpeed = walkspeed
        self.__HitBox_X = hitbox_x
        self.__HitBox_Y = hitbox_y
        self.__HitBox_H = height
        self.__HitBox_W = width

    __Health: int
    __Name: str
    __WalkSpeed: float
    __HitBox_X: int
    __HitBox_Y: int
    __HitBox_H: int
    __HitBox_W: int

    def makeHitBox(self):
        hitbox = Rect(self.__HitBox_X, self.__HitBox_Y, self.__HitBox_H, self.__HitBox_W)
        return hitbox

