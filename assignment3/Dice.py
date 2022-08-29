import random
i=0
while True:
    number=random.randint(1,6)
    print(number)
    i=i+number
    if number != 6:
        continue
    else:
        break
print('The sum is equal to:',i)