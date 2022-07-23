import itertools
Upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lower="abcdefghijklmnopqrstuvwxyz"
Num="0123456789"
Sym="`~!@#$%^&*()_-"

# charset='0123456789'
class Generator:
    def genpass(minlength,maxlength,SN):
        # for i in range(len):
        #     password+=random.choice(charset)
        if(SN==1):
            charset=Lower
        elif(SN==2):
            charset=Upper
        elif(SN==3):
            charset=Lower+Num
        elif(SN==4):
            charset=Upper+Num
        elif(SN==5):
            charset=Lower+Sym
        elif(SN==6):
            charset=Upper+Sym
        elif(SN==7):
            charset=Lower+Upper+Num
        elif(SN==8):
            charset=Lower+Upper+Num+Sym
        
        for x in range(minlength,maxlength,1):
            print("Trying password of length ",x)
            for l in itertools.product(charset,repeat = x):
                yield ''.join(l)

