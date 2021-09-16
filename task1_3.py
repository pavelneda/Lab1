st=input()
lst=list(st)
lst.append("\0")

def filtr(l,i=0):
    if l[i] == "\0" :
        print("(True,",str(eval(st))+")")
    else:
            i=i+1
            filtr(l,i)   
        else:
            print("(False, None)")
        
if lst[0].isdigit():
    filtr(lst)
else:
    print("(False, None)") 


