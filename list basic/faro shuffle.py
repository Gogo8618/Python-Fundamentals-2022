deck = input().split(' ')
count_shuffle = int(input())

half_deck = len(deck) // 2

for _ in range(count_shuffle):

    new_deck = []
    first_half = deck[:half_deck]
    second_half = deck[half_deck:]
    for i in range(len(first_half)):
        new_deck.append(first_half[i])
        new_deck.append(second_half[i])
    deck = new_deck

print(deck)
