# generator
# yield     next()

def generator ():
    for i in range(10) : 
        yield i**2

x = generator()
print(next(x))  # 0 ** 2 = 0 
print(next(x))  # 1 ** 2 = 1
print(next(x))  # 2 ** 2 = 4
print(next(x))  # 3 ** 2 = 9

print(40 * "-")

def list_asame ():
    asmha = ["samane","sosan","sajad","saman"]
    nomre = [20,15,17,16]
    for i in zip(asmha,nomre):
        yield i

yield_shodn = list_asame()
print(list(next(yield_shodn)))   # ['samane', 20]
print(list(next(yield_shodn)))   # ['sosan', 15]
