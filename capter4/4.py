'''
フィボナッチ数列のN番目を求める
→1つ前と2つ前の数字を足して出来上がる数列
→0,1,1,2,3,5,8,13...
'''

def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1

    return fibo(N-1) + fibo(N-2)

print(fibo(5))