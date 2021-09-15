from sys import argv
name,func,number1,number2=argv

def add(x,y):
    return x+y
    
def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y
    
print(eval(func+'('+number1+','+number2+')'))
