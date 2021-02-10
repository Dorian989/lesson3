def stepen(x, y):
    x = int(input('Enter first number: '))
    y = int(input('Enter second negative number: '))
    res = (x ** y) * y ** 1/y
    return res

step = stepen('', '')
print(f' result - {step}')

