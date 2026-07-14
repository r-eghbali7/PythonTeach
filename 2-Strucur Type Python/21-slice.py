# Data structure type ---- انواع داده
# slice ----> itreable and index -----> list _ tuple _ string  

# list

my_list = [1,2,3,4,5,6,7,8,9]
for i in dir(my_list):
    if i == 'index' and '__iter__' : 
        print(True)

print("1_",my_list[:])

print("2_",my_list[0:])

print("3_",my_list[:0])

print("4_",my_list[:5])

print("5_",my_list[2:7])

print("6_",my_list[2::2])

print("7_",my_list[5::-2])

print("8_",my_list[:6:-1])

print("9_",my_list[::-1]) # -----> revers

print("10_",my_list[::-50])

print("11_",my_list[::50])

print("12_",my_list[5::50])

print("13_",my_list[:6:50])

print("14_",my_list[:6:-50])

print(40 * "-")

# tuple

my_list_2 = (1,2,3,4,5,6,7,8,9)
for i in dir(my_list_2):
    if i == 'index' and '__iter__' : 
        print(True)

print("1_",my_list_2[:])

print("2_",my_list_2[0:])

print("3_",my_list_2[:0])

print("4_",my_list_2[:5])

print("5_",my_list_2[2:7])

print("6_",my_list_2[2::2])

print("7_",my_list_2[5::-2])

print("8_",my_list_2[:6:-1])

print("9_",my_list_2[::-1]) # -----> revers

print("10_",my_list_2[::-50])

print("11_",my_list_2[::50])

print("12_",my_list_2[5::50])

print("13_",my_list_2[:6:50])

print("14_",my_list_2[:6:-50])

print(40 * "-")

# string

my_list_3 = "bikhial lonte ghasedak to ke band ye fote"
for i in dir(my_list_3):
    if i == 'index' and '__iter__' : 
        print(True)

print("1_",my_list_3[:])

print("2_",my_list_3[0:])

print("3_",my_list_3[:0])

print("4_",my_list_3[:5])

print("5_",my_list_3[2:7])

print("6_",my_list_3[2::2])

print("7_",my_list_3[5::-2])

print("8_",my_list_3[:6:-1])

print("9_",my_list_3[::-1]) # -----> revers

print("10_",my_list_3[::-50])

print("11_",my_list_3[::50])

print("12_",my_list_3[5::50])

print("13_",my_list_3[:6:50])

print("14_",my_list_3[:6:-50])