
from collections import deque

def bfs(jug1, jug2, target):
    visited=set()
    queue=deque([(0,0)])

    while queue:
        x,y=queue.popleft()

        if (x,y) in visited:
            continue

        visited.add((x,y))
        print(x,y)

        if x==target or y==target:
            print("Target reached")
            return

        queue.append((jug1,y))
        queue.append((x,jug2))
        queue.append((0,y))
        queue.append((x,0))
        queue.append((min(x+y,jug1), y-(min(x+y,jug1)-x)))
        queue.append((x-(min(x+y,jug2)-y), min(x+y,jug2)))

def dfs(x,y,visited,jug1,jug2,target):

    if (x,y) in visited:
        return

    visited.add((x,y))
    print(x,y)

    if x==target or y==target:
        print("Target reached")
        return

    dfs(jug1,y,visited,jug1,jug2,target)
    dfs(x,jug2,visited,jug1,jug2,target)
    dfs(0,y,visited,jug1,jug2,target)
    dfs(x,0,visited,jug1,jug2,target)

if __name__=="__main__":
    print("BFS Solution")
    bfs(4,3,2)

    print("DFS Solution")
    dfs(0,0,set(),4,3,2)
