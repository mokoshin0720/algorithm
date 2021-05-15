'''
https://atcoder.jp/contests/arc098/tasks/arc098_a
リーダーの方向を向かせる最小値

【入力例】
5
WEEWW

【出力例】
1 → 西から3番目の人をリーダーとすると、1番目の人が向きを変えるだけでOK
'''

'''
愚直に解く　→　O(N**2)
'''
N = int(input())
s = input()

min_turn = 10**9

for i in range(N):
    turn = 0

    for p in range(N):
        if p==i: continue # リーダーの場合はスキップ

        if p<i and s[p] == "W":
            turn += 1
        
        if p>i and s[p] == "E":
            turn += 1

    min_turn = min(turn, min_turn)

print(min_turn)

'''
累積和のアルゴリズムで解く → O(N)
'''
N = int(input())
s = input()

min_turn = 10**9

# westを向いている人の累積和
sum_W = [0]
for i in range(N):
    if s[i] == "W":
        sum_W.append(sum_W[i]+1)
    else:
        sum_W.append(sum_W[i])

for i in range(N):
    # リーダーiより西側にいて、westを向いている人の人数
    w = sum_W[i]
    # リーダーiより東側にいて、eastを向いている人の人数
    e = (N-1-i) - (sum_W[N]-sum_W[i+1])

    turn = w+e
    min_turn = min(min_turn, turn)

print(min_turn)