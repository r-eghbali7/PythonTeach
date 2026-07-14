# Data structure type ---- انواع داده 
# string format
# انواع داده سطح ۱
# % (%c  %d  %e  %f  %r  %o  %x)     .format()       f

# Operator % (%i  %c  %s  %d  %e(namad elme)  %f  %r  %o  %x(mabna16)
a ,b = (2,3)
print("a is: %i\n y is: %i :"%(a,b))

add = (65,66)
print("character: %c %c"%(add))

asm = "ali"
print("asm:%s"%asm)

num = 1
print("float=%d"%(num))

flot = 2.2587955
print("float%.2f"%flot)

reshte = "BENEVIS"
print("benvis:%r nvestam 2 ta add: %i , %i"%(reshte,a,b))

print(40*"-")

x, y = 20,33
print("magmo do add {} + {} =53 ".format(x,y))

d = {"k" : 6 , "l" : 5}
print("k is:{k} \n l is :{l}".format(**d))

print(40*"-")

f = "best"
e = 50
print(f"who is  {f} player in the world?   {e} goles in match ")
print(f"who is '{f}' player in the world? '{e}' goles in match ")
