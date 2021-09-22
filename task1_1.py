import sys
def count(numbers):
    if len(numbers) == 3 and numbers[1] in "/*-+":
        try:
            return eval("".join(numbers))
        except:
            return None
print(count(sys.argv[1:]))


