# 아래 그림과 같은 이진트리를 전위순회와 후위순회를 연습해보세요.
#     1
#   2   3
#  4 5 6 7
 

# 전위순회 출력 : 1 2 4 5 3 6 7 
# 중위순회 출력 : 4 2 5 1 6 3 7 
# 후위순회 출력 : 4 5 2 6 7 3 1


###
import sys
sys.stdin=open("input.txt", "r")
#전위순회
def DFS(v):
    if v>7:
        return
    else:
        print(v end=" ")
        DFS(v*2)
        DFS(v*2+1)
#중위순회
def DFS(v):
    if v>7:
        return
    else:
        DFS(v*2)
        print(v end=" ")
        DFS(v*2+1)
#후위순회
def DFS(v):
    if v>7:
        return
    else:
        DFS(v*2)
        DFS(v*2+1)
        print(v end=" ")
