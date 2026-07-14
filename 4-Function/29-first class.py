# Function
# first class


# Functions are objects
def my_number () :
    num = [1,2,3,4,5] 
    res = 0
    for i in num :
        res = i + res   
        
    return(res)

print("my_number: ",my_number())

first = my_number
print("first: ",first())

print(40 * "-")

def def_1(text):
    return text.upper()
  
def def_2(text):
    return text.lower()
  
def daaf(func):
    # storing the function in a variable
    str_daaf = func("""Hi, I am created by a function passed as an argument.""")
    print (str_daaf) 
  
daaf(def_1)
daaf(def_2)

print(40 * "-")

def create_adder(x):
    def adder(y):
        return x+y
  
    return adder
  
add_15 = create_adder(15)
  
print (add_15(10))
