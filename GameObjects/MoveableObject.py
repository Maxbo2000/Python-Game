
class MoveableObject:
    def __init__(self, health, name, walkspeed, hitbox_x, hitbox_y):
        self.__Health = health
        self.__Name = name
        self.__WalkSpeed = walkspeed
        self.__HitBox_X = hitbox_x
        self.__HitBox_Y = hitbox_y

    __Health: int
    __Name: str
    __WalkSpeed: float
    __HitBox_X: int
    __HitBox_Y: int

