while True:
  height=float(input('please enter your hieght(m):'))
  weight=float(input('please enter your wieght(Kg):'))
  BMI=(weight/(height**2))
  if(16<=BMI<18.5):
    print('your BMI is:',BMI,'you need to gain your weight. :))')
    break
  elif (18.5<= BMI <24):
    print("Your BMI is: ",BMI, " Congrats! Your weight is Normal. ")
    break
  elif 24 <= BMI < 30:
    print("Your BMI is:",BMI, " You're close to Overweight ! becareful. ")
    break
  elif 30 <= BMI < 35:
    print("Your BMI is: " ,BMI, "You are a little overweight , You need a Diet. ")
    break
  elif 35 <= BMI < 40:
      print("You're BMI is: ", BMI, " You are overweight :(,do exercise.")
      break
  elif BMI >= 40:
      print("You're BMI is ", BMI , ", Your weight is too much ,it's dangrous!!,take care.")
      break
  else:
      print("Information is incorrect!\nPlease try again.")
      continue