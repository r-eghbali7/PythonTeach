# attribute function
# setattr()     getattr()   hasattr()

def add_aval ()  :
    a=[2,3,5,7,11,13]
    print(a)

add_aval()

add_aval.ezaf = [17,23,27]  # <--------------
setattr(add_aval,"ezaf",31) # <--------------
setattr(add_aval,"ezaf2",[31,37])
print(add_aval.ezaf)

print("getattr:",getattr(add_aval,"ezaf2"))
print("getattr:",getattr(add_aval,"ezaf4","tamom_shod_add :)"))

print("hasattr:",hasattr(add_aval,"ezaf"))

print(add_aval.__dir__())
print(add_aval.__dict__)
