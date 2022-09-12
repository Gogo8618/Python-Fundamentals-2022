def version(new_version):
    result = int(''.join(new_version)) + 1
    result1 = '.'.join(str(result))
    print(result1)


data = input().split(".")
version(data)
