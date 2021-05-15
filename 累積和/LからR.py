'''
N個の整数をもつ配列Aがある。
この配列AのL番目からR番目までの和を出力せよ。

【入力例】
5
1 4 2 6 5
1 3

【出力例】
12　→ 1+4+2
'''

N = int(input())
num_list = list(map(int, input().split()))
L, R = map(int, input().split())

s=0

for i in range(L, R+1):
    s += num_list[i]
print(s)