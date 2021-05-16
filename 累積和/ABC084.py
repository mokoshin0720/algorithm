'''
https://atcoder.jp/contests/abc084/tasks/abc084_d
'''
import math

Q = int(input())
lr_list = [list(map(int, input().split())) for _ in range(Q)]

# n以下の素数をエラトステネスによって求める。リストを返す.
def eratosthenes(n):
    prime = []
    limit = math.sqrt(n)
    data = [i+1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime+data
        prime.append(p)
        data = [e for e in data if e%p != 0]

primes = eratosthenes(10**5)

# 条件に当てはまる全ての数が素数かどうか
is_prime = [False]*(10**5+1)
for p in primes:
    is_prime[p] = True

# 条件に当てはまる全ての数が2017に近いかどうか
like_2017 = [False]*(10**5+1)
for p in primes:
    if is_prime[(p+1)//2]:
        like_2017[p] = True

# 通常は0(False=2017に近くない)
tmp = 0
ruiseki = [0]

for i in range(1, 10**5+1):
    if like_2017[i]:
        tmp += 1
    ruiseki.append(tmp)

for lr in lr_list:
    left = lr[0]
    right = lr[1]
    print(ruiseki[right]-ruiseki[left-1])