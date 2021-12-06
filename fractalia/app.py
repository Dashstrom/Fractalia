import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

from .core import RecusiveDraw, TreeDraw, BarnsleyDraw


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
        # self.draw(TreeDraw(400, 600))
        # self.draw(BarnsleyDraw(400, 300))
        self.update_draw()
