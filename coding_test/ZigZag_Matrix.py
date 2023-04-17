"""
      1  2  3  4  5
  ------------------
  1 | 1  2  6  7  15
  2 | 3  5  8  14 16
  3 | 4  9  13 17 22
  4 | 10 12 18 21 23
  5 | 11 19 20 24 25

index가 지그재그로 되어있는 n크기의 행렬에서
좌표 (r, c)의 값 찾기
!!(1, 1)부터 시작!!

"""


def solution(n, r, c):
    find_row = r + c - 1
    if find_row <= n:
        find_col = r
    else:
        find_col = r - (find_row - n)

    array = [1]
    sum_i = 1
    j = 1

    for i in range(1, 2 * n - 1):
        if i < n:
            sum_i += i
            j += 1
        else:
            sum_i += j
            j -= 1
        array.append(sum_i)

        if i > find_row:
            break

    if find_row % 2 == 0:
        answer = (array[find_row] - 1) - (find_col - 1)  # reversed
    else:
        answer = array[find_row - 1] + (find_col - 1)

    return answer


import time
tt = time.time()
print(solution(10000000, 10000000, 10000000))
print(time.time() - tt)
