'''
【ナップサック問題】
N個の荷物があり、i番目の荷物には価値vと重さwが割り当てられている。
重さの和がW以下となるように荷物を選びナップサックに詰め込む時、価値の和の最大値を求めよ。
'''
N, W = map(int, input().split())
weight = []
value = []

for i in range(N):
    x, y = map(int, input().split())
    weight.append(x)
    value.append(y)

# テーブルの初期化
dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(N):
    for w in range(W+1):
        if w < weight[i]: #　選ばない時
            dp[i+1][w] = dp[i][w]
        else: # 選ぶ時
            dp[i+1][w] = max(dp[i][w], dp[i][w-weight[i]]+value[i])
print(dp[N][W])
'''
dp[i][w]は、w以下の重さでi個の荷物を選んだ時の、最大となる価値。
表のようなイメージを持っておくと良いかも。

① 選んだ結果がdp[i+1][w]になるのであれば、選ぶ前はdp[i][w-weight[i]]である。
　 そこにvalue[i]を加えて、dp[i][w]とどちらが価値が高いかを比べている。

② if文で選んだとしても、最終的にwになるのであれば、最大値を超えることはない。

'''