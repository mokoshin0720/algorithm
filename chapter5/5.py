'''
【区間DP】
N個の要素が一列に並んでいて、これをK個の区間に分割したい。
各区間[l, r)にはスコアC(l,r)がついているものとする。
区間分割を行った際のスコアc0+c1+...+ckの最小値は？
'''

N, K = map(int, input().split())
score = 

dp[0] = 0

for i in range(N+1):
    for j in range(N+1):
        dp[i] = min(dp[i], dp[j]+score[i][j])

'''
ちょっと挫折中...
DPの理解を深めてから、また戻ってくる...
'''