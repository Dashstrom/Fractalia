# pylint: disable=import-outside-toplevel
import argparse
from os import makedirs
import random
import sys


def main():
    parser = argparse.ArgumentParser(
        description=("Tkinter application for generate landscapes "
                     "composed of fractals.")
    )
    parser.add_argument("-s", "--seed", type=int,
                        help="Seed for random generator")
    parser.add_argument("-n", "--number", type=int,
                        help="Generate N images in directory named 'out'")
    args = parser.parse_args()

    seed = args.seed if args.seed else random.randint(0, sys.maxsize)
    random.seed(seed)
    print("Seed:", seed)

    if args.number is None:
        from .app import App

        app = App()
        app.mainloop()
    else:
        from tqdm import trange
        from .drawing import drawing

        makedirs("out", exist_ok=True)
        for _ in trange(abs(args.number)):
            img = drawing()
            img.save(f"out/{seed}.png")
            seed = random.randint(0, sys.maxsize)
            random.seed(seed)


if __name__ == "__main__":
    main()
