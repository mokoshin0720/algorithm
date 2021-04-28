'''
長さNの整数列(a0, a1, a2...)が小さい順でソートされている。
また、整数Kが与えられ、ai >= Kであるようなインデックスiのうち、最小のものを出力せよ。
なお、条件を満たす要素が存在しない場合は-1を出力せよ。
【入力例】
8 4
1 3 5 7 9 11 13 15
【出力例】
2
'''

N, K = map(int, input().split())
num_list = list(map(int, input().split()))

left = -1
right = N

while abs(left-right) > 1:
    mid = (left+right) // 2
    if num_list[mid] >= K: right = mid
    else: left = mid

if right == N:
    print(-1)
else:
    print(right)

'''
対象リストをソート
↓
選択範囲の左端と右端を指定
↓
左端と右端からリストの中央を見つけて、中央の要素と条件を比較
↓
結果に応じて、左端or右端を求めた中央に移動させる
'''