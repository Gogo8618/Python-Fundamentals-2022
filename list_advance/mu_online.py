rooms = input().split("|")

health = 100
bitcoins = 0
counter = 0

for i in range(len(rooms)):
    room = rooms[i].split(" ")
    point = int(room[1])
    counter += 1
    if room[0] == "potion":
        currnet_health = health
        health += point
        if health >= 100:
            health = 100
            point = 100 - currnet_health
        print(f"You healed for {point} hp.")
        print(f"Current health: {health} hp.")
    elif room[0] == "chest":
        bitcoins += point
        print(f"You found {point} bitcoins.")
    else:
        health -= point

        if health > 0:
           print(f"You slayed {room[0]}.")
        else:
          print(f"You died! Killed by {room[0]}.")
          print(f"Best room: {counter}")
          break
    if counter == len(rooms):
        print("You've made it!")
        print(f"Bitcoins: {bitcoins}")
        print(f"Health: {health}")