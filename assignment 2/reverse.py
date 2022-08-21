number = (int(input('please enter your number ; ')))
num = number
reverse = 0
while (number > 0):
    newnum = number % 10
    reverse = ((reverse * 10) + newnum)
    number //= 10
if num == reverse:
    print(reverse , ":the number is equal to it's reverse . ")
else:
    print(reverse , ":the number is not equal to it's reverse . ")