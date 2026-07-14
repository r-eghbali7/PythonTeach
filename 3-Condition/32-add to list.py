had = int(input("meghdar ra moshkhas konid:"))
z = []
count = 0 
while count <= had :
    add = int(input("add ha ro moshakhs konid: "))
    if add % 2 == 0 :
        z.append(add)
        print(z)
    count += 1 