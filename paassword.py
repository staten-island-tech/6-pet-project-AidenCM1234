def password(x,y):
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
    if ty==False:
        print(">8 charcters needed")
        return
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
    if ty2 == False:
        print("You need at least 1 capatilize")
        return




password("eee@ee","aa11111aaaaaaaaaaa")
