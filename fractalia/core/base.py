from abc import ABC, abstractmethod
from typing import Tuple
from dataclasses import dataclass
from PIL.ImageDraw import ImageDraw


Color = Tuple[int, int, int]


class RecusiveDraw(ABC):

    @abstractmethod
    def draw(self, draw: ImageDraw) -> None:
        raise NotImplementedError()


class Coloring(ABC):

    @abstractmethod
    def color(self, i: int, max_i: int) -> Color:
        raise NotImplementedError()


@dataclass
class DegradedColor(Coloring):
    color_start: Color
    color_end: Color
    power: float = 2

    def color(self, i: int, max_i: int) -> Color:
        r0, g0, b0 = self.color_start
        r1, g1, b1 = self.color_end
        a = (i/max_i)**self.power
        b = 1 - a
        return (int(r0 * b + r1 * a),
                int(g0 * b + g1 * a),
                int(b0 * b + b1 * a))
