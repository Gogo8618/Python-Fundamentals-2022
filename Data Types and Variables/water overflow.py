n = int(input())
tank = 0
for i in range(n):
    liters_of_water = int(input())
    if tank + liters_of_water > 255:
        print("Insufficient capacity!")
        continue
    tank += liters_of_water
print(tank)

