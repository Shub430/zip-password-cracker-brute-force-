import zipfile#importing predefined zipfile module

import passwordgenerator#importing passwordgenerator.py to generate password


count =1#Number of tries

name=input("Enter zipfile name :")

min=int(input("minimum length of password is :"))
max=int(input("maximum length of password is :"))
choice=int(input('What does password contain:\n1)Lower Case Alphabet\n2)Upper Case Alphabet\n3)Lower Case Alphabet + Numbers\n4)Upper Case Alphabet + Numbers\n6)Lower Case Alphabet + Symbols\n5)Upper Case Alphabet + Symbols\n7)Lower Case Alphabet + Numbers + Upper Case Alphabet\n8)Lower Case Alphabet + Numbers + Upper Case Alphabet + Symbols\n'))


for password in passwordgenerator.Generator.genpass(minlength=min,maxlength=max,SN=choice):#genetrating password in loop
    try:
        with zipfile.ZipFile(name,'r') as zf:#Openning zip file to operate
            zf.extractall(pwd=bytes(password,'utf-8'))
            data=zf.namelist()[0]
            data_size=zf.getinfo(data).file_size
            print('''-------------------------------\n!!!password found!!! ~%s\n ~%s\n ~%s\n-----------------------------'''
                  %(password,data,data_size))
            break
    except KeyboardInterrupt:
            exit(0)
    except:
        number=count
        print('<%s> - Password failed! - %s'%(number,password))   
        count=count+1
        
