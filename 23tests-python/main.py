

import random


def place_random_bombe(nb_bombs, nb_columns, nb_lines):
    for i in range(nb_bombs):
        x = random.randint(0, nb_columns - 1)
        y = random.randint(0, nb_lines - 1)
        grid[y][x] = 'X'


def grid_generator(n, m, char):
    array = [[char for column in range(n)] for line in range(m)]
    print(array)
    return array


def display_grid(grid_to_display):
    for row in grid_to_display:
        print("  ".join(str(cell) for cell in row))
        print("")


def case(x, y):
    if 0 <= x < len(grid):
        if 0 <= y < len(grid[x]):
            playerGrid[y][x] = grid[y][x]
        else:
            print("Out of the grid! Play again")
    else:
        print("Out of the grid! Play again")


if __name__ == "__main__":
    columns = 5
    lines = 10
    grid = grid_generator(columns, lines, 0)
    playerGrid = grid_generator(columns, lines, "-")

    place_random_bombe(1, columns, lines)

    while True:
        print("Enter coordinates to open a case")
        coordinateX = input("Enter x between 1 to " + str(columns) + " : ")
        coordinateY = input("Enter y between 1 to " + str(lines) + " : ")

        case(int(coordinateX)-1, int(coordinateY)-1)
        display_grid(playerGrid)
