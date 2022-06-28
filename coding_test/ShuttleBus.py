"""""
셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m, 크루가 대기열에 도착하는 시각을 모은 배열 timetable이 입력으로 주어진다.

0 ＜ n ≦ 10
0 ＜ t ≦ 60
0 ＜ m ≦ 45
timetable은 최소 길이 1이고 최대 길이 2000인 배열로, 하루 동안 크루가 대기열에 도착하는 시각이 HH:MM 형식으로 이루어져 있다.
크루의 도착 시각 HH:MM은 00:01에서 23:59 사이이다.

"""


def parse_to_int(a):
    a = a.replace(':', '')
    parsed_str = int(a)
    return parsed_str


def parse_to_str(a):

    hour_time = int(a / 100)
    min_time = int(a % 100)

    if min_time > 60:
        min_time = min_time - 60
        hour_time += 1

    if hour_time < 10:
        str_hour_time = '0' + str(hour_time)
    else:
        str_hour_time = str(hour_time)
    if min_time < 10:
        str_min_time = '0' + str(min_time)
    else:
        str_min_time = str(min_time)

    parsed_int = str_hour_time + ':' + str_min_time

    return parsed_int


def solution(n, t, m, timetable):

    answer = ''

    if n > 1:
        hour_time = int( (n-1) * t / 60)
        min_time = (n-1) * t % 60

        hour_time = 9 + hour_time
        if hour_time < 10:
            str_hour_time = '0' + str(hour_time)
        else:
            str_hour_time = str(hour_time)
        if min_time < 10:
            str_min_time = '0' + str(min_time)
        else:
            str_min_time = str(min_time)

        last_bus_time = str_hour_time + ':' + str_min_time
    else:
        last_bus_time = "09:00"

    timetable.sort()
    current_bus_time = "09:00"
    last_remain = False
    for i in range(n):
        if i == (n - 1):
            for j in range(m - 1):
                if timetable[0] <= current_bus_time:
                    del timetable[0]
                    if m >= len(timetable):
                        last_remain = True
        else:
            for j in range(m):
                if timetable[0] <= current_bus_time:
                    del timetable[0]
                    if timetable[0] == current_bus_time:
                        break

        current_bus_time = parse_to_int(current_bus_time)

        hour_time = int(current_bus_time / 100)
        min_time_bus = int(current_bus_time % 100)
        min_time_bus = min_time_bus + t
        if min_time_bus >= 60:
            hour_time += 1
            min_time_bus = min_time_bus - 60
        next_bus_time = hour_time*100 + min_time_bus

        current_bus_time = parse_to_str(next_bus_time)

    timetable.append(last_bus_time)
    timetable.sort()

    count = 0
    temp = len(timetable)
    for i in range(1, temp):
        count += 1
        if timetable[count] > last_bus_time:
            del timetable[count]
            count -= 1

    if(timetable[0] == last_bus_time) & (len(timetable) == 1):
        answer = timetable[0]
    elif (last_remain == True) & (m <= len(timetable)):
        timetable[0] = parse_to_int(timetable[0])
        timetable[0] = timetable[0] - 1

        hour_time = int(timetable[0] / 100)
        min_time = int(timetable[0] % 100)

        if min_time == 99:
            min_time = 59
        if hour_time < 10:
            str_hour_time = '0' + str(hour_time)
        else:
            str_hour_time = str(hour_time)
        if min_time < 10:
            str_min_time = '0' + str(min_time)
        else:
            str_min_time = str(min_time)

        answer = str_hour_time + ':' + str_min_time
    else:
        timetable[0] = parse_to_int(timetable[0])

        timetable[0] = 0
        timetable[0] = timetable[0] - 1

        hour_time = int(timetable[0] / 100)
        min_time = int(timetable[0] % 100)

        if min_time == 99:
            min_time = 59
        if hour_time < 10:
            str_hour_time = '0' + str(hour_time)
        else:
            str_hour_time = str(hour_time)
        if min_time < 10:
            str_min_time = '0' + str(min_time)
        else:
            str_min_time = str(min_time)

        answer = str_hour_time + ':' + str_min_time

    return answer


def main():
    # n = 1
    # t = 1
    # m = 5
    # timetable = ["08:00", "08:01", "08:02", "08:03"]

    n = 2
    t = 1
    m = 2
    timetable = ["09:00", "09:00", "09:00", "09:00"]

    # n = 2
    # t = 10
    # m = 2
    # timetable = ["09:10", "09:09", "08:00"]

    # n = 10
    # t = 60
    # m = 1
    # timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
    #              "23:59", "23:59", "23:59", "23:59", "23:59"]

    n = 1
    t = 1
    m = 1
    timetable = ["00:01"]

    # n = 5
    # t = 1
    # m = 1
    # timetable = ["09:00", "09:01", "09:02", "09:03", "09:04"]

    # n = 1
    # t = 1
    # m = 1
    # timetable = []

    # n = 1
    # t = 1
    # m = 5
    # timetable = ["00:01", "00:01","00:01","00:01","00:01"]

    answer = solution(n, t, m, timetable)

    print(answer)


if __name__ == "__main__":
    main()

# Maid Bie SunYong
