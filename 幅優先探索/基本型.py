'''
幅優先探索をpythonで実装してみる
'''

from collections import deque

# 頂点数N, 辺情報E, 始点sは定義済みとする

# N個のFalseで初期化した配列visitedを用意する
visited = []
for i in range(N):
    visited.append(False)

# キュー（データ構造）を用意する
Q = deque()
Q.append(s)
visited[s] = True

# キューを取り出しながら探索する
while len(Q) > 0:
    i = Q.popleft()
    for j in E[i]:
        if not visited[j]:
            visited = True
            Q.append(j)
            