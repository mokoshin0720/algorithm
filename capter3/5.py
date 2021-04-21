'''
N個の正の整数（a0, a1, a2...)と正の整数Wが与えられる。
a0, a1, a2...の中から何個かの整数を選んで、総和をWとできるかどうか判定。
→組み合わせの全探索
'''

N, W = map(int, input().split())
num_list = list(map(int, input().split()))

exist = False
for bit in range(2**N): # 2のn乗通りを探索
    sum_val = 0
    for i in range(N):
        if bit & (1 << i): # 例えば、bit=3(0b11)のとき、i=0,1でif文が通る / iは1をN桁まで移動させている
            sum_val += num_list[i] # 1が含まれている（フラグが立っている）要素をカウント
    if sum_val == W:
        exist = True
if exist:
    print('Yes')
else:
    print('No')

'''
以下、bit全探索の下準備

bit演算子
    &: 論理積(1001 & 1010 -> 1000)
    |: 論理和(1001 | 1010 -> 1011)
    ^: 排他的論理和 (1001 ^ 1010 -> 0011)
    <<: 左シフト(1001 -> 10010)　→ 1（フラグ）の位置を移動させるのに使える
    >>: 右シフト(1001 -> 0100)　→ 1（フラグ）の位置を移動させるのに使える
'''
i = int(input())
bit = int(input(), 2)

if bit & (1 << i):
    print('Yes')
else:
    print('No')