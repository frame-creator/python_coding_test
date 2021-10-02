//N개의 숫자로 이루어진 숫자열이 주어지면 숫자열 중에서 s번째 수부터 e번째 수를 오름차순으로 정렬했을 때 k번째 수를 출력하는 프로그램을 만드시오.


///
import sys
sys.stdin=oepn("input.txt","rt")
T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))
