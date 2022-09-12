n = [int(x) for x in input().split(" ")]

command = input()
counter = 0
while command != "End":
    index = int(command)

    if index in range (len(n)):
        target = n[index]
        n[index] = -1
        for i in range(len(n)):
            if n[i] != -1:
                if target < n[i]:
                    n[i] -= target
                else:
                    n[i] += target
        counter += 1

    command = input()

print(f"Shot targets {counter} -> {' '.join(map(str, n))}")
