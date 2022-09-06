numbers = [int(x) for x in input().split(', ')]
beggars = int(input())

beggars_count = [0] * beggars
count = 0
for num in numbers:
    beggars_count[count] += num
    count += 1
    if count >= beggars:
        count = 0
print(beggars_count)

