products = input().split("!")

command = input()

while command != "Go Shopping!":

    action = command.split(" ")
    start = action[0]
    word = action[1]
    if start == "Urgent":
        if word not in products:
            products.insert(0, word)
    elif start == "Unnecessary":
        if word in products:
            products.remove(word)
    elif start == "Correct":
       for i, y in enumerate(products):
           if  y == word:
               products.remove(word)
               products.insert(i, action[2])
    elif start == "Rearrange":
        for i, y in enumerate(products):
            if y == word:
                products.remove(word)
                products.append(word)



    command = input()
print(", ".join(products))
