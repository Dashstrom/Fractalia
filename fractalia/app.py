import sys
import random
import tkinter as tk

from PIL import ImageDraw, ImageTk
from .drawing import gen_new_gradient_bg
from .drawing import drawing


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.resizable(width=True, height=True)
        self.title("Fractalia")
        self.configure(bg='white')
        self.can = tk.Canvas(self, width=800, height=600)
        self.can.pack()
        self.btn = tk.Button(self, text="Relancer", command=self.redraw)
        self.btn.pack(side=tk.BOTTOM)
        self.img = gen_new_gradient_bg()
        self._draw_img = ImageDraw.Draw(self.img)
        self._tk_img = None
        self.resizable(False, False)
        self.render()

    def redraw(self):
        seed = random.randint(0, sys.maxsize)
        random.seed(seed)
        print("Seed:", seed)
        self.render()

    def render(self) -> None:
        self.img = drawing()
        self._tk_img = ImageTk.PhotoImage(self.img)
        if self._tk_img is not None:
            self.can.delete(self._tk_img)  # type: ignore
        self.can.create_image(0, 0, anchor=tk.NW, image=self._tk_img)
        self.update()
