import sys
from typing import List

class Card:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a: int = a
        self.b: int = b
        self.c: int = c
        self.d: int = d

# After this, Evirir will gain points equal to the sum of all visible numbers. What is the maximum amount of points Evirir can gain if he chooses the m cards and arrange them optimally?

# def max_points(card: List[Card], m):

#     card.sort(key=lambda card: (card.a + card.b), reverse=True)
    
#     a_b_card = card[:m - 1]
#     for i in a_b_card:
#         card.remove(i)
#     max_sum = sum([i.a + i.b for i in a_b_card])

#     card.sort(key=lambda card: (card.a + card.b + card.c + card.d), reverse=True)
#     card_last = card[0]
#     max_sum += card_last.a + card_last.b + card_last.c + card_last.d

#     print(max_sum)

def max_points(card: List[Card], m):

    card.sort(key=lambda card: ((card.d + card.c + card.b + card.a)), reverse=True)
    card_last = card[0]
    max_sum = card_last.a + card_last.b + card_last.c + card_last.d
    card.remove(card_last)

    card.sort(key=lambda card: ((card.a + card.b)), reverse=True)
    
    a_b_card = card[:m - 1]

    max_sum += sum([i.a + i.b for i in a_b_card])
    print(max_sum)

sys.stdin = open("innovation.in", "r")
sys.stdout = open("innovation.out", "w")

n, m = map(int, input().split(" "))
cards: List[Card] = []

for i in range(n):
    a, b, c, d = map(int, input().split(" "))
    cards.append(Card(a, b, c, d))

max_points(cards, m)
