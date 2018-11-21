from pprint import pprint
from random import choice


def main():
    for x in range(10):
    grid = [
        [
            choice(["*", " "]) for _x in range(10)
        ] for _y in range(10)
    ]
    pprint(grid)


if __name__ == '__main__':
    main()
