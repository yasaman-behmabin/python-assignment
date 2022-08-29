password = 1234
i = 0
while True:
    userpass = int(input('please Enter your password: '))
    
    if 1000<=userpass<=9999:
        i =i+1
        if userpass == 4321:
            print('Alert for you ...!!! Reverse password entered. The police are aware')
            break
        elif userpass == password:
            print('** ..Welcome..  **')
            break
        elif i < 3:
            print('Your password is wrong, Please try again!')
        elif i == 3:
            print('Your account is locked! Please try later.')
            break
    else:
        print('Try again!')