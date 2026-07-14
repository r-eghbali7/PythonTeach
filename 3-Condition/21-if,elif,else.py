# Decision order
# if 
# شرط ها 
# if    elif    else

# if 

# if ---conditions--- :
#    .  
#    .
#    .

a = int(input("chose a : "))
if a > 20 :
    print(True)

print(40*"-")

# elif

# if ---conditions--- :
#    .
#    .
#    .
# elif ---conditions--- :
#    .
#    .
#    .

b = int(input("chose b : "))
if b > 20 :
    print(True)
elif b == 20 :
    print("that nice ")

print(40*"-")

# if ---conditions--- :
#    .
#    .
#    .
# elif ---conditions--- :
#    .
#    .
#    .
# else : 
#    .
#    .
#    .

c = int(input("chose c : "))
if c > 20 :
    print(True)
elif c == 20 :
    print("that nice ")
else :
    print("not ok very lower")

print(40*"-")

x = [1,2,3,4,5,67,8,9]
num = int(input("num: "))
if num in x :
    print(f"num {num} va index {x.index(num)}")