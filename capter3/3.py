# N個の整数(a0, a1, a2...)の中の最小値を求める

N = int(input())
num_list = list(map(int, input().split()))

min_value = 10**10

for num in num_list:
    if num < min_value:
        min_value = num
print(min_value)