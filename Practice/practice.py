# attempts = 3
# username = 'admin'
# password = 1234
# while attempts > 0:
#    user_input1 = str(input("enter your username : "))
#    user_input2 = str(input("enter your password : "))
#    if user_input1 ==str ('admin') and user_input2 == str(1234):
#           user_input3 = int(input('enter  N: '))
#           for i in range(1, user_input3, 2):
#               print(i%user_input3)
# #               break
# #    else :
# #       attempts -=1
# # else:
# #     print('account locked')
    

# # def my_function(*girls):
# #     print('the youngest child is: ' + girls[1])
# # my_function('farah', 'noor', 'fatima')
total = 0
print('sum of even numbers from 1 till n:')
n = int(input('enter n: '))
for num in range(1, n+1):
    is_even = True
    if num % 2 == 0:
        total += num
        print(num , end = " " )
print('total=',total)
# def sum_even_numbers(n):
    # total = 0
    # for num in range 
