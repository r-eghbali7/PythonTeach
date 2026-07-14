# iterator
# iterate = تکرار کردن 
# iteration = عمل تکرار کردن
# iterable = قابل تکرار ، تکرار پذیر
# iterator = اخرین ابجکت خودشون رو حفظ کند
# __next__ = یک ایتریتور باید درون خودش این متد را داشته باشد
# for = خودش یک لیست رو به ایتریتور تبدیل میکند

# iterator
I = [1,2,3,4,5,6]
i = iter( I )
print(type(i),list(i))
print(type(I),I)
print("__next__" in dir(i) )

print(40 * "-")

# next
a = (55,66,77,88,99)
print("a: ", type(a),"\t",a)
b = iter( a )
print("b: ",type(b),"\t","__next__" in dir(b) )
print("b2:",next(b))
print("b1:",next(b))
print("b3:",next(b)) # 77
