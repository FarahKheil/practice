attempts = 3
username = 'admin'
password = 1234
while attempts > 0:
   user_input1 = str(input("enter your username : "))
   user_input2 = str(input("enter your password : "))
   if user_input1 ==str ('admin') and user_input2 == str(1234):
          user_input3 = int(input('enter  N: '))
          for i in range(1, user_input3, 2):
              print(i%user_input3)
              break
   else :
      attempts -=1
else:
    print('account locked')
    
     
    