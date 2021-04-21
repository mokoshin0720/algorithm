'''
N個の整数(a0, a1, a2...)とN個の整数(b0, b1, b2...)から、それぞれ1個ずつ整数を選んで和をとる。
その和の中で、整数K以上の範囲内での最小値は？
'''

N, K = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

min_value = 10**10

for a in a_list:
    for b in b_list:
        if K <= a+b <= min_value:
            min_value = a+b
print(min_value)