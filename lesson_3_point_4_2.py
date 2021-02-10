def stepen(x, y):
     result = x
     for i in range(abs(y)-1):
      result = result * x
     return 1/result


print(f'result  {stepen(x = int(input("Enter first number: ")), y = int(input("Enter second negative number: ")))}')

# вроде все работает, но выдает что-то не понятное.



