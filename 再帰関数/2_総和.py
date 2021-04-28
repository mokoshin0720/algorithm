'''
1からNまでの総和を計算する再帰関数
'''

# pythonは再帰が1000回程度に制限されているため、リミットを解除
import sys
sys.setrecursionlimit(10**9)

def add(N):
    print('add({})を呼び出しました。'.format(N))
    # ベースケース
    if N == 0:
        return 0

    result = N + add(N-1)

    print('{}までの和 = {}'.format(N, result))

    return result

add(5)