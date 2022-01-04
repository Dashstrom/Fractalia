from .app import App
import argparse
import random
import sys


def main():
    parser = argparse.ArgumentParser(description="Draw art with fractale")
    parser.add_argument("-s", "--seed", type=int, help="Seed for random generator")
    args = parser.parse_args()

    seed = args.seed if args.seed else random.randint(0, sys.maxsize)
    random.seed(seed)
    print("Seed:", seed)

    app = App()
    app.render()
    app.mainloop()


if __name__ == "__main__":
    main()
