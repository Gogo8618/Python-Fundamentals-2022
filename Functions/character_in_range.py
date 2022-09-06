def string_all_characters(a, b):
    result = [chr(x) for x in range(ord(a) + 1, ord(b))]
    return result


w1 = input()
w2 = input()

end_result = string_all_characters(w1, w2)

print(' '.join(end_result))
