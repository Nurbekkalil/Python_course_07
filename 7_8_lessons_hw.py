plane = [
    ['X',   'X',   'O'], #0
    ['O',   'O',   'O'], #1
    ['O',   'X',   'X'], #2
]


def check_winner(p):
    for i in range(0, 1, 2):
        if i == 0:
            if p[i][0] == p[i + 1] == p[i + 2]:
                return p[i][0]
            elif i == 1:
                if p[1][i] == p[i][1] == p[i + 1][1]:
                    return p[i][0]
            elif i == 2:
                if p[2][i] == p[2][1] == p[2][2]:
                    return p[i][0]


    l = []
    for i in range(3):
        for k in range(3):
            if p[i][k] == "*":
                break
            l.append(p[i][k])

        if l.count("O") == 3 or l.count("X") == 3:
            return l[0]

        l.clear()

    for i in range(0, 3, 2):
        if i == 0:
            if p[i][0] == p[i+1][1] == p[i+2][2]:
                return p[i][0]
            elif i == 2:
                if p[0][i] == p[1][i - 1] == p[2][i - 2]:
                    return p[i][0]

            elif i == 0:
                if p[0][i] == p[1][i + 1] == p[2][i + 2]:
                    return p[i][0]



def input_x_y():
    return int(input('Enter X')) - 1, int(input('Enter Y')) - 1


def print_plane(plane):
    for i in range(3):
        row = plane[i]
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if i != 2:
            print('-' * 9)

# print_plane(plane)
#
# player_1_x, player_1_y = input_x_y()
#
# plane[player_1_x][player_1_y] = 'X'
#
# print_plane(plane)

print(check_winner(plane))


file = open('game_XO.txt', 'w')


file.write(check_winner(plane))