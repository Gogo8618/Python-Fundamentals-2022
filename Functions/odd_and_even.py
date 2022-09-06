def sum_all_even_odd_numbers(number):
    odd = 0
    even = 0

    for i in number:
        if i % 2 == 0:
            even += i
        else:
            odd += i

    print(f"Odd sum = {odd}, Even sum = {even}")


num = map(int, list(input()))
sum_all_even_odd_numbers(num)
