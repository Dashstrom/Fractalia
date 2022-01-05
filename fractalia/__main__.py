import argparse
from os import makedirs
import random
import sys

from tqdm import trange

from .drawing import drawing

from .app import App


def main():
    parser = argparse.ArgumentParser(description="Draw art with fractale")
    parser.add_argument("-s", "--seed", type=int,
                        help="Seed for random generator")
    parser.add_argument("-n", "--number", type=int,
                        help="Generate N images in directory named 'out'")
    args = parser.parse_args()

    seed = args.seed if args.seed else random.randint(0, sys.maxsize)
    random.seed(seed)
    print("Seed:", seed)

    if args.number is None:
        app = App()
        app.mainloop()
    else:
        makedirs("out", exist_ok=True)
        for _ in trange(abs(args.number)):
            img = drawing()
            img.save(f"out/{seed}.png")
            seed = random.randint(0, sys.maxsize)
            random.seed(seed)


if __name__ == "__main__":
    main()
