'''
n個の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] が与えられる。
これらの整数から何個かの整数を選んで総和をとったときの、総和の最大値を求めよ。
また、何も選ばない場合の総和は 0 であるものとする。

【入力例】
n = 3
a = (7, -6, 9)

【出力例】
16 → 7と9を選ぶ

'''

N = int(input())
num_list = list(map(int, input().split()))

dp = [-1]*N
dp[0] = 0

for i in range(1, N):
    if i == 1:
        dp[1] = max(num_list[0], dp[0])
        continue
    
    dp[i] = max(dp[i-1]+num_list[i], dp[i-1])
print(dp[-1])

