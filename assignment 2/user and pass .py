username='yasaman behmabin'
Password = '1881'
i=0
for i in range (3):
    user = input ('please enter your Username : ')
    pass1 = input ('please enter your Password : ')
    if (user == username) and (pass1 == Password):
        print ('welcom :)))')
        break
    elif (user != username) or (pass1 != Password):
        if (i == 2):
            print ('your account has been locked, please try again later...')
            break
        print ('your username or password is incorrect.please try again...')

        i += 1 

