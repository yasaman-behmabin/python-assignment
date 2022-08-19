n=int(input("Please enter a six-digit number: "))
second_digit=(n//10)%10
fifth_digit=(n//10000)%10
sum=second_digit+fifth_digit
print("the sum of the second and fifth digits=",sum)
