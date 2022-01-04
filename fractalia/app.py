import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
from numpy.random.mtrand import randint
from fractalia.core.julia import JuliaDraw
from .core import RecursiveDraw, TreeDraw, BarnsleyDraw
import random
import sys


def randpop(a: int, b: int, gap: int, repulsion: int = None, rnd: random.Random = None) -> list[int]:
    repulsion = repulsion if repulsion else gap
    randint = rnd.randint if rnd else random.randint
    pop = []
    x = a
    while True:
        x = randint(x + gap, x + gap + repulsion)
        if x < b - gap:
            pop.append(x)
        else:
            break
    return pop


class App(tk.Tk):

    def __init__(self, seed: int = None):
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
        self.seed = seed if seed else random.randint(0, sys.maxsize)
        self.rnd = random.Random(self.seed)
        print("Seed:", self.seed)

    def update_draw(self) -> None:
        self._tk_img = ImageTk.PhotoImage(self.img)
        if self._tk_img is not None:
            self.can.delete(self._tk_img)
        self.can.create_image(0, 0, anchor=tk.NW, image=self._tk_img)
        self.update()

    def draw(self, draw: RecursiveDraw) -> None:
        draw.draw(self._draw_img)
    
    def render(self) -> None:
        self.draw(TreeDraw(400, 600))
        self.draw(BarnsleyDraw(300, 300))
        
        self.nuages()
        self.update_draw()
    
    def nuages(self) -> None:
        for x in randpop(0, 800, gap=100, repulsion=50, rnd=self.rnd):
            y = self.rnd.randint(50, 150)
            zoom = 10/self.rnd.randint(35, 55)
            color = (200 + self.rnd.randint(-20, 20),) * 3
            im = self.rnd.choice((-1, 1)) * self.rnd.randint(5, 15) / 100
            print(x, y, zoom, color, im)
            self.draw(JuliaDraw(x, y, zoom, im=im, color=color))
        
