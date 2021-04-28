# N個の整数(a0, a1, a2...)の中に「aj == V」となるデータがあるかどうか

N, V = map(int, input().split())
num_list = list(map(int, input().split()))

exist = False

for num in num_list:
    if num == V:
        exist = True

if exist:
    print('Yes')
else:
    print('No')