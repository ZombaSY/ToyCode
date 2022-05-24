from time import time


def ant_matrix(len_arr):
    start = time()
    prev_arr = [1]
    print(prev_arr)
    for i in range(1, len_arr):
        current_arr = []
        prev_index = 0
        prev_num = 0
        flg = True
        prev_arr_len = len(prev_arr)
        while(flg):
            count = 0
            prev_num = prev_arr[prev_index]
            current_arr.append(prev_num)
            while True:
                if prev_index == prev_arr_len:
                    flg = False
                    break
                elif prev_arr[prev_index] == prev_num:
                    count += 1
                    prev_index += 1
                else:
                    break
            current_arr.append(count)
        print(current_arr)
        prev_arr = current_arr
    print("Elapsed Time : ", time()-start)


def main():
    input_len = int(input("Length of Matrix : "))
    ant_matrix(input_len)


if __name__ == "__main__":
    main()

# Maid Bie SunYong
