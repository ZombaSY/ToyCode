def solution(m, n, board):

    answer = 0

    is_destroyed = True
    list_board = []

    # convert to 2dim matrix
    for i in range(m):
        list_board.append([])
        for j in range(n):
            list_board[i].append(board[i][j])

    while is_destroyed:
        check_board = []

        # initialize check block
        for i in range(m):
            check_board.append([])
            for j in range(n):
                check_board[i].append(False)

        is_destroyed = False

        # check blocks
        for i in range(m - 1):
            for j in range(n - 1):
                char = list_board[i][j]
                if char != '0':
                    if (char == list_board[i+1][j]) & (char == list_board[i][j+1]) & (char == list_board[i+1][j+1]):
                        answer += 4
                        is_destroyed = True
                        if check_board[i][j]:
                            answer -= 1
                        if check_board[i+1][j]:
                            answer -= 1
                        if check_board[i][j+1]:
                            answer -= 1
                        if check_board[i+1][j+1]:
                            answer -= 1

                        check_board[i][j] = True
                        check_board[i+1][j] = True
                        check_board[i][j+1] = True
                        check_board[i+1][j+1] = True

        # push board using check_board
        for i in reversed(range(m)):
            for j in range(n):
                if check_board[i][j]:
                    temp2 = True
                    temp = i

                    while temp2:
                        if temp == -1:
                            break
                        if check_board[temp][j]:
                            break
                        temp -= 1

                    if temp >= 0:
                        list_board[i][j] = list_board[temp][j]
                        list_board[temp][j] = '0'
                        check_board[temp][j] = True
                    else:
                        check_board[i][j] = True
                        list_board[i][j] = '0'

        del check_board

    print(answer)

    return answer


def main():
    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

    solution(m, n, board)


if __name__ == "__main__":
    main()

# Maid Bie SunYong
