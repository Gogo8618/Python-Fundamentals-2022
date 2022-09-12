def houses_targets(houses, position):

    houses[position] -= 2
    if houses[position] <= -2:
        print(f"Place {hposition} already had  Valentine's day")
    elif houses[position] <=0:
        print(f"Place {position}  has Valentine's day.")

    return houses
numbers = [int(x) for x in input().split("@")]

command = input()
cupid_position = 0
while command != "Love!":

    jump = command.split(" ")
    index = int(jump[1])
    cupid_position += index
    if cupid_position >= len(numbers):
        cupid_position = 0
    numbers = houses_targets(numbers, cupid_position)


    command = input()
print(f"Cupid's last position was {cupid_position}.")
failed_house = [int(x) for x in numbers if int(x)> 0]

if failed_house:
    print(f"Cupid has failed {len(failed_house)} places.")
else:
    print("Mission was successful.")