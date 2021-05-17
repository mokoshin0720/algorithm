'''
https://atcoder.jp/contests/abc199/tasks/abc199_c
'''
N = int(input())
S = input()
Q = int(input())
tab_list = [list(map(int, input().split())) for _ in range(Q)]

ans = list(S)

def listToString(s): 
    str1 = "" 
    return (str1.join(s))

for tab in tab_list:
    t = tab[0]
    a = tab[1]
    b = tab[2]

    if t == 1:
        ans[a-1], ans[b-1] = ans[b-1], ans[a-1]
    elif t == 2:
        pre = ans[:N]
        post = ans[N:]
        ans = post+pr

print(listToString(ans))