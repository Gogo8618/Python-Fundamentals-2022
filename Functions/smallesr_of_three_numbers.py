def smallest_number(one, two, three):
    result = 0
    if one < two and one < three:
        result = one
    elif two < one and two < three:
        result = two
    elif three < one and three < two:
        result = three
    return result


first = int(input())
second = int(input())
thirth = int(input())

end_result = smallest_number(first, second, thirth)
print(end_result)
