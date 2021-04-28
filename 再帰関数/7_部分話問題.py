'''
N個の数列(a0, a1, a2...)の中から何個かを選んで、総和をWにできるかどうか
→部分和問題を再帰関数で解いてみる
'''

def func(i, w, a):
    # ベースケース -> 0個の数字で0を作る
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    
    # a[i-1]を選ばない場合
    if func(i-1, w, a):
        return True

    # a[i-1]を選ぶ場合
    if func(i-1, w-a[i-1], a):
        return True
    
    return False

N, W = map(int, input().split())
a = list(map(int, input().split()))

if func(N, W, a):
    print('Yes')
else:
    print('No')