filename = input("input your flie name:")
file_extention = filename.split(".")
print("file_extention:",repr(file_extention[1])) # repr del ----> ' '

print(40*"-")

import os
for i in os.listdir():
    if os.listdir != ".":
        b=i.split(".")
        print(b)