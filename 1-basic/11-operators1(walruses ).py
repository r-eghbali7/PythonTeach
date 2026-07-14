# basic ---- ساده
# walruses operators
# :=

#### x = 2
#### s = x+4
#### print(s)

print(x := 4+2)

print(40*"-")

zakhire_nam = []
asm= input("asm:")
while asm.lower() != "q" :
    zakhire_nam.append(asm)
    asm=input("name:")
    print("name:",zakhire_nam)

print(40*"-")

zakhire = []
while (asm1 := input("asm1:")) != "q" :
    zakhire.append(asm1)
    print(zakhire)

