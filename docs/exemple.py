from PIL import ImageDraw, Image
from fractalia import TreeDraw, BarnsleyDraw


img = Image.new("RGBA", (650, 200), (255, 255, 255, 0))
draw_img = ImageDraw.Draw(img)
for i in range(5):
    TreeDraw(i * 125 + 50, 170, i + 1, width=2).draw(draw_img)
    draw_img.text((i * 125 + 36, 175), f"i = {i}", (0, ) * 3)
img.save("docs/tree.png")

img = Image.new("RGBA", (450, 225), (255, 255, 255, 0))
draw_img = ImageDraw.Draw(img)
BarnsleyDraw(75, 205, 2.0, 1000).draw(draw_img)
draw_img.text((50, 210), "i = 1000", (0,) * 3)
BarnsleyDraw(175, 205, 2.0, 5000).draw(draw_img)
draw_img.text((150, 210), "i = 5000", (0,) * 3)
BarnsleyDraw(275, 205, 2.0, 25000).draw(draw_img)
draw_img.text((250, 210), "i = 25000", (0,) * 3)
BarnsleyDraw(375, 205, 2.0, 100000).draw(draw_img)
draw_img.text((350, 210), "i = 100000", (0,) * 3)
img.save("docs/barnsley.png")
