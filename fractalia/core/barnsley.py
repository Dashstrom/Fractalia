from dataclasses import dataclass
from PIL.ImageDraw import ImageDraw
from random import random
import numpy as np

from .base import DegradedColor, RecursiveDraw, Coloring

F1a = np.array([[0, 0],
                [0, .16]])
F1b = np.array([[0],
                [0]])
F1p = 0.01

F2a = np.array([[.85, .04],
                [-.04, .85]])
F2b = np.array([[0],
                [1.6]])
F2p = 0.85

F3a = np.array([[.20, -.26],
                [.23, .22]])
F3b = np.array([[0],
                [1.6]])
F3p = 0.07

F4a = np.array([[-.15, .28],
                [.26, .24]])
F4b = np.array([[0],
                [.44]])
F4p = 0.07


@dataclass
class BarnsleyDraw(RecursiveDraw):
    x: float = 1
    y: float = 1
    size: float = 1
    max_iterations: int = 10000
    coloring: Coloring = DegradedColor((85, 122, 45), (26, 173, 39))

    def draw(self, draw: ImageDraw) -> None:
        sc = np.array([
            [self.x],
            [self.y]
        ])
        v = np.array([[0],
                      [0]])

        points = np.array((self.max_iterations, 2))
        for i in range(self.max_iterations):
            u = random()
            if u < F1p:
                v = np.dot(F1a, v) + F1b
            elif u < F1p + F2p:
                v = np.dot(F2a, v) + F2b
            elif u < F1p + F2p + F3p:
                v = np.dot(F3a, v) + F3b
            else:
                v = np.dot(F4a, v) + F4b
            pts = v * -10 * self.size + sc
            draw.point((pts[0][0], pts[1][0]), self.coloring.color(i, self.max_iterations))
