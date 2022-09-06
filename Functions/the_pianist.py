def change_key(store_dict, piece_dict, new_dict):
    if piece_dict in store_dict:
        store_dict[piece_dict]['key'] = new_dict
        print(f"Changed the key of {piece_dict} to {new_dict}")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection!")
    return store_dict


def remove_piece(store_dict, piece_dict):
    if piece_dict in store_dict:
        store_dict.pop(piece_dict)
        print(f"Successfully removed {piece_dict}!")
    else:
        print(f"Invalid operation! {piece_dict} does not exist in the collection.")
    return store_dict


def add_store(store_dict, piece_dict, composer_dict, key_dict):
    if piece_dict not in store_dict:
        store_dict[piece_dict] = {"composer": composer_dict, "key": key_dict}
        print(f"{piece_dict} by {composer_dict} in {key_dict} added to the collection! ")
    else:
        print(f"{piece_dict} is already in collection!")
    return store_dict


store = {}
n = int(input())
for i in range(n):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]
    if piece not in store:
        store[piece] = {"composer": composer, "key": key}

command = input()
while command != "Stop":
    items = command.split("|")
    if items[0] == "Add":
        piece = items[1]
        composer = items[2]
        key = items[3]
        store = add_store(store, piece, composer, key)
    elif items[0] == "Remove":
        piece = items[1]
        store = remove_piece(store, piece)
    elif items[0] == "ChangeKey":
        piece = items[1]
        new = items[2]
        store = change_key(store, piece, new)
    command = input()
for key, value in store.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']} ")
