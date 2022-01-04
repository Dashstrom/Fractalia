from .core import (
    ORANGE1,
    ORANGE2,
    ORANGE3,
    ORANGE4
)
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
from .core import (
    RecursiveDraw,
    TreeDraw,
    BarnsleyDraw,
    JuliaDraw,
    MountainsDraw
)

import random


def randpop(a: int, b: int, gap: int, repulsion: int = None) -> list[int]:
    repulsion = repulsion if repulsion else gap
    pop = []
    x = a
    while True:
        x = random.randint(x + gap, x + gap + repulsion)
        if x < b - gap:
            pop.append(x)
        else:
            break
    return pop


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.resizable(width=True, height=True)
        self.title("Fractalia")
        self.configure(bg='white')
        self.can = tk.Canvas(width=800, height=600)
        self.can.pack()
        self.img = Image.new("RGB", (800, 600), (255, 255, 255))
        self._draw_img = ImageDraw.Draw(self.img)
        self._tk_img = None
        self.resizable(False, False)

    def update_draw(self) -> None:
        self._tk_img = ImageTk.PhotoImage(self.img)
        if self._tk_img is not None:
            self.can.delete(self._tk_img)
        self.can.create_image(0, 0, anchor=tk.NW, image=self._tk_img)
        self.update()

    def draw(self, draw: RecursiveDraw) -> None:
        draw.draw(self._draw_img)

    def render(self) -> None:
        print("Render mountains ...")
        base = MountainsDraw(max_iterations=2).points()
        elevation = 50
        colors = [ORANGE1, ORANGE2, ORANGE3, ORANGE4]

        for p1, p2 in zip(base[:-1], base[1:]):
            for i, color in enumerate(colors):
                p1b = (p1[0], p1[1] + i * elevation)
                p2b = (p2[0], p2[1] + i * elevation)
                self.draw(MountainsDraw(p1b, p2b, color=color, vertical_displacement=20))
        print("Render ground ...")
        self.draw(MountainsDraw((0, 550), (800, 580), color=ORANGE1, roughness=0.7, vertical_displacement=20))

        self.draw(TreeDraw(400, 600))
        self.draw(BarnsleyDraw(400, 300))

        print("Render clouds ...")
        for x in randpop(0, 800, gap=100, repulsion=50):
            y = random.randint(50, 150)
            zoom = 10/random.randint(35, 55)
            color = (200 + random.randint(-20, 20),) * 3
            im = random.choice((-1, 1)) * random.randint(5, 15) / 100
            self.draw(JuliaDraw(x, y, zoom, im=im, color=color))


        print("Done")
        self.update_draw()
