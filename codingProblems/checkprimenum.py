
'''
prime num has no other factors except 1 and the number itself'''


num = int(input('enter da number bro lol lmao wow '))


flag = False

if  num > 1:
   for i in range(2,num):
      if (num%i) == 0:
         flag= True
         break

      
# check if flag is True
if flag :
   print('the num is not prime')
else : 
   print('the num is prime')