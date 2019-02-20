# 4.16.3: Enter a Number using Try and Except
# Connor
# 2.20.19
#
# try:
# 	my_num = int(input('Enter an interger: '))
# 	print('Your number:', my_num)
#
# except ValueError:
# 	print('\n''That was not an Interger!')



# 4.16.4: Enter Name & Age using the Try & Except Rule
# Connor
# 2.20.19

name = input('Enter your name: ')

age = -1

try:
	age = int(input('Enter your age: '))
except ValueError:
	print('\n''That was not an Integer for your age')

print('Name: ', name)
print('Age:', age)