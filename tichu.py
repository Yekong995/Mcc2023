import sys

def longest_run(N, K, cards: list):
    
    max_run_length = 1  # Minimum run length is 1
    current_run_length = 1
    
    for i in range(1, len(cards)):
        diff = cards[i] - cards[i - 1] - 1

        # If the difference between consecutive cards is greater than 1, you can use wild cards
        if diff == 0:
            current_run_length += 1
        elif diff > 0 and K > 0 and K >= diff:
            # Current run length extend because of cards[i] didn't count in the run
            current_run_length += 1
            # You can use up to min(K, diff) wild cards to extend the run
            current_run_length += min(K, diff)
            K -= min(K, diff)
        elif diff > 0 and K <= 0:
            break
        else:
            break
        
        max_run_length = max(max_run_length, current_run_length)

        # print(f"第{i}次迭代：", f"max_run_length={max_run_length}", f"current_run_length={current_run_length}", f"K={K}",
        #       f"diff={diff}", f"cards[i]={cards[i]}", f"cards[i-1]={cards[i-1]}")
    
    # If you have any remaining wild cards, you can use them at the end of the run
    max_run_length += K
    
    return max_run_length

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')

n, k = map(int, input().split(" "))
cards = map(int, input().split(" "))
cards = list(set(cards))
cards.sort()
# print(cards)
print()

numarr = []

import concurrent.futures

numarr = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(longest_run, n, k, cards[i:]) for i in range(len(cards))]
    for future in concurrent.futures.as_completed(futures):
        numarr.append(future.result())

print(max(numarr))
