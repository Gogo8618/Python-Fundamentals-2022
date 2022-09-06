def swap_func(num, index_func, index1_func):
    num[index_func], num[index1_func] = num[index1_func], num[index_func]
    return num


def multiply_func(num, idx, idx1):
    num[idx] = num[idx] * num[idx1]
    return num


def decrease_func(num):
    for i in range(len(num)):
        num[i] -= 1
    return num


numbers = list(map(int, input().split(' ')))

command = input()

while command != "end":

    data = command.split(" ")
    if data[0] == "swap":
        index = int(data[1])
        index1 = int(data[2])
        numbers = swap_func(numbers, index, index1)
    elif data[0] == "multiply":
        index = int(data[1])
        index1 = int(data[2])
        numbers = multiply_func(numbers, index, index1)
    elif data[0] == "decrease":
        numbers = decrease_func(numbers)
    command = input()
print(', '.join(map(str, numbers)))