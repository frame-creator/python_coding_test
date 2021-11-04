# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용해서 출력해야 합니다.

# ▣ 입력설명
# 첫 번째 줄에 10진수 N(1<=N<=1,000)이 주어집니다.

# ▣ 출력설명
# 첫 번째 줄에 이진수를 출력하세요.

# ▣ 입력예제  
# 11

# ▣ 출력예제  
# 1011



###
import sys
sys.stdin=open("input.txt","r")
def DFS(x):
    if x==0:
        return
    else:
        print(x%2, end=' ')
        DFS(x//2)


if __name__=="__main__":
    n=int(input())
    DFS(n)
    
    
    
# [참고] 재귀 함수
import sys
sys.stdin=open("input.txt","r")
def DFS(x):
    if x>0:
        DFS(x-1)
        print(x, end=' ')

if __name__=="__main__":
    n=int(input())
    DFS(n)
    
    
    

    
    
    
    
    
