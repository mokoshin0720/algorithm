'''
https://atcoder.jp/contests/dp/tasks/dp_c

【入力例】
3
10 40 70
20 50 80
30 60 90


【出力例】
210 -> 70, 50, 90を取ると最大になる
'''

N = int(input())
abc_list = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N+1)]
dp[0] = [0]*3

for i in range(1, N+1):
    if i == 1:
        dp[i][0] = abc_list[i-1][0]
        dp[i][1] = abc_list[i-1][1]
        dp[i][2] = abc_list[i-1][2]
    else:
        dp[i][0] = max(dp[i-1][1]+abc_list[i-1][0], dp[i-1][2]+abc_list[i-1][0])
        dp[i][1] = max(dp[i-1][0]+abc_list[i-1][1], dp[i-1][2]+abc_list[i-1][1])
        dp[i][2] = max(dp[i-1][0]+abc_list[i-1][2], dp[i-1][1]+abc_list[i-1][2])
print(max(dp[-1]))

'''
i日目にa,b,cを行うとしたとき、i日目の最大値を求める。
例えば、i日目にaを行う -> i-1日目はbかcを行っているので、i-1日目のb,cの大きい方を選択すれば良い。
'''