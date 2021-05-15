'''
配列の先頭からi番目までの和を求めよ
【入力例】
2 5 1
【出力例】
8
'''

'''
愚直にfor文を回すパターン→O(N**2)
'''
N = int(input())
num_list = list(map(int, input().split()))
ans = [0]

for i in range(0, N):
    s = 0 # num_list[0]からnum_list[i]までの和を記録する

    for j in range(0, i+1): # sにnum_list[0]からnum_list[i]までを足し合わせる
        s += num_list[j]

    ans.append(s)

print(ans[-1])

'''
すでに計算した部分を使い回す
'''
N = int(input())
num_list = list(map(int, input().split()))
ans = [0]

# num_listとansの配列は1つズレていることに注意
for i in range(0,N):
    s = ans[i] + num_list[i]
    ans.append(s)

print(ans[-1])