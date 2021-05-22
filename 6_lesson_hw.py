plane = [
    ['*'],   ['*'],   ['*'],
    ['*'],   ['*'],   ['*'],
    ['*'],   ['*'],   ['*'],
]


def check_winner(p):
    for i in range(3):
        row = plane[i]
        start = ""
        for k in row:
            if k == "*":
                break
            if not start:
                start = k
            else:
                if start == k:


def input_x_y():
    return int(input('Enter X')) - 1, int(input('Enter Y')) - 1


def print_plane(plane):
    for i in range(3):
        row = plane[i]
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if i != 2:
            print('-' * 9)

print_plane(plane)

player_1_x, player_1_y = input_x_y()

plane[player_1_x][player_1_y] = 'X'

print_plane(plane)