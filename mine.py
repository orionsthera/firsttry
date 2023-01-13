from datetime import datetime
now=datetime.now()
x= (input('Do you want to know the date? \n'))
if x.upper()== 'YES':
    print('%02d/%02d/%04d' % (now.month, now.day, now.year))
else:
    print('OK')

b= (input('Do you want to know the time? \n'))
if b.upper() =='YES':
    print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))
else:
    print('OK')

y=(input('Do you need advice? \n'))
if y.upper() == 'NO':
    print("I couldn't help you anyhow.")
else:
    print('Chase your dreams!')


z= (input('Do you want to play a game? \n'))
if z.upper() == 'YES':
    a= (input('Pick a number \n'))
    if int(a) < 1000:
        print('You win!')
else:
    print('No guts no glory!')


    
    
    
        
    
