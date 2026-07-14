# Function
# def 

# def 
# def name-def () :
#       .
#       .
#       .
#       print() // return()
# 
# name-def ()

def print_name () : 
    daneshjo_1 = "saeed molaye "
    daneshjo_2 = "samane samete"
    print(daneshjo_1,"\t",daneshjo_2)

print_name()

print(40*"-")

def name_university (daneshgah_1,daneshgah_2,daneshgah_3) :

    return(daneshgah_1,daneshgah_2,daneshgah_3)

print(name_university("azad_rasht","gilan","azad lahijan"))
    
print(40*"-")

def moshakhasat_daneshjo () :
    sen_1 = 25
    sen_2 = 20
    nomre_1 = 15
    nomre_2 = 17
    print_name()
    print(name_university("anzali","somesara","hajibakande"))
    print(sen_1,sen_2,nomre_1,nomre_2)

moshakhasat_daneshjo()

print(40*"-")

def input_add() :
    add_Aval = int(input("enter num1 : "))
    add_dovm = int(input("enter num2 : "))
    sum = add_Aval + add_dovm
    return(add_Aval,add_dovm,sum)

farakhane = input_add()
print(farakhane)