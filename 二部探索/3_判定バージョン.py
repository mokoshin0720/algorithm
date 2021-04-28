'''
高橋くんは赤い花をR本、青い花をB本持っています。
高橋くんは次の2種類の花束を作ることができます。

・x本の赤い花と1本の青い花からなる花束
・1本の赤い花とy本の青い花からなる花束

高橋くんが作ることのできる花束の個数の最大値を求めよ。
なお、全ての花を使い切る必要はない。

【入力例】
5 5 -> R B
3 4 -> x y

【出力例】
2
「3本の赤い花と1本の青い花からなる花束」を1つ、「1本の赤い花と4本の青い花からなる花束」を1つ。
この時、赤い花が1本余る。
'''

R, B = map(int, input().split())
x, y = map(int, input().split())

# 整数Nが与えられた時に、花束を合計N個作れるか判定
def check(N):
    # 赤青ともに、花束1つにつき最低1つは花が必要だから、引いておく
    r = R-N
    b = B-N
    if r < 0 or b < 0:
        return False
    # 上で残った花を使って、赤青それぞれに必要な束をどれだけ作れるか
    r_num = r // (x-1)
    b_num = b // (y-1)
    num = r_num + b_num
    return (num >= N)

left = 0
right = 10**18 + 1

while abs(left-right) > 1:
    mid = (left+right) // 2
    if check(mid): left = mid
    else: right = mid

print(left)

'''
二分探索は、答えになる可能性がある範囲をTrueとFalseで分けているイメージを持つ。
'''