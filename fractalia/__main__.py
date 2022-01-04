from .app import App
import argparse


def main():
    parser = argparse.ArgumentParser(description="Draw art with fractale")
    parser.add_argument("-s", "--seed", type=int, help="Seed for random generator")
    args = parser.parse_args()
    app = App(
        seed=args.seed
    )
    app.render()
    app.mainloop()


if __name__ == "__main__":
    main()
