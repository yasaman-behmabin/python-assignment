num = int (input('please enter the number : '))
if (num % 7 == 0):
    print (num ,': it is a multiple of seven.')
else:
    result = 7 - num % 7 + num 
    print (num ,': it is not a multiple of seven.\n',result,': the next  multiple of seven.')
    