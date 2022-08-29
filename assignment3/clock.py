selection = input('Which conversion do you want?: \n 1. hours to seconds \n 2. second to hour \n Selection : ')

if selection == '1':
    Time_h = int(input('Enter the hour : '))
    Time_m = int(input('Enter the min : '))
    Time_s = int(input('Enter the sec : '))
    Time = print('Time : ',Time_h ,' : ',Time_m ,' : ',Time_s ,' : ')
    NewTime = (Time_h * 3600) + (Time_m * 60) + (Time_s)
    print('time convert : ',NewTime,)

elif selection == '2':
    second = int (input('Enter second : '))
    Time_h = second // 3600
    Time_m = (second % 3600) // 60
    Time_s = (second % 3600) % 60
    print ('time convert : ',Time_h,' : ',Time_m,' : ',Time_s,)

else:
    print('please use available options.')
