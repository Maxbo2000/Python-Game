from abc import ABCMeta, abstractmethod


class MoveableObject(metaclass=ABCMeta):
    def __init__(self): pass

    @property
    @abstractmethod
    def _Health(self): pass

    @property
    @abstractmethod
    def _Name(self): pass

    @property
    @abstractmethod
    def _WalkSpeed(self): pass

    @property
    @abstractmethod
    def _HitBox_X(self): pass

    @property
    @abstractmethod
    def _HitBox_Y(self): pass
