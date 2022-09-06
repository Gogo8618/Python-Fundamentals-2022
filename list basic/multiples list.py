factor = int(input())
count = int(input())
numbers = []
for num in range(1, count + 1):
    result = factor * num
    numbers.append(result)
print(numbers)
