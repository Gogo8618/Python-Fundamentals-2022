numbers = list(map(int, input().split(", ")))

border = 10

while True:

    if len(numbers) == 0:
        break

    current_list = [num for num in numbers if num <= border]
    for y in current_list:
        numbers.remove(y)
    print(f"Group of {border}'s: {current_list}")
    border += 10