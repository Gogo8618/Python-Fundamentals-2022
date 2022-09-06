def change_command(message_func, sub, replace):
    message_func = message_func.replace(sub, replace)
    return message_func


def insert_command(message_func, ind, val):
    message_func = message_func[0:ind] + val + message_func[ind:]
    return message_func


def move_command(message_func, num_func):
    cut_letters = message_func[0:num_func]
    message_func = message_func.replace(cut_letters, '', 1)
    message_func = message_func[0:len(message_func)] + cut_letters
    return message_func


message = input()

command = input()

while command != "Decode":
    data = command.split("|")
    if data[0] == "Move":
        number = int(data[1])
        message = move_command(message, number)
    elif data[0] == "Insert":
        index = int(data[1])
        value = data[2]
        message = insert_command(message, index, value)
    elif data[0] == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = change_command(message, substring, replacement)

    command = input()
print(message)
