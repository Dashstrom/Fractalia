from random import choice
from bisect import insort
from dataclasses import dataclass
from PIL import Image, ImageDraw
from .base import DegradedColor, RecursiveDraw, Coloring

@dataclass
class MountainsDraw(RecursiveDraw):
    start: tuple = (0, 300)
    end: tuple = (800, 300)
    roughness: int = 1
    vertical_displacement: int = 100
    max_iterations: int = 10
    width: int = 4
    color: tuple = (255, 0, 0)
    _points: list[tuple] = None

    def draw(self, draw: ImageDraw) -> None:
        terrain_points = self.points
        # Insertion of the bottom-left and right corners in order to draw
        # a full shape
        terrain_points.insert(0, (self.start[0], 2000))
        terrain_points.insert(len(terrain_points), (self.end[0], 2000))
        draw.polygon(
            terrain_points,
            fill=self.color
        )
    
    @property
    def points(self) -> list[tuple]:
        """Applies the midpoint displacement algorithm and returns points"""
        
        if self._points is not None:
            return self._points
            
        if self.vertical_displacement is None:
            self.vertical_displacement = (self.start[1] + self.end[1]) / 2
        
        terrain_points = [self.start, self.end]
        iteration = 1
        while iteration <= self.max_iterations:
            init_line = tuple(terrain_points)

            for i in range(len(init_line)-1):
                #Finds the middle point of the segment
                line_middle = lambda x: (init_line[i][x]+init_line[i+1][x])/2
                midpoint = list(map(line_middle, [0, 1]))
                #Applies the vertical displacement
                midpoint[1] += choice([
                    -self.vertical_displacement,
                    self.vertical_displacement]
                )
                #Inserts in the list and keeps the order
                insort(terrain_points, tuple(midpoint))
            self.vertical_displacement *= 2 ** (-self.roughness)
            iteration += 1
        self._points = terrain_points
        return self._points
