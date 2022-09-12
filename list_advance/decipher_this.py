def return_to_chr(word):
    operate_string = list(word)
    num_of_str = list()

    while operate_string[0].isdigit():
        num_of_str.append(operate_string[0])
        operate_string.pop(0)

    num = int(''.join(num_of_str))
    operate_string.insert(0, chr(num))
    return ''.join(operate_string)


def exchange_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return ''.join(letters)


print(' '.join([exchange_letters(return_to_chr(word)) for word in input().split()]))
