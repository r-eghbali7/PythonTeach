# Function
# def

def maximum (x,y,z) : 
    print(max(x,y,z))

maximum (10, 15, 12)

print(40*"-")

def megdar_moteghayer (q=5, w=6, e=7) : 
    return(q, w, e)

print(megdar_moteghayer())

print(40*"-")

def halat_3 (r, t="salam", u="woow") : 
    return(r, t, u)

print(halat_3(10))

print(40*"-")

def dict (i, o, p) :
    return(i, o, p)

d = {'i':2 , 'o':3 , 'p':4} ; dict(**d)
print(d)
