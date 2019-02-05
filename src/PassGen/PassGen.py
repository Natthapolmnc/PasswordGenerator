import random as rd

def genPass(num , length):
    print ("Password Generator")
    print ("===================\n")
    numpass=num
    lenpass=length
    AlphaLcase=[ chr(m) for m in range(65, 91)]
    AlphaCcase=[ chr(n) for n in range(97, 123)]
    Intset=[ chr(p) for p in range(48,58)]
    listsetpass=[]
    for j in range(lenpass):
        randAlphaset=rd.randint(2,lenpass)
        randAlphaL=rd.randint(1,randAlphaset)
        randAlphaH=randAlphaset-randAlphaL
        randIntset=lenpass-randAlphaset
        password=[]
        strpassword=""
        for i in range(randAlphaH):
            randindexAlphaH=rd.randint(0,len(AlphaCcase)-1)
            password.append(AlphaCcase[randindexAlphaH])
        for k in range(randAlphaL):
            randindexAlphaL=rd.randint(0,len(AlphaLcase)-1)
            password.append(AlphaLcase[randindexAlphaL])
        for l in range(randIntset):
            randindexInt=rd.randint(0,len(Intset)-1)
            password.append(Intset[randindexInt])
        for u in range(len(password)):
            rd.shuffle(password)
            strpassword+=str(password[u])
        listsetpass+=[strpassword]
    return listsetpass
