# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.

# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N)이 주어집니다.

# ▣ 출력설명
# 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 출력순서는 사전순으로 오름차순으로 출력합니다.

# ▣ 입력예제 
# 3 2

# ▣ 출력예제  
# 1 2
# 1 3
# 2 1
# 2 3 
# 3 1 
# 3 2 
# 6



###
import sys
import itertools as it
# sys.stdin=open("input.txt", "rt")
n,f=map(int, input().split())
b=[1]*n
cnt=0
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1,n+1))
print(a)
for tmp in it.permutations(a, 3):
    sum=0
    for L, x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=" ")
        break
        
        
        
        
        
        
        
    

