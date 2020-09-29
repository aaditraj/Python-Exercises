cards = int(input())
p1_cards = list(map(int, input().split()))
p2_cards = list(map(int, input().split()))
p1_cards.sort(reverse=True)
p2_cards.sort(reverse=True)
winner_found = False
for index, card in enumerate(p1_cards):
    if card > p2_cards[index]:
        print('You win')
        winner_found = True
        break
    elif card < p2_cards[index]:
        print('Friend wins')
        winner_found = True
        break
if not winner_found:
    print('Draw')
