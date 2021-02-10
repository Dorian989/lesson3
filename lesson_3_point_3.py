def my_func():
     arg1 = int(input("enter 1 arg "))
     arg2 = int(input("enter 2 arg "))
     arg3 = int(input("enter 3 arg "))
     if arg1 >= arg3 and arg2 >= arg3:
      return arg1 + arg2
     elif arg1 > arg2 and arg1 < arg3:
      return arg1 + arg3
     else:
      return  arg2 + arg3

print(f' result: {my_func()}')
