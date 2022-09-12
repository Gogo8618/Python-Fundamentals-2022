todo = ["" for i in range(11)]
command = input()

while command != "End":
    notes = command.split("-")
    position = int(notes[0])
    product = notes[1]
    todo[position] = product
    command = input()
final_todo_list = [product for product in todo if product != ""]



print(final_todo_list)
