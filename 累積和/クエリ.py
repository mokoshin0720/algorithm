'''
N個の整数を持つ配列Aがあり、クエリ（つまり、LRのパターン）がQ個与えられる。
i番目のクエリでは配列AのLi番目からRi番目までの和を出力せよ。

【入力例】
5 3
1 4 2 6 5
1 3
0 1
2 4

【出力例】
12 → 4+2+6
5 → 1+4
13 → 2+6+5

'''

'''
愚直に1クエリずつ解くバージョン → O(NQ)
'''
N, Q = map(int, input().split())
num_list = list(map(int, input().split()))
lr_list = [list(map(int, input().split())) for _ in range(Q)]

for lr in lr_list:
    ruiseki = 0
    for i in range(lr[0], lr[1]+1):
        ruiseki += num_list[i]
    print(ruiseki)

'''
ruiseki[R+1] = num_list[0]+num_list[1]+...+num_list[R]
ruiseki[L] = num_list[0]+num_list[1]+...+num_list[L-1]
↓↓↓
特定区間の累積和 = ruiseki[R+1]-ruiseki[L]
O(N+Q)
'''
N, Q = map(int, input().split())
num_list = list(map(int, input().split()))
lr_list = [list(map(int, input().split())) for _ in range(Q)]

ruiseki = [0]

for i in range(0, N):
    ruiseki.append(ruiseki[i]+num_list[i])

for lr in lr_list:
    left = lr[0]
    right = lr[1]
    print(ruiseki[right+1] - ruiseki[left])