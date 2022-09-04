number_of_order = int(input())

total = 0

for order in range(number_of_order):
    price_per_capsule = float(input())
    days = int(input())
    count_capsules = int(input())

    current_order = days * count_capsules * price_per_capsule
    total += current_order
    print(f"The price for the coffee is: ${current_order:.2f}")

print(f"{total:.2f}")
