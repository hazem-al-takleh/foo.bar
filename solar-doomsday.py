from math import floor, sqrt

def solution(area):
    squared_nums_list = list()
    for num in range(floor(sqrt(area)), 0, -1):
        squared_nums_list.append(num*num)

    solution_list = list()
    i = True
    while (True):
        if area == 0:
            break

        # if squared_nums_list empty
        if not squared_nums_list:
            solution_list.append(1)
            # solution_list = solution_list + ",1"
            area = area - 1
            continue

        greatest_squared_num = squared_nums_list[0]
        if area >= greatest_squared_num:
            solution_list.append(greatest_squared_num)
            area = area - greatest_squared_num
        squared_nums_list.pop(0)

    return solution_list


if __name__ == "__main__":
    var = solution(12)
    print(var)

