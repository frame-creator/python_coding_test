//어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다. 

//6을 예로 들면

//6 ÷ 1 = 6 … 0
//6 ÷ 2 = 3 … 0
//6 ÷ 3 = 2 … 0
//6 ÷ 4 = 1 … 2
//6 ÷ 5 = 1 … 1
//6 ÷ 6 = 1 … 0
//그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.

//두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.


///
import sys
sys.stdin=open("input","rt")
n, k=map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%==0
    cnt+=1
    if cnt=k:
        print(i)
        break
    else: print(-1)
      
///
while(True):
  try:
    input_num = int(input("약수를 구할 숫자를 입력해주세요 : ")) 
    break; 
    except: 
      print("숫자만 입력하실 수 있습니다") 
      
      
      count = 0 
      print(input_num,"의 약수 : ", end='') 
      for a in range(1, input_num+1): 
        if input_num == a: 
          print(a) 
          count += 1 
          elif input_num % a == 0: 
            print(a, end=', ') 
            count += 1 
            
  print(input_num,"의 약수의 총 개수 : ", count)
  
  
  
  
            
            
            
            
