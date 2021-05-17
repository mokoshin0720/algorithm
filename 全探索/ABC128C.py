'''
https://atcoder.jp/contests/abc128/tasks/abc128_c
'''

n,m = map(int, input().split())
ks = [tuple(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
 
ans = 0
for bit in range(2**n):
    h = set() # onになっているswitch
    for i in range(n):
        if bit >> i & 1:
            h.add(i+1)
    num = 0 # ついている電球の数
    for i in range(m):
        k = ks[i][0]
        total = 0
        for j in range(k):
            if ks[i][j+1] in h:
                total += 1
        if total % 2 == p[i]:
            num += 1
    if num == m:
        ans += 1
                
print(ans)