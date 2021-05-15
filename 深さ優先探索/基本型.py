'''
深さ優先探索をpythonで実装してみる
'''
# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

# 頂点数N, 辺情報E, 始点sは定義済みとする

# N個のFalseで初期化した配列visitedを用意する
visited = []
for i in range(N):
    visited.append(False)

# 再起関数dfsを定義する
def dfs(i):
    visited[i] = True
    for j in E[i]:
        if not visited[j]:
            dfs(j)
    
# 始点から呼び出す
dfs(s)