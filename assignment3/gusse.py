import random
print('Welcome to the game :) \n Choose a number between 0 and 99 in your mind')
num1 = 0
num2 = 99
number = random.randint(num1,num2)
 
while True:
    print('Is this ',number,'(Yes/No)')
    answer = input ()

    if answer == 'Yes':
        print('you won.')
        break

    elif answer == 'No':
        guess = input('Is it bigger or smaller ? ')
        if guess == 'bigger':
            num1 =  number + 1
            number = random.randint(num1,num2)
        elif guess == 'smaller':
            num2 = number - 1
            number = random.randint(num1,num2)
        else:
            print('The number is not in the range.')
            continue
    else:
        print('answer should be between Yes or No.')
        continue