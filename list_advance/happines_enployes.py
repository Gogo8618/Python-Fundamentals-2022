numbers = input().split(" ")
happines_factor = int(input())

numbers = list(map(lambda x: int(x)*happines_factor, numbers))

filt = list(filter(lambda x: x >= (sum(numbers) / len(numbers)), numbers))

if len(filt) >= len(numbers) / 2:
    print(f"Score: {len(filt)}/{len(numbers)}. Employees are happy!")

else:
    print(f"Score: {len(filt)}/{len(numbers)}. Employees are not happy!")