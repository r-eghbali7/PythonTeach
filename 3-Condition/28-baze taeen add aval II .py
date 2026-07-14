lower = 900 # int(input(" meghdar1 "))
upper = 1000 # int(input(" meghdar2 "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper ):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)