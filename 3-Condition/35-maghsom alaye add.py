x = int(input("add:"))
count = 0
for i in range(1,x+1):
    
    if x % i == 0:
        print(i)
        count += 1
print("count:",count)