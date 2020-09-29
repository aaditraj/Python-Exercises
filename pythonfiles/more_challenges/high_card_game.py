cards = int(input())
p1_cards = map(int, input().split())
p2_cards = map(int, input().split())
for card in p1_cards:
    if card == cards*2:
        print("You win")
for card in p2_cards:
    if card == cards*2:
        print("Friend wins")
