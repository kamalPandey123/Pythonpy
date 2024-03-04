#write a program to make fabonacci serise
#draw tringle star pattern
#rivers pawan string
def fabonacci(n):
    if n==0:
      return 0
    elif n==1:
        return 1
    else:
        return fabonacci(n-2) + fabonacci(n-1) 
    
    

n =  int(input("Enter the size:"))
i=0
while i<n-1:
    print(fabonacci(i),end=" ")
    i+=1 
