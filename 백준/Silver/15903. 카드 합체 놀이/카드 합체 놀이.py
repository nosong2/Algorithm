import sys
input = sys.stdin.readline

N, game = map(int, (input().split()))
card_list = list(map(int, input().split()))

for _ in range(game):
    card_list.sort()
    card_sum = card_list[0] + card_list[1]
    card_list[0], card_list[1] = card_sum, card_sum

print(sum(card_list))