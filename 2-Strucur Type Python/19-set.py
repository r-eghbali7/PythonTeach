# Data structure type ---- انواع داده 
# set
# انواع داده سطح ۱
# {}    set()    add()     update()     remove()    discard()     -----(muteble, slice nist ,  ) 

# {}        
set_1 = {1,2,3,4,5,6}
print(type(set_1) , "___",set_1)

# point ########################################
set_2 = {1,2,2,3,4,5,5,5,5,6}  
print(type(set_2),"___", set_2)  

set_3= {"alsam"}
print(type(set_3),set_3)

print(40*"-")

# set()
set_4 = set("salam")
print(type(set_4), "___" , set_4)

set_5 = set([1,2,3,4])
print(type(set_5) , "___", set_5)

set_6 = set([1,2,2,3,4,5,5,5,5,6]) 
print(type(set_6) , "___", set_6)

print(40*"-")

# add()
set_7 = {2,3,4,5}
print(type(set_7) , "___", set_7)
set_7.add(1)
print(type(set_7) , "___" , set_7)

print(40*"-")

# update()
set_8 = {2,3,4,5}
print(type(set_8) , "___", set_8)
set_8.update("a","b","b","c")
print(type(set_8) , "___" , set_8)

print(40*"-")

# remove()
set_9= set([1,2,2,3,4,5,5,5,5,6]) 
print(type(set_9) , "___", set_9)
set_9.remove(3)
print(type(set_9) , "___", set_9)
# set_9.remove()
# print(type(set_9) , "___", set_9)     ------>     TypeError: set.discard() takes exactly one argument (0 given)   

print(40*"-")

# discard()
set_10= set([1,2,2,3,4,5,5,5,5,6]) 
print(type(set_10) , "___" , set_10)
set_10.discard(4)
print(type(set_10) , "___", set_10) 

print(40*"-")

# در ست ها قوانین  محموعه های ریاضی برقرار است
a = {10,11,12,13,14}
b = {14,15,16,17}
print("a - b=" , a - b)
print("a | b=" , a | b)
print("a & b=" , a & b)
print("a ^ b=" , a ^ b)    #  tafazol motegharen          .symmetric_defference()
print("a < b=" , a < b)    # subset                       .issubset()
print("a > b=" , a > b)    # superset                     .issuperset() 