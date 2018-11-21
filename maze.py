"""
Mazes can be created with recursive division, an algorithm which works as follows:
Begin with the maze's space with no walls. Call this a chamber.

----

Divide the chamber with a randomly positioned wall (or multiple walls)
where each wall contains a randomly positioned passage opening within it.

Then recursively repeat the process on the subchambers until all chambers are minimum sized.
This method results in mazes with long straight walls crossing their space,
making it easier to see which areas to avoid.

Recursive Maze generation

For example, in a rectangular maze, build at random points two walls that are
perpendicular to each other. These two walls divide the large chamber into four
smaller chambers separated by four walls. Choose three of the four walls at random,
and open a one cell-wide hole at a random point in each of the three.

Continue in this manner recursively, until every chamber has a width of one cell in either of the two directions.
"""
from pprint import pprint
from random import randint

WALL = "*"
NO_WALL = " "

MIN_WIDTH = 2


def main():
    chamber = [
        [
            NO_WALL for _x in range(10)
        ] for _y in range(10)
    ]
    pprint(chamber)

    chamber = divide(chamber)
    pprint(chamber)


def divide(chamber):
    x = randint(0, len(chamber))
    line = chamber[x]

    open_passage = randint(0, len(line))

    def get_wall_char(cell_index):
        return NO_WALL if cell_index == open_passage else WALL

    chamber[x] = list(map(get_wall_char, range(len(line))))

    return chamber




if __name__ == '__main__':
    main()
