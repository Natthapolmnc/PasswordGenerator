def cipherShift(mess, shift) :  
    c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cL="abcdefghijklmnopqrstuvwxyz"
    cipher=""
    message=mess
    d=str(shift)
    i=0
    j=0
    while len(cipher)!=len(message):
        if message[i] in c:
            if message[i]==c[j]:
                cipher+=c[(j+int(d))%26]
                i+=1
                j=0
                continue
            j+=1
        elif message[i] in cL:
            if message[i]==cL[j]:
                cipher+=cL[(j+int(d))%26]
                i+=1
                j=0
                continue
            j+=1
        else :
            cipher=message
            break
    if cipher==message:
        print ("something wrong with your input")
        return "INVALID INPUT"
    else:
        return cipher
