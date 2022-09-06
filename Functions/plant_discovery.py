import re


def reset_rating(store_func, plant_func):
    if plant_func in store_func:
        store_func[plant_func]['rating'] = 0
    else:
        print("error")
    return store_func


def add_rarity(store_func, plant_func, rarity_func):
    if plant_func in store_func:
        store_func[plant_func]['rarity'] = rarity_func
    else:
        print("error")
    return store_func


def add_rating(store_func, plant_func, rating_func):
    if plant_func in store:
        store_func[plant_func]['rating'] += rating_func
        store_func[plant_func]['counter'] += 1
    else:
        print("error")
    return store_func


n = int(input())
store = {}
for _ in range(n):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = int(plant_info[1])
    if plant not in store:
        store[plant] = {"rarity": rarity, "rating": 0, "counter": 0}
command = input()

while command != "Exhibition":
    data = re.split(": | - ", command)
    if data[0] == "Rate":
        plant = data[1]
        rating = int(data[2])
        store = add_rating(store, plant, rating)
    elif data[0] == "Update":
        plant = data[1]
        new_rarity = int(data[2])
        store = add_rarity(store, plant, new_rarity)
    elif data[0] == "Reset":
        plant = data[1]
        store = reset_rating(store, plant)
    command = input()

print("Plant for the exhibition:")
for key, value in store.items():
    average = value['rating'] / value['counter']
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {average:.2f}")
