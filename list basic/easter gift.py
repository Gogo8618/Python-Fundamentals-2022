gifts = input().split(' ')

command = input()

while command != "No Money":
    data = command.split(' ')
    if data[0] == "OutOfStock":
        gift = data[1]
        if gift in gifts:
            for i, value in enumerate(gifts):
                if value == gift:
                    gifts.remove(value)
                    gifts.insert(i, "None")
    elif data[0] == "Required":
        gift = data[1]
        index = int(data[2])
        if 0 < index < len(gifts):
            gifts[index] = gift
    elif data[0] == "JustInCase":
        gift = data[1]
        gifts[-1] = gift

    command = input()
while "None" in gifts:
    gifts.remove("None")
print(' '.join(gifts))
