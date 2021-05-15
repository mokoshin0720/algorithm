'''
https://atcoder.jp/contests/abc114/tasks/abc114_c

整数Nが与えられる。1以上N以下の整数のうち、七五三数は何個あるでしょうか？
七五三数：　数字7, 5, 3がそれぞれ1回以上現れ、これら以外の数字はない。

【入力例】
575

【出力例】
4 → 357, 375, 537, 573の4つ

'''

N = int(input())
ans = 0

# 数nについて調べ、末尾に数字を追加した数を再帰的に調べる関数
# use3, use5, use7はそれぞれ3, 5, 7を使ったかというフラグ
def dfs(n, use3, use5, use7):
    global ans
    # Nを超えていたら打ち切って終了する
    if n > N: return
    
    # 3種類全てを使っていたら、答えに加算する
    if use3 and use5 and use7:
        ans += 1

    # 末尾に3, 5, 7を付けた数を再帰的に調べる
    dfs(10*n+3, True, use5, use7)
    dfs(10*n+5, use3, True, use7)
    dfs(10*n+7, use3, use5, True)

# 何もない状態（値としては0)から呼び出す
dfs(0, False, False, False)
print(ans)