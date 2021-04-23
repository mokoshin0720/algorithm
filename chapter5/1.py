'''
【Frog問題】
N個の足場があって、足場の高さはhで与えられる。
以下のいずれかの処理を行って、N-1番目の足場を目指す。

・足場iからi+1に移動する　→　コストは|hi - h(i+1)|
・足場iからi+2に移動する　→　コストは|hi - h(i+2)|

N-1番目に辿り着くまでに必要な最小コストは？
'''

N = int(input())
height_list = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0

for i in range(1,N):
    if i == 1:
        dp[1] = abs(height_list[1] - height_list[0])
        continue
    # 二つの処理を実装　→　「丸」と「矢印」で表したグラフをイメージするとわかりやすいかも
    one = dp[i-1] + abs(height_list[i-1] - height_list[i])
    two = dp[i-2] + abs(height_list[i-2] - height_list[i])
    dp[i] = min(one, two)

print(dp[-1])