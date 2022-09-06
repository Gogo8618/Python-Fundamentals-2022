def valid_password(word):
    valid = True
    if not 6 <= len(word) <= 10:
        valid = False
        print("Password must be between 6 and 10 characters")
    for i in word:
        if not i.isalpha() and not i.isdigit():
            valid = False
            print("Password must consist only of letters and digits")
            break
    counter = 0
    for i in word:
        if i.isdigit():
            counter += 1
    if counter < 2:
        valid = False
        print("Password must have at least 2 digit")
    return valid


text = input()

result = valid_password(text)

if result:
    print("Password is valid")
