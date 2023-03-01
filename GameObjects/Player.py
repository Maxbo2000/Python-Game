from GameObjects.MoveableObject import MoveableObject

class Player(MoveableObject):
    def __init__(self, health=int, name=str, walkspeed=float, hitbox_x=int, hitbox_y=int, height=int, width=int, x=int, y=int):
        super().__init__(health, name, walkspeed, hitbox_x, hitbox_y, height, width, x, y)
        sprite: None
        inv: None

