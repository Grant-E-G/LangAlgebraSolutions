"""
Random problem selection

"""
import numpy as np


def main():
    # building our list of problems and subchapers
    data = [[11, 3, 9, 18, 4, 4, 8],
            [12, 7],
            [8, 2, 3, 2, 3, 11],
            [17, 1, 2, 7],
            [34],
            [16, 17, 4, 4, 4, 6],
            [6, 5, 1],
            [10],
            [9, 4, 6],
            [14, 2, 1, 2],
            [4, 9],
            [20],
            [30, 2, 3, 1],
            [12, 14],
            [8, 6, 5, 3, 3, 4],
            [5, 3, 3, 2, 2],
            [8, 7],
            [17, 10],
            [5, 7, 3, 6],
            [13, 5, 10, 2],
            [5]]
    # Data sanity checks
    print("Number of Chapers is " + str(len(data)))
    for chapter in range(len(data)):
        pnumb = 0
        for x in range(len(data[chapter])):
            pnumb += data[chapter][x]
        print("Number of problems in chapter " +
              str(chapter + 1) + " is " + str(pnumb))

    return None


if __name__ == '__main__':
    main()
