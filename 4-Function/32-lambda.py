# function
# lambda    ----> map()   filter()   reduce()     sorted()    

# lambda 

# lambda ___input___   :  _____body def_____

# posht parde tabe lambda
def add_five(number):
    return number + 5
print(add_five(number=4))

print(40 * "-")

a = lambda b,c,d : (b + d)*c
print("a:" , a(5,4,9))

print(40 * "-")

z = lambda x,y : x ** y

print("z",z(int(input("x:")),int(input("y:"))))

# if    for     while  -------> nmetavan astefadeh kard

print(40 * "-")

g = (lambda q,w : q+w)(2,4)
print(g)

print(40 * "-")
# map ///// map(def , ltis)
li = [1,2,3]
lam  =  map(lambda q:q*3,li)
lam1 =  list(map(lambda w:w*3,li))
print(lam)
print(lam1)

print(40 * "-")

# filter ///// filter(def , list)
lam2 = list(filter(lambda e : e>2 ,li ))
print(lam2)

print(40 * "-")

# reduce
from functools import reduce
li2 = [6,7,8,9,10]
lam3 = reduce(lambda r , t : r + t , li2)
print(lam3)

print(40 * "-")

#li3 = [5,6,8,1,2,3,4,7] 
#lma4 = (sorted(lambda u : u*2 ))
#print(lma4)