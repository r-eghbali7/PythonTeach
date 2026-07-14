tadad_daneshjo = 0

tadad_vorode = int(input("chand daneshjo:"))
while tadad_daneshjo <= tadad_vorode :
    dict_daneshjo = {"shomare":int(input("shomare:")),"asm":input("asm:"),"age":int(input("age:"))}
    tadad_daneshjo += 1
    print(dict_daneshjo)

    if karbar := input("if you have 'exit' type exit else press Enter: ") == "exit": # karbar = "exit"
        pass
    else :
        continue
    break

