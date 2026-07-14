# Data structure type ---- انواع داده 
# list
# انواع داده سطح ۱
# []    list    immutable\mutable     copy\deepcopy     append()    del()   len()   انتخاب جندگانه

# []
list1 = 1,2,3,4
print(type([list1]),"---->",[list1])

print(40*("-"))

list2 = [5,6,7,8]
print(type(list2),"---->",list2)

print(40*("-"))

list3 = [10,20,30,40] 
list4 = ["ali","mmamd"]
list3.append(list4)
print(type(list3),"---->",list3)

print(type(list3+list4),"---->",print(list3+list4))

print(40*("-"))

list5 = [14,15,16]
print(type(list5),"---->",list5)
print(type(list5),"---->",list5*3)

print(40*("-"))

# list
list6 = list("ali123")
print(type(list6),"---->",list6)

print(40*("-"))

################## list7 = list(1,2,3)
################## print(list7)   --------------> TypeError: list expected at most 1 argument, got 3   /// TypeError: 'int' object is not iterable

# *pint
x = "foot,ball"  
s = x.split(",")
print(type(s),"---->",s)

print(40*("-"))

#immutable\mutable
mylist = ["football","bamshad"]
mylist[0]="seloll"
print("1_",mylist)

del(mylist[0])
print("2_",mylist)

print(len(mylist))

print(40*("-"))

#str1= "foooball"
#str1[3]="sool"
#print(str1)
list7= ["bamda","tes","sadegh"]
del(list7)
#print(list7)   ----------------------------> NameError: name 'list7' is not defined. Did you mean: 'list1'?
f,g,h = 88,99,66
print(f,g,h)
# o,i,u = 111,222,333,444
# print(o,i,u)  ----------------------------> ValueError: too many values to unpack (expected 3)
*v,b,n = 555,666,777,888,999  
print(v,b,n)