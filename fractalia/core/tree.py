from math import pi, cos, sin
from dataclasses import dataclass
from PIL.ImageDraw import ImageDraw

from .base import DegradedColor, RecursiveDraw, Coloring


@dataclass
class TreeDraw(RecursiveDraw):
    x: float = 1
    y: float = 1
    max_iterations: int = 8
    theta: float = pi/2
    gap: float = pi/10
    branch: int = 3
    length: int = 50
    ratio: float = 3/4
    width: int = 1
    coloring: Coloring = DegradedColor((112, 86, 64), (63, 161, 56))

    def draw(self, draw: ImageDraw) -> None:
        self._draw_recursive(draw, self.x, self.y, 0, self.theta, self.length)

    def _draw_recursive(self, draw: ImageDraw, x: float, y: float,
                        i: int, theta: float, length: float) -> None:
        if self.max_iterations <= i:
            return
        x1, y1 = x - length * cos(theta), y - length * sin(theta)
        draw.line(
            ((x, y), (x1, y1)),
            fill=self.coloring.color(i, self.max_iterations),
            width=self.width
        )
        for b in range(self.branch):
            theta_branch = theta - (self.gap * ((self.branch-1)/2 - b))
            self._draw_recursive(draw=draw, x=x1, y=y1, i=i+1,
                                 theta=theta_branch, length=length*self.ratio)
