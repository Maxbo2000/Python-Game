from pygame import Rect


class MoveableObject:
    def __init__(self, health, name, walkspeed, hitbox_x, hitbox_y, height, width, x, y):
        self.__Health = health
        self.__Name = name
        self.__WalkSpeed = walkspeed
        self.__HitBox_X = hitbox_x
        self.__HitBox_Y = hitbox_y
        self.__HitBox_H = height
        self.__HitBox_W = width
        self.__Pos_X = x
        self.__Pos_Y = y

    __Health: int
    __Name: str
    __WalkSpeed: float
    __Pos_X: int
    __Pos_Y: int
    __HitBox_X: int
    __HitBox_Y: int
    __HitBox_H: int
    __HitBox_W: int

    def getHealth(self): return self.__Health
    def getName(self): return self.__Name
    def getWalkSpeed(self): return self.__WalkSpeed
    def getPosX(self): return self.__Pos_X
    def getPosY(self): return self.__Pos_Y
    def getHitBox_H(self): return self.__HitBox_H
    def getHitBox_W(self): return self.__HitBox_W
    def setHealth(self, value): self.__Health = value
    def setName(self, value): self.__Name = value
    def setWalkSpeed(self, value): self.__WalkSpeed = value
    def setPosX(self, value): self.__Pos_X = value
    def setPosY(self, value): self.__Pos_Y = value
    def setHitboxX(self, value): self.__HitBox_X = value
    def setHitBoxY(self, value): self.__HitBox_Y = value

    def makeHitBox(self):
        hitbox = Rect(self.__HitBox_X, self.__HitBox_Y, self.__HitBox_H, self.__HitBox_W)
        return hitbox
