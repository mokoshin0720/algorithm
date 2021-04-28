# N個の整数(a0, a1, a2...)の中に「aj == V」となるデータがあるかどうか / また、存在するときは何番目にあるのか

N, V = map(int, input().split())
num_list = list(map(int, input().split()))

found_id = -1

for i in range(N):
    if num_list[i] == V:
        found_id = i
        break

print(found_id)

'''
found_idの初期値を-1（あり得ない値）とすることで、「存在しているかどうか」と「あるなら何番目か」の情報を同時に取得できる
'''