from joblib import Parallel, delayed
import time

def compute(x):
    if x == 0:
        return 0
    if (x % 2 == 0):
        return x / 2
    else:
        return 3 * x + 1

time1 = time.time()
n = input()
n, k = map(int, n.split(" "))

num_arr = map(int, input().split(" "))

# Parallel processing
for i in range(0, k):
    num_arr = Parallel(n_jobs=4)(delayed(compute)(x) for x in num_arr)

time2 = time.time()


print(sum(num_arr))
print(time2 - time1)
