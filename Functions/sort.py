def sort_nums(number):
    number.sort()
    return number


num = list(map(int, input().split(' ')))
result = sort_nums(num)
print(result)
