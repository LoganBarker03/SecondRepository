count = 0 

def guessingRed():
  guess = input('What color is the last color in the visible spectrum')
  global count 
  count = count + 1
  if (guess!= 'red'):
        guessingRed()

def guessingOrange():
  guess = input('What color in fruits and vegetables comes from carotene')
  global count
  count = count + 1 
  if(guess!= 'orange'):
        guessingOrange()

def guessingYellow():
  guess = input('What is my favorate color')
  global count
  count = count + 1 
  if(guess!= 'yellow'):
        guessingYellow()

def guessingGreen():
  guess = input('What was George Washingtons favorate color')
  global count
  count = count + 1 
  if(guess!= 'green'):
        guessingGreen()

def guessingBlue():
  guess = input('What is the worlds favorate color')
  global count
  count = count + 1 
  if(guess!= 'blue'):
        guessingBlue()        


print('Color test')
guessingRed()
print('Nice')
guessingOrange()
print('Good Job')
guessingYellow()
print('Wow')
guessingGreen()
print('Youre smart')
guessingBlue()
print('All done')
if count < 7:
    print("You are very smart")
elif count <10:
    print('Learn your colors better')
else:
    print('Are u color blind?')