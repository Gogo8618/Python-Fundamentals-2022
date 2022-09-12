pirate_ship = [int(x) for x in input().split(">")]
warship = [int(y) for y in input().split(">")]

health_capacity = int(input())


loose = False

command = input()
count = 0
while command != "Retire":

    action = command.split(" ")
    act = action[0]
    if act == "Fire":
        index = int(action[1])
        if 0 <= index < len(warship):
            warship[index] -= int(action[2])
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break
    elif act == "Defend":
        index = int(action[1])
        index1 = int(action[2])
        if 0 <= index < len(pirate_ship) and 0 <= index1 < len(pirate_ship):
            for i in range(index, index1 + 1):
                pirate_ship[i] -= int(action[3])
                if pirate_ship[i] <= 0:
                    loose = True
                    print("You lost! The pirate ship has sunken.")
                    break
    elif act == "Repair":
        index = int(action[1])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += int(action[2])
            if pirate_ship[index] > health_capacity:
                pirate_ship[index] = health_capacity
    elif act == "Status":
        minimum = helth_capacity * 0.20
        for i in pirate_ship:
            if i < minimum:
                count +=1
        print(f"{count} sections need repair.")

    command = input()


if not loose:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
