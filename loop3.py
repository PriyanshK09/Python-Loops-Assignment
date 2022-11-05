min = int(input("Enter the min number range : "))
max = int(input("Enter the max number of the range : "))

for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)