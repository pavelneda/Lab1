import sys
StrNumbers="".join(sys.argv[1:])
def count(numbers):
    try:
        return eval(numbers)
    except:
        return None
print(count(StrNumbers))


