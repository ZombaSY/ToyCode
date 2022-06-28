import numpy as np


def game(change_door=True):
    door = [True, False, False]
    index = [0, 1, 2]

    np.random.shuffle(door)
    np.random.shuffle(index)

    door_show = None
    door_closed = None
    door_selected = door[index[0]]

    if door[index[1]] is False:
        door_show = door[index[1]]
        door_closed = door[index[2]]
    else:
        door_show = door[index[2]]
        door_closed = door[index[1]]

    if change_door:
        door_selected = door_closed

    return door_selected


def main():
    game_play_count = 100000
    wins = 0
    for i in range(game_play_count):
        result = game(change_door=False)
        if result:
            wins += 1

    print(f'Acc : {wins / game_play_count}')


if __name__ == '__main__':
    main()
