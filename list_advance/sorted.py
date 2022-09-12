words = input().split(", ")

sorted_names = sorted(words)

sorted_names = sorted(sorted_names, key=lambda name: -len(name))

print(sorted_names)