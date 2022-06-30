myNumber=float(input('Enter your number: '))
rem=myNumber %2
if (myNumber>=0 and (rem==0)):
    print('Your number is positive and even')
if (myNumber<0) and (rem==0):
    print('Your number is negavtive and even')
if (myNumber>=0 and (rem==1)):
    print('Your number is positive and odd')
if (myNumber<=0) and (rem==1):
    print('Your number is negavtive and odd')
