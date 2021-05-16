'''
https://atcoder.jp/contests/abc122/tasks/abc122_c
'''
N, Q = map(int, input().split())
S = input()
lr_list = [list(map(int, input().split())) for _ in range(Q)]

ruiseki = [0]
tmp = 0

for i in range(len(S)-1):
    a = S[i]
    b = S[i+1]
    if a == 'A' and b == 'C':
        tmp += 1
    ruiseki.append(tmp)

for lr in lr_list:
    left = lr[0]
    right = lr[1]
    ans = ruiseki[right-1] - ruiseki[left-1]
    print(ans)