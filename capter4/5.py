'''
フィボナッチ数列をfor文による反復で求める
'''

f = [None]*50
f[0], f[1] = 0, 1

for n in range(2, 50):
    f[n] = f[n-1] + f[n-2]
    print('{}項目：{}'.format(n, f[n]))