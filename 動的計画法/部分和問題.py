'''
n個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 Aが与えられる。
これらの整数から何個かの整数を選んで総和が A になるようにすることが可能か判定せよ。
可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。

【入力例】
N, A = 3, 10
a_list = [7, 5, 3]

【出力例】
Yes -> 7と3を選ぶ
'''

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(N): # 表を埋めるのに使えるnum_listを前から取ってくる
    for j in range(M+1): # 最大値をどんどん増やしていく
        if num_list[i] > j: # 選ばない時
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-num_list[i]]+num_list[i])
if dp[N][M] == M:
    print("Yes")
else:
    print("No")

'''
マジで表のイメージを持つ
迷ったらココを見に行くこと: https://www.momoyama-usagi.com/entry/info/algo/dp#Python

選ばない時は、表の上からそのまま引っ張ってくる
選ぶ時は、1つ上の行の今回選ぶ重さ分引いたところに価値をプラスする。そして、それと真上を比べて大きい方を取る。
'''