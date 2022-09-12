journal = input().split(", ")

command = input()

while command != "Craft!":

    n = command.split(" - ")
    n1 = n[0]
    n2 = n[1]

    if n1 == "Collect":
        if n2 not in journal:
            journal.append(n2)
    elif n1 == "Drop":
        if n2 in journal:
            journal.remove(n2)

    elif n1 == "Combine Items":
        item = n2.split(":")
        old_item = item[0]
        new_item = item[1]
        for i in range(len(journal)):
            if journal[i] == old_item:
                journal.insert(i + 1, new_item)
    elif n1 == "Renew":
        if n2 in journal:
            if journal[-1] == n2:
                continue
            else:
                journal.remove(n2)
                journal.append(n2)
    command = input()
print(", ".join(journal))