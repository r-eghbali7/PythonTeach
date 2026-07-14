import random
x = []
add_random = random.randint(1,100)
x.append(add_random)
while True : 
    add_karbar = int(input("add_karbar: "))
    list_add = [add_karbar]
    if list_add > x:
        print("add kochik tar antekhab kon!!!!!!!!!")
    elif list_add == x :
        print("hamin add:",x," afarin")
        break
    else:
        print("add bozorg tar antekhab kon!!!!!!!!!")
    #add_karbar += 1
