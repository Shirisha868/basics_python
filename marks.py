name=input()
marks=int(input())
if(marks>=90):
   grade="A grade"
elif(marks>=80 and marks<=89):
   grade="B grade"
elif(marks>=70 and marks<=79):
    grade="C grade"
elif(marks>=60 and marks<=69):
    grade="D grade"
else:
    grade="oops! you got failed, better luck next time"
print(grade)