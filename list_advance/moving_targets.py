targets = [int(x) for x in input().split(" ")]

command = input()

while command != "End":
    shoot = command.split(" ")

    first_step = shoot[0]
    index = int(shoot[1])
    value = int(shoot[2])
    if first_step == "Shoot":
        if 0 < int(index) < len(targets):
            targets[index] -= value
            if targets[index] <=0:
                targets.pop(index)
    elif first_step == "Add":
        if 0 < index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif first_step == "Strike":
        left_side = index - value
        right_side = index + value
        if left_side >= 0 and right_side < len(targets):
           del targets[left_side:right_side + 1]
        else:
            print("Strike missed!")


    command = input()

print("|".join(map(str, targets)))
