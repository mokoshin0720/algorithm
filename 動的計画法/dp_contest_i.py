'''
https://atcoder.jp/contests/dp/tasks/dp_i
【入力例】
3
0.30 0.60 0.80

【出力例】
0.612 -> 表が出る方が多い場合の確率を全て足し合わせる
'''

N = int(input())
p_list = list(map(float, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0] = [0]*(N+1)

for i in range(1, N+1):
    if i == 1:
        dp[i][0] = 1-p_list[i-1]
        dp[i][1] = p_list[i-1]
        continue
    for j in range(i+1):
        dp[i][j] = dp[i-1][j]*(1-p_list[i-1]) + dp[i-1][j-1]*(p_list[i-1])
ans = 0
for i in range((N+1)//2, N+1):
    ans += dp[-1][i]
print(ans)

'''
i回目までに表がj回出る場合を考えている。
→DPで解けると思ったら、表を書いてみるとイメージが湧きやすい。
'''