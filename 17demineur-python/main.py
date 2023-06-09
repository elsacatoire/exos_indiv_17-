import random

# il faut créer une grille neutre de A et quand on entre une coordonnée ça révèle la case


def generate_grid(rows, columns):
    grid = []
    for c in range(columns):
        line = []
        for r in range(rows):
            line.append("#")
        print(line)
        grid.append(line)
    return grid


def get_random_char(grid_char):
    """
    take an array and gives a random character
    :param grid_char: the array giving the possibible charachters
    :return: a character
    """
    random_char = random.choice(grid_char)
    return random_char


def create_bomb_coordinates(grid_rows, grid_columns):
    """
    :param grid_rows:
    :param grid_columns:
    :return:
    """
    x_position = random.randrange(0, grid_columns)
    y_position = random.randrange(0, grid_rows)
    bomb_x_y = [x_position, y_position]
    return bomb_x_y


def grid_generator(R, C, K):
    """
    geenarte a grid to play bomb squad

    :param R: number of lines
    :param C: number of columns
    :param K: number of bombs
    :return: a grid
    """
    grid = []
    bombs_coordinates = []
    # manufacturing some bombs...
    for b in range(K):
        bombs_coordinates.append(create_bomb_coordinates(R, C))
    print(f"bombs coordinate : {bombs_coordinates}")

    # creating the grid
    for c in range(C):
        line = []
        safe_box = "0"
        bomb_box = "X"
        # line by line
        for r in range(R):
            instant_coordinate = [r, c]
            if not instant_coordinate in bombs_coordinates:
                line.append(safe_box)
            else:
                line.append(bomb_box)
        print(line)
        grid.append(line)
    return grid


def game_play(nb_of_rows, nb_of_columns, nb_of_bombs):
    # setting the board game
    generate_grid(nb_of_rows, nb_of_columns)
    # generate the bombs, tik...tak...
    for b in range(nb_of_bombs):
        print(create_bomb_coordinates(nb_of_rows, nb_of_columns))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     game_play(5, 5, 3)


