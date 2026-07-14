# Data structure type ---- انواع داده 
# string operators
# انواع داده سطح ۱ 
# isinstance(_____ , _____) ------> True/false    "  "     '  '   \n    \t    +    *     sliceing [  :  :  ]     \   r   len()

# isinstance(_____ , _____) ------> True/false 
x = "booo" 
y = "4000"
z = 98465
print(isinstance(x, str))
print(isinstance(y, str))
print(isinstance(z, str))

print(40*"-")

# ' '  " "
q = "loooo"
w = 'joooo'
print("q:",type(q))
print("w:",type(w))

print(40*"-")

# \n   \t 
e = "sooo \n  pooo"
r = 'kooo \t aooo'
print("e:",e)
print("r:",r)

print(40*"-")

# +   *
t = "parsa"
i = "mohammad"
o = "kobra"
print("t+i:",t+i)
print("o*3:",o*3)

print(40*"-")

# sliceing [  :  :  ]
u = "ali be bazar raft"
print("u[ 0 : 3 ]:",u[0 : 3])
print("u[ : 3 ]:",u[ :3])
print("u[ 5 : ]:",u[5: ])
print("u[ 0 : ]:",u[0: ])
print("u[ 3 : -1 ]:",u[ 3 : -1 ])
print("u[ 0: : 2 ]:",u[0::2])
print("u[ 0: 8:0 ]:",u[0: 8 :1])
print("u[ : : -1 ]:",u[ : : -1 ])

print(40*"-")

# r 
s = (r"best team \t in the \n woreld")
d = ("best team \\t in the \\n woreld")
print("s:", s)
print("d:", d)

print(40*"-")

# len()
c="teach python in uni"
print("c:",len(c))
