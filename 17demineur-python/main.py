import random
#function for python bomb squad


# il faut créer une grille neutre de A et quand on entre une coordonnée ça révèle la case

#

def get_random_char(grid_char):
    """
    take an array and gives a random character
    :param grid_char: the array giving the possibible charachters
    :return: a character
    """
    random_char = random.choice(grid_char)
    return random_char


def create_bomb_cordonates(grid_rows, grid_columns):
    """
    :param grid_rows:
    :param grid_columns:
    :return:
    """
    x_position = random.randrange(0,grid_columns)
    y_position = random.randrange(0, grid_rows)
    bomb_x_y = []
    bomb_x_y.append(x_position)
    bomb_x_y.append(y_position)
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
    bombs_coordonates = []
    # manufacturing some bombs...
    for b in range(K):
        bombs_coordonates.append(create_bomb_cordonates(R, C))
    print(f"bombs coordonate : {bombs_coordonates}")

    # creating the grid
    for c in range(C):
        line = []
        safe_box = "0"
        bomb_box = "X"
        # line by line
        for r in range(R):
            intstant_coordonate = [r, c]
            if(not intstant_coordonate in bombs_coordonates):
                line.append(safe_box)
            else:
                line.append(bomb_box)
        print(line)
        grid.append(line)
    return grid


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid_generator(5,5,5)

