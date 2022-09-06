def sum_numbers(one, two):
    result = one + two
    return result


def sub_result(one, two, third):
    end_result = sum_numbers(one, two) - third
    return end_result


first = int(input())
second = int(input())
three = int(input())

second_end = sub_result(first, second, three)
print(second_end)
