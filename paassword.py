"""def password(x,y):
    strx= False
    if type(x) is str:
        strx= True
    if strx ==False:
        print("Email not a string")
        return 
    tx=False
    if strx ==True:
        for i in x:
            if i == "@":
                tx=True
                print("Valid Email")
    if tx==False:
        print("No @ in email")
        return
    
    stry= False
    if type(x) is str:
        stry= True
    if stry ==False:
        print("Passswrod not a string")
        return "Password not a string"
    ty=False
    ty1=False
    ty2=False
    count = 0
    if stry ==True:
        for i in y:
            count+=1
            if count >=8:
                ty =True
    if len(y)<8:
        return "Error: >8 charcters needed"
    
    if ty==True:
        for i in y:
            if i is str.isdigit:
                ty1 =True
    if ty1 ==False:
        print("You need an digit in password")
        return
    if ty1 == True:
        for i in y:
            if i is str.isupper:
                ty2 =True
                print("Valid Password")
    if ty2 == False:
        print("You need at least 1 capatilize")
        return
    if ty2 == True and tx ==True:
        print ("ee")



password("eee@ee","11")"""

def create_user(e,p):
    e=e.strip()
    p=p.strip()

    if not isinstance(e,str) or not isinstance(p,str):
        print("error:email +password be strings")
        return
    if "@" not in e:
        print("error:email need @")
        return
    if len(p)<8:
        print("error:password >=8 charcters")
        return
    if not any(ch.isdigit() for ch in p):
        print("error password>=1 number")
        return
    if not any(ch.isupper() for ch in p):
        print("error:password >=1 upper lettter")
        return"Error:password >=1 upper lettter"
    print(e,p)
    
create_user("@","1Ee                          e")