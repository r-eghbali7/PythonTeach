# Function
# name space
# built-in      global      enclosing       local

# built-in

a = {1,2,3,4,5,6}
print("a: ",len(a))
print(dir(__builtins__))

print(40 * "-")

# global

#b = int(input("add:"))

#def sum_num () : 
#    return( b + 4 )

#print("sum_num:",sum_num())
#print("b:",b)

# enclosing      local

x = "python"
def enclosing_sapace () :
    x = "c++"
    print ("encloseing:",x)
    def local_space () :
        x = "ruby"
        print ("local:",x)
    return(local_space())

enclosing_sapace()
print(x)