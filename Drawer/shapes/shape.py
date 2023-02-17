from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x, y):
        self.x, self.y = x, y

    @abstractmethod
    def draw(self, size, color, thickness):
        pass
