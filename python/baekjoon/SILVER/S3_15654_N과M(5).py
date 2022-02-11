import sys

def dfs(start:int):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in l:
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()


n, m = map(int, sys.stdin.readline().split())
l = sorted(list(map(int, sys.stdin.readline().split())))
s = []
dfs(1)
