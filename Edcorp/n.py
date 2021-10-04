# accept data input
a = input('enter course workarks: ')
b = input('enter test marks: ')
c = input('enter end of sem marks: ')

#function to process depending on the total
def total(): 
    if float(d) >= 60 <= 100:
       print('passed')
    elif float(d) > 100:
       print('Error in marks. Marks can not exceed 100%')
    else:
       print('failed')
       
#data processing depending on input requirements
if float(b) < 15:
   print('failed') 
else:
   d = a + b + c
   total()
  
print('''
 ___ ____ ____ _    ____    _  _ ____ ____ _  _ ____ ____              |  |  | |  | |    [__     |__| |__| |    |_/  |___ |__/
  |  |__| |__| |___ ___]    |  | |  | |___ | \_ |___ |  \
     
     ''')