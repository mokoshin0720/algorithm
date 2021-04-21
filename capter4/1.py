'''
再帰関数の基本形
'''

def func(N):
    if N == 0:
        return 0
    return N + func(N-1)

'''
挙動
例えば、func(5)が入力されたら、
func(5) -> 5 + func(4) -> 5 + (4 + func(3)) -> のようにfunc(0)まで続く
'''