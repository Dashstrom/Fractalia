from dataclasses import dataclass
from PIL.ImageDraw import ImageDraw
from .base import DegradedColor, RecusiveDraw, Coloring

@dataclass
class JuliaDraw(RecusiveDraw):
    w: float = 800
    h: float = 600
    zoom: int = 1
    max_iterations = 10
    re: float = -1.4
    im: float = 0.01
    dX: float = 0.0
    dY: float = 0.0
    max_iterations: int = 255
    color: Coloring = DegradedColor((111, 111, 111), (200, 200, 200))

    def draw(self, draw: ImageDraw) -> None:
    
        for x in range(self.w):
            for y in range(self.h):
                zx = 1.5*(x - self.w/2)/(0.5*self.zoom*self.w) + self.dX
                zy = 1.0*(y - self.h/2)/(0.5*self.zoom*self.h) + self.dY
                i = self.max_iterations
                while zx*zx + zy*zy < 4 and i > 1:
                    tmp = zx*zx - zy*zy + self.re
                    zy,zx = 2.0*zx*zy + self.im, tmp
                    i -= 1
    
                # convert byte to RGB (3 bytes instead of 1 byte)
                if i != self.max_iterations-1 and i < self.max_iterations-6:
                    draw.point(
                        (x, y),
                        self.color.color(i, self.max_iterations)
                    )
    