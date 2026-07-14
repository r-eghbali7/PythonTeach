# decorator
# decorator = 1- درتابع تو در تو تابع داخلی تابه دیکوریتور هست
# 2- @ بالای تابع دیگر فراخوانی کنیم با

# decorator 1
# defining a decorator
def hello_decorator(func):
 
    def inner1():
        print("Hello, this is before function execution")
 
        func()
 
        print("This is after function execution")
         
    return inner1
 
 
def function_to_be_used():
    print("This is inside the function !!")
 
 
function_to_be_used = hello_decorator(function_to_be_used)
 
function_to_be_used()

print(40 * "-")

# decorator 2
def avl (func) :
    def dovom () :
        func()
        a=[1,2,3,4,5,6]
        for i in a:
            b=i**2
            print([b],end="\t",)
        
        
        
    return dovom

@avl
def svome () :
    print("hasel zarb add ha !!!!")    

    def chaharom() :
        a=[1,2,3,4,5,6]
        for i in a:
            b=i**2
            print(b,end="\t",)
        
        print("halat dige!!!!!!!!!!")
    return chaharom()

svome()




