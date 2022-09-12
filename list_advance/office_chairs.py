def facility_managment(rooms):
    in_boolean = True
    left_chairs = 0
    for i in range(1, rooms + 1):
        room = input().split(' ')

        number_of_chairs = room[0]
        visitors = int(room[1])

        diff = abs(len(number_of_chairs) - visitors)
        if len(number_of_chairs) < visitors:
            in_boolean = False
            print(f"{diff} more chairs needed in room {i}")

        elif len(number_of_chairs) > visitors:
            in_boolean = True
            left_chairs += diff

    if in_boolean:
        print(f'Game On, {left_chairs} free chairs left')


data = int(input())
facility_managment(data)
