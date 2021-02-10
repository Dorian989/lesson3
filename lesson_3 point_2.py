def my_func():
 try:
    name = str(input('enter name: '))
    surname = str(input('enter surname: '))
    city = str(input('enter city: '))
    mail = str(input('enter email: '))
    age = str(input('enter year: '))
    phone = input('input telephone: ')
 except ValueError:
    return
 return ([name], [surname], [city], [mail], [age], [phone])

print(f'{my_func()}')


