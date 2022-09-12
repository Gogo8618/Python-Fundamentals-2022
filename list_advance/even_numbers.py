numbers = input().split(", ")
numbers = list(map(int, numbers))
event_list=[]
for n in range (len(numbers)):
    if numbers[n] % 2 == 0:
        event_list.append(n)

print(event_list)
