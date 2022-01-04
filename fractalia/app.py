from random import randint
from .core import (
    ORANGE1,
    ORANGE2,
    ORANGE3,
    ORANGE4
)
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
from .core import (
    RecusiveDraw,
    TreeDraw,
    BarnsleyDraw,
    JuliaDraw,
    MountainsDraw
)


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.resizable(width=True, height=True)
        self.title("Fractalia")
        self.configure(bg='white')
        self.can = tk.Canvas(width=800, height=600)
        self.can.pack()
        self.img = Image.new("RGB", (800, 600), "white")
        self._draw_img = ImageDraw.Draw(self.img)
        self._tk_img = None
        self.resizable(False, False)

    def update_draw(self) -> None:
        self._tk_img = ImageTk.PhotoImage(self.img)
        if self._tk_img is not None:
            self.can.delete(self._tk_img)
        self.can.create_image(0, 0, anchor=tk.NW, image=self._tk_img)
        self.update()

    def draw(self, draw: RecusiveDraw) -> None:
        draw.draw(self._draw_img)

    def render(self) -> None:
        
        base = MountainsDraw(max_iterations=2).points()

        def randcolor():
            return (randint(0,255), randint(0,255), randint(0,255))

        elevation = 50
        colors = [ORANGE1, ORANGE2, ORANGE3, ORANGE4]

        for p1, p2 in zip(base[:-1], base[1:]):    
            for i, color in enumerate(colors):
                p1b = (p1[0], p1[1] + i*elevation)
                p2b = (p2[0], p2[1] + i*elevation)
                self.draw(MountainsDraw(p1b, p2b, color=color, vertical_displacement=20))
        self.draw(MountainsDraw((0, 550), (800, 580), color=ORANGE1, roughness=0.7, vertical_displacement=20))
        
        self.draw(TreeDraw(400, 600))
        self.draw(BarnsleyDraw(400, 300))
        self.draw(JuliaDraw(zoom = 1))

        self.update_draw()
