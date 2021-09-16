userIn=input()
lst=list(userIn)
lst.append(" ")

def process(lst,i=0):
    if i+1 == len(lst) :
        return (True,eval(userIn))
    else:
        if lst[i].isdigit() or ((lst[i] == "+" or lst[i] == "-")  and lst[i+1].isdigit()):
            i=i+1
            return process(lst,i)   
        else:
            return (False, None)
        
if lst[0].isdigit():
    print(process(lst))
else:
    print("(False, None)") 


