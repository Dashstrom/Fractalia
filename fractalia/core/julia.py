from dataclasses import dataclass
from typing import Tuple

from PIL import ImageDraw

from .base import DegradedColor, RecursiveDraw


@dataclass
class JuliaDraw(RecursiveDraw):
    x: int = 0
    y: int = 0
    zoom: float = 1
    w: int = 800
    h: int = 600
    re: float = -1.4
    im: float = 0.01
    dX: float = 0.0
    dY: float = 0.0
    max_iterations: int = 255
    color: Tuple[int, int, int] = (200, 200, 200)

    def draw(self, draw: ImageDraw.ImageDraw) -> None:
        # pylint: disable=protected-access

        pix = draw._image.load()
        w, h = draw._image.size

        for x in range(self.w):
            for y in range(self.h):
                zx = (1.5 * (x - self.w / 2)
                      / (0.5 * self.zoom * self.w)
                      + self.dX)
                zy = (1.0 * (y - self.h / 2)
                      / (0.5 * self.zoom * self.h)
                      + self.dY)
                i = self.max_iterations
                while zx * zx + zy * zy < 4 and i > 1:
                    tmp = zx * zx - zy * zy + self.re
                    zy, zx = 2.0 * zx * zy + self.im, tmp
                    i -= 1

                _x = x + self.x - self.w / 2
                _y = y + self.y - self.h / 2

                # convert byte to RGB (3 bytes instead of 1 byte)
                if i < self.max_iterations - 5 and 0 <= _x < w and 0 <= _y < h:
                    coloring = DegradedColor(self.color, pix[_x, _y], 8)
                    draw.point(
                        (_x, _y),
                        coloring.color(i, self.max_iterations)
                    )
