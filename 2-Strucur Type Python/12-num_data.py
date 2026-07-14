# Data structure type ---- انواع داده 
#membership operators
# انواع داده سطح ۱ 
# numbers   dictionary   boolian    set    sequence type    special

# numbers
num_int = 2
num_flot = 1.25 
num_complex = (2j) + (3j) 
print("num_int:",type(num_int))
print("num_flot:",type(num_flot))
print("num_num_complex:",type(num_complex))

print(40*"-")

# dictionary 
my_dict = {"a" : 2,"b" : 3}
print("my_dict",type(my_dict))

print(40*"-")

# boolian
x = True
y = False
print("x:",type(x))
print("y:",type(y))

print(40*"-")

# set
my_set = set("booob")
print("my_set:",type(my_set))

print(40*"-")

# sequence type 
my_string = "helow"
my_list = [1,2,3,"wooow"]
my_tuple = (1,2,3)
print("my_string:",type(my_string))
print("my_list:",type(my_list))
print("my_tuple:",type(my_tuple))

print(40*"-")

# special
q = None
print("q:",type(q))

print(40*"-")

import fractions
h=2e+7
print(fractions.Fraction(h))

print(40*"-")

p = 256.23
print(pow(p,3))
print(abs(-25564.22213))
print(round(2566.44487874,2))