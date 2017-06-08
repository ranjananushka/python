import math
firts_number=int(input("enter the first number"));
second_number=int(input("enter the second number"));
print("Available operation ");

options = {0 : 'multiply',
           1 : 'divide',
           2 : 'add',
           3 : 'sub',
           4 : 'remainder',
           5 : 'reciprocal',
           6 : 'underroot',
           7 : 'log base 10',
           8 :  'exponential',
          }
print(options);
a=input("select your operation")
if(a=='0'):
    result=firts_number*second_number
    print("result=" , result)
elif(a=='1'):
    result = firts_number / second_number
    print("result=" , result)
elif(a=='2'):
    result = firts_number + second_number
    print("result=" , result)
elif(a=='3'):
    result = firts_number - second_number
    print("result=" , result)
elif(a=='4'):
    result = firts_number % second_number
    print("result=" , result)
elif(a=='5'):
    result = 1/firts_number
    print("result=" , result)
elif(a=='6'):
    result=math.sqrt(firts_number)
    result1 = math.sqrt(second_number)
    print("squareroot of first number",result)
    print("squareroot of second number", result1)
elif(a=='7'):
    result=math.log10(firts_number)
    result1 = math.log10(second_number)
    print("log of first number", result)
    print("log of second number", result1)
elif(a=='8'):
    result=math.exp(firts_number)
    result1 = math.exp(second_number)
    print("exponential of first number", result)
    print("exponential of second number", result1)
else:
    print("Invalid option selected")
