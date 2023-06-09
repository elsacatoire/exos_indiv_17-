import random
import itertools


def generate_grid(rows, columns):
    grid = [['#' for _ in range(columns)] for _ in range(rows)]
    return grid


def create_bomb_coordinates(grid_rows, grid_columns, bombs_nb):
    all_positions = list(itertools.product(range(grid_columns), range(grid_rows)))
    array_of_bombs = random.sample(all_positions, bombs_nb)
    return array_of_bombs


def game_play(nb_of_rows, nb_of_columns, bomb_quantity):
    # setting the board game
    print(generate_grid(nb_of_rows, nb_of_columns))
    # generate the bombs, tik...tak...
    bombs = create_bomb_coordinates(nb_of_rows, nb_of_columns, bomb_quantity)
    print(bombs)
    explosion = False
    while not explosion:
        give_me_x = input("column nb")
        give_me_y = input("line nb")
        box_played = (int(give_me_x), int(give_me_y))
        print(box_played)
        if box_played in bombs:
            print("EXPLOSION")
            explosion = True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_play(5, 5, 3)
    # grid_generator(3,5,3)
