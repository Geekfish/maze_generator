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
from itertools import cycle
from pprint import pprint
from random import randint, seed

import requests

# new_seed = randint(1, 100)
# print("Seed was:", new_seed)
seed(86)

WALL = "*"
NO_WALL = " "

HORIZONTAL = 1
VERTICAL = 2

MIN_WIDTH = 2


def main():
    chamber_tree = []
    chamber = [
        [
            NO_WALL for _x in range(10)
        ] for _y in range(10)
    ]
    pprint(chamber)

    direction_gen = cycle([HORIZONTAL, VERTICAL])

    chamber = divide(chamber, chamber_tree, direction_gen)
    pprint(chamber)

    chamber = divide(chamber, chamber_tree, direction_gen)
    pprint(chamber)

    # my_list = iter([1,2,3,4,5])
    # print(next(my_list))
    # print(next(my_list))
    # print(next(my_list))
    # print(next(my_list))
    # print(next(my_list))
    # print(next(my_list))
    # print(next(my_list))


def divide(chamber, chamber_tree, direction_gen):
    direction = next(direction_gen)

    if direction == HORIZONTAL:
        line_index = randint(0, len(chamber) - 1)
        line_length = len(chamber[line_index])
    else:
        line_index = randint(0, len(chamber[0]) - 1)
        line_length = len(chamber[0])

    open_passage = randint(0, line_length - 1)

    print(line_index, line_length)

    def get_wall_char(cell_index):
        print(open_passage, cell_index)
        return NO_WALL if cell_index == open_passage else WALL

    if direction == HORIZONTAL:
        chamber[line_index] = list(map(get_wall_char, range(line_length)))
    else:
        new_chamber = []
        for row_index, row in enumerate(chamber):
            new_row = []
            for cell_index, cell in enumerate(row):
                new_cell = " "
                if cell_index == line_index:
                    new_cell = get_wall_char(row_index)
                new_row.append(new_cell)
            new_chamber.append(new_row)
        chamber = new_chamber


    # sub_chamber = chamber[:x-1]

    return chamber




if __name__ == '__main__':
    main()
