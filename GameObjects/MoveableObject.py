from pygame import Rect


class MoveableObject:
    def __init__(self, health, name, walkspeed, x, y):
        self.__Health = health
        self.__Name = name
        self.__WalkSpeed = walkspeed
        self.__Pos_X = x
        self.__Pos_Y = y

    __Health: int
    __Name: str
    __WalkSpeed: int
    __Pos_X: int
    __Pos_Y: int
    __HitBox: Rect

    #Getter
    def getHealth(self): return self.__Health
    def getName(self): return self.__Name
    def getWalkSpeed(self): return self.__WalkSpeed
    def getPosX(self): return self.__Pos_X
    def getPosY(self): return self.__Pos_Y
    def getHitbox(self): return self.__HitBox

    #Setter
    def setHealth(self, value:int): self.__Health = value
    def setName(self, value:str): self.__Name = value
    def setWalkSpeed(self, value:int): self.__WalkSpeed = value
    def setPosX(self, value:int): self.__Pos_X = value
    def setPosY(self, value:int): self.__Pos_Y = value
    def setHitbox(self,value:Rect): self.__HitBox = value
