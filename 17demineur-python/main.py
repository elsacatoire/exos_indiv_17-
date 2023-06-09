import random
import itertools


def generate_grid(rows, columns):
    grid = [['#' for _ in range(columns)] for _ in range(rows)]
    return grid


def get_random_char(grid_char):
    """
    take an array and gives a random character
    :param grid_char: the array giving the possible characters
    :return: a character
    """
    random_char = random.choice(grid_char)
    return random_char


def create_bomb_coordinates(grid_rows, grid_columns, bombs_nb):
    all_positions = list(itertools.product(range(grid_columns), range(grid_rows)))
    array_of_bombs = random.sample(all_positions, bombs_nb)
    return array_of_bombs


def grid_generator(rows, columns, bombs):
    """
    generate a grid to play bomb squad

    :param rows: number of lines
    :param columns: number of columns
    :param bombs: number of bombs
    :return: a grid
    """
    grid = []
    bombs_coordinates = []
    # manufacturing some bombs...
    for b in range(bombs):
        bombs_coordinates.append(create_bomb_coordinates(rows, columns))
    print(f"bombs coordinate : {bombs_coordinates}")

    # creating the grid
    for c in range(columns):
        line = []
        safe_box = "0"
        bomb_box = "X"
        # line by line
        for r in range(rows):
            instant_coordinate = [r, c]
            if instant_coordinate not in bombs_coordinates:
                line.append(safe_box)
            else:
                line.append(bomb_box)
        print(line)
        grid.append(line)
    return grid


def game_play(nb_of_rows, nb_of_columns, bomb_quantity):
    # setting the board game
    generate_grid(nb_of_rows, nb_of_columns)
    # generate the bombs, tik...tak...
    print(create_bomb_coordinates(nb_of_rows, nb_of_columns, bomb_quantity))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_play(5, 5, 3)
    print(generate_grid(3, 3))
    # grid_generator(3,5,3)

