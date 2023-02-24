from abc import ABCMeta, abstractmethod


class MoveableObject(metaclass=ABCMeta):
    def __init__(self): pass

    @property
    @abstractmethod
    def __Health(self): pass

    @property
    @abstractmethod
    def __Name(self): pass

    @property
    @abstractmethod
    def __WalkSpeed(self): pass

    @property
    @abstractmethod
    def __HitBox_X(self): pass

    @property
    @abstractmethod
    def __HitBox_Y(self): pass
