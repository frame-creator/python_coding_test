#그래프 정보를 인접행렬로 표현해보세요.

# ▣ 입력설명
# 첫째 줄에는 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결정보와 거리비용이 주어진다.

# ▣ 출력설명 
# 인접행렬을 출력하세요.

# ▣ 입력예제 
# 6 9 
# 1 2 7 
# 1 3 4 
# 2 1 2 
# 2 3 5 
# 2 5 5 
# 3 4 5 
# 4 2 2 
# 4 5 5 
# 6 4 5

# ▣ 출력예제  
# 074000 
# 205050 
# 000500 
# 020050 
# 000000 
# 000500
 
  

 

###
import sys
sys.stdin=open("input.txt","r")
n,m=map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int, input().split())
    g[a][b]=1
    g[b][a]=1



for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=" ")
    print()
    
    
    
    
    
    
    
    
