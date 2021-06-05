def sort(s):
    s= input("Enter string : ")
    upp=''
    law=''
    dige=''
    digo=''
    spc=''
    c=0
    for i in s:
        if i.isupper():
            upp+=i
            #print(upp)
        elif i.islower():
            law+=i
        elif i.isdigit():
            #dig+=i
            if (int(i) % 2) == 0:  
               dige+=i
            else:  
                digo+=i 
        elif i==' ':
            c+=1
            #print(c)
        else:
            spc+=i
            #print(spc)
    result=spc+law+' '+upp+' '+dige+' '+digo+' '
    return result
#print (sort('131/265 is where I and Sam Live.'))
print (sort(''))
def main():
	s= ' '
	sort(s)					

if __name__=="__main__":
	main()





