# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑는 방법의 수를 출력하는 프로그램을 작성하세요.

# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N)이 주어집니다.

# ▣ 출력설명
# 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 출력 순서는 사전 순으로 오름차순으로 출력합니다.

# ▣ 입력예제  
# 4 2

# ▣ 출력예제  
# 1 2
# 1 3
# 1 4
# 2 3 
# 2 4 
# 3 4 
# 6


###
import sys
sys.stdin=open("input.txt", "r")
def DFS(L,s):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        cnt+=1
        print()
    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1)



if __name__=="__main__":
    n,m=map(int, input().split())
    res=[0]*(n+1)
    cnt=0
    DFS(0,1)
    
    
    
    
    
    
    
