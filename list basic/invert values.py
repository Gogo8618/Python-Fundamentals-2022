numbers = input().split(' ')
new_numbers = []
for i in numbers:
    if int(i) > 0:
        new_numbers.append(-int(i))
    else:
        new_numbers.append(abs(int(i)))


print(new_numbers)


