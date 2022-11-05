nTerms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nTerms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nTerms == 1:
   print("Fibonacci sequence upto",nTerms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nTerms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1