import sys
import operator

ops={"add": operator.add,"mul":operator.mul,"sub":operator.sub,"div":operator.truediv}
def guard(func,numbers):
    try:
        return ops[func](int(numbers[0]),int(numbers[1]))
    except:
        return None
try:
    func=sys.argv[1]
    numbers=sys.argv[2:]
    print(guard(func,numbers))
except:
    print("Enter parameters")
