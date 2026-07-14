# Decision order
# while
# حلقه 

# while ---conditions--- :
#        .
#        .
#        .

a = int(input("write number:"))
while a < 11 :
    print(a)
    a = a + 1 

print(40*"-")

b = 3
while b < 7 :
    f = int(input("write number:"))
    print(b) 
    b += 1

print(40*"-")

x = 0
while x <= 3:
    print(x)
    x += 1 
else : 
    print("done")

print(40*"-")

r = 0
while  r > -1:    
    r = int(input("add :"))
    t = [1,2,3,4,5,6,7,8,9] 
    for i in t :
        i *= r
        print(i) 

print(40*"-")

#c = 10
#while True : 
#    
#    print(c)
#    c = c + 1         /* Dont run /*

#d = 10             
#while False : 
#    print(c)
#    d = d + 1         /* Dont run /*