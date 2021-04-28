'''
【Frog問題】
N個の足場があって、足場の高さはhで与えられる。
以下のいずれかの処理を行って、N-1番目の足場を目指す。

・足場iからi+1に移動する　→　コストは|hi - h(i+1)|
・足場iからi+2に移動する　→　コストは|hi - h(i+2)|

N-1番目に辿り着くまでに必要な最小コストをメモ化再帰関数で求めよ。
'''

N = int(input())
height_list = list(map(int, input().split()))
INF = 10**9

dp = [INF] * N

def func(n):
    if dp[n] != INF:
        return dp[n]
    
    if n == 0:
        dp[n] = 0
    elif n == 1:
        dp[n] == abs(height_list[0] - height_list[1])
    else:
        # メモ化しながら、再帰呼び出しを行う
        one = func(n-1) + abs(height_list[n-1] - height_list[n])
        two = func(n-2) + abs(height_list[n-2] - height_list[n])
        dp[n] = min(one, two)

    return dp[n]

print(func(N-1))