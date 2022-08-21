win=0
loss=0
equal=0
score=0
i=1
point=0
while i<=8:
    print('please enter the result\n(win=3,equal=1 ,loss=0)',i)
    point=int(input('your point:'))
    print('----------------------------------------')
    
    if point==3:
      win+=1
      score+=1
      i+=1
    elif point==0:
      loss+=1
      score+=0
      i+=1
    elif point==1:
      equal+=1
      score+=1
      i+=1
    else:
      print('please try again.')
      i-=1
      i+=1
print('your fanail score is:',score,'\n and the result of games.\n your wins:',win,' \n your loss:',loss, '\n equal point:',equal)