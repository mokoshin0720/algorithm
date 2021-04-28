'''
【編集距離】
2つの文字列SとTが与えられる。
以下の3つの操作を用いて、SをTに変形する。
・挿入
・削除
・置換
この際の、最小コストを求めよ。
'''

S, T = map(str, input().split())
len_s = len(S)
len_t = len(T)

# 以下、初期設定
dp = [[0] * (len_t+1) for _ in range(len_s+1)]

for i in range(len_s+1):
    dp[i][0] = i

for j in range(len_t+1):
    dp[0][j] = j

# DP開始
for i in range(1, len_s+1):
    for j in range(1, len_t+1):
        if S[i-1] == T[j-1]:
            cost = 0
        else:
            cost = 1
        
        insertion = dp[i-1][j] + 1
        deletion = dp[i][j-1] + 1
        replacement = dp[i-1][j-1] + cost

        dp[i][j] = min(insertion, deletion, replacement)
    
print(dp[-1][-1])

'''
S[i-1] == T[j-1]の時は、同じ文字のため、変更を加える必要がなくcostが0
'''