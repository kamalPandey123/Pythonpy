num = int(input("Enter the number:"))
count = 0
i =2
for i in range(num -1):
    if num % i == 0:
        count += 1

if count == 1:
    print("Number is prime:")
else:
   print("Number is Not prime:")    

