def stops_replace(stop_func, old_func, new_func):
    stop_func = stop_func.replace(old_func, new_func)
    print(stop_func)
    return stop_func


def remove_stop(stop_func, start_func, end_func, cut_func):
    if 0 <= start_func < len(stop_func) and 0 <= end_func < len(stop_func):
        stop_func = stop_func.replace(cut_func, '', 1)
        print(stop_func)
    return stop_func


def add_stop(stop_func, index_func, text_func):
    if 0 <= index_func < len(stop_func):
        stop_func = stop_func[0:index_func] + text_func + stop_func[index_func:]
        print(stop_func)
    return stop_func


stops = input()

command = input()

while command != "Travel":
    data = command.split(":")
    if data[0] == "Add Stop":
        index = int(data[1])
        text = data[2]
        stops = add_stop(stops, index, text)

    elif data[0] == "Remove Stop":
        start = int(data[1])
        end = int(data[2])
        cut = stops[start:end + 1]
        stops = remove_stop(stops, start, end, cut)
    elif data[0] == "Switch":
        old = data[1]
        new = data[2]
        stops = stops_replace(stops, old, new)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")
