from GameObjects.MoveableObject import MoveableObject


class Player(MoveableObject):
    super().__init__(100, "test", 1.00, 10, 10)
    sprite: None
    inv: None

    #def walk(self):

