'''
再帰関数のメモ化　→　動的計画法
一度計算をした結果「例えば、func(5)」をメモして、再びfunc(5)が出たら計算せずメモをよぶ
'''

memo = [-1] * 50

def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1

    if memo[N] == -1:
        memo[N] = fibo(N-1) + fibo(N-2)
    else:
        return memo[N]

    return memo[N]

fibo(49)
for N in range(2, 50):
    print('{}項目：{}'.format(N, memo[N]))