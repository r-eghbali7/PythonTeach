# Function
# neshangarha def


def neshangar (a,c,*,d) :
  
    print(a,"\t",c,"\t",d)
  
neshangar("ali",3,d=8)

print(40 * ("-"))

def neshangar2 (q,w,e,/,r) :
    
    return(q,"\t",w,e,r)  

print(neshangar2(10,3,"samira",r="woow"))    

print(40 * "-")

def neshangar3 (x:int ,y:str ,z:list) :

    print(x,"\t",y,"\t",z)

(neshangar3(5,"salam",["oooo",25,["jook"]]))