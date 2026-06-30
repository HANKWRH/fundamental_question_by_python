n=int(input())
suit_order = {'S':4,'H':3,'D':2,'C':1}

def card_key(card):
    suit = card[0]
    number = int(card[1:])
    return (suit_order[suit],number)

for _ in range(n):
    cards = input().split()
    cards.sort(key=card_key, reverse=True)
    print(*cards)