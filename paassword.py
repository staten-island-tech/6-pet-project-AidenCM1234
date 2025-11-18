def password(x,y):
    if x is str:
        eeee
    tx=False
    for i in x:
       if i == "@":
            tx=True
            print("Valid Email")
    if tx==False:
        print("No @")
    ty=False
    ty1=False
    count = 0
    for i in y:
        count+=1
        if count >=8:
            ty =True
    if ty==False:
        print(">8 charcters needed")
    if ty==True:
        for i in y:
            if i is str.isdigit:
                ty1 =True



password("e@gmail.com","12344567")
