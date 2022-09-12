loots = input().split("|")

command = input()
while command != "Yohoho!":

    n = command.split(" ")
    n0 = n[0]
    if n0 == "Loot":
       for point in n[1:]:
            if point not in loots:
                loots.insert(0, point)
    elif n0 == "Drop":
        index = int(n[1])
        if 0 <= index < len(loots):
            loots.append(loots[index])
            loots.pop(index)
    elif n0 == "Steal":
        count = int(n[1])
        stolen = loots[-count:]
        del loots[-count:]
        print(", ".join(stolen))


    command = input()
if len(loots) != 0:
    average = 0
    sum = 0
    for i in loots:
       sum += int(len(i))
    average = sum / len(loots)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

