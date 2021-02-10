def delenie(*nums):
 try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second numbers: '))
    result = num1 / num2
    return result
 except:
    print('Warning! Division on 0 is impossible')

print(f'result {delenie()}')

