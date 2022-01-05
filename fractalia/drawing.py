import random

from PIL import Image, ImageDraw

from .core import (
    TreeDraw,
    BarnsleyDraw,
    JuliaDraw,
    MountainsDraw,
    ORANGES,
    SORBUS
)


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


def randsign() -> int:
    return random.choice((-1, 1))


def drawing() -> Image.Image:
    img = Image.new("RGB", (800, 600), (114, 155, 242))
    draw_img = ImageDraw.Draw(img)

    base = MountainsDraw(max_iterations=2).points
    elevation = 50
    for p1, p2 in zip(base[:-1], base[1:]):
        for i, color in enumerate(ORANGES):
            p1b = (p1[0], p1[1] + i * elevation)
            p2b = (p2[0], p2[1] + i * elevation)
            MountainsDraw(p1b, p2b, color=color,
                          vertical_displacement=20).draw(draw_img)
    ground = MountainsDraw((0, 550), (800, 580), color=SORBUS,
                           roughness=0.7, vertical_displacement=20)
    ground.draw(draw_img)
    points = ground.points

    indexs = randpop(0, len(points), gap=100, repulsion=75)
    random.shuffle(indexs)
    for i in indexs:
        p = points[i]
        size = random.randint(4, 6) / 10
        if random.randint(0, 5) <= 1:
            i2 = i + randsign() * random.randint(25, 35)
            p2 = points[i2]
            BarnsleyDraw(p2[0], p2[1], size=size - 0.2).draw(draw_img)
        BarnsleyDraw(p[0], p[1], size=size).draw(draw_img)

    indexs = randpop(0, len(points), gap=150, repulsion=50)
    random.shuffle(indexs)
    for i in indexs:
        p = points[i]
        TreeDraw(p[0], p[1], length=random.randint(25, 40),
                 width=random.randint(1, 2)).draw(draw_img)

    for x in randpop(0, 800, gap=100, repulsion=50):
        y = random.randint(50, 150)
        zoom = 10/random.randint(35, 55)
        color = (200 + random.randint(-20, 20),) * 3  # type: ignore
        im = randsign() * random.randint(5, 15) / 100
        JuliaDraw(x, y, zoom, im=im, color=color).draw(draw_img)
    return img
