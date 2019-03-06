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

# name = input('Enter your name: ')
#
# age = -1
#
# try:
# 	age = int(input('Enter your age: '))
# except ValueError:
# 	print('\n''That was not an Integer for your age')
#
# print('Name: ', name)
# print('Age:', age)

# 4.16.6: Temperature Converter using Try and Except
# Connor
# 2.20.19
# def celcius_to_fahrenheit(celcius):
# 	return celcius * 1.8 + 32
#
# def fahrenheit_to_celcius (fahrenhei):
# 	return (fahrenheit - 32) / 1.8
#
# try:
# 	c = float(input('Enter a Temp in Celcius: '))
# 	print('In F:', round(celcius_to_fahrenheit(c), 2))
#
# 	f = float(input('Enter a Temp in Fahrenheit: '))
# 	print('In C:', round(fahrenheit_to_celcius(f), 2))
#
# except ValueError:
# 	print('You must Enter a Float!')


#4.16.7: Enter a Positive Number
# Connor
# 2.21.19

def retrieve_positive_number():
	while True:
		try:
			number = int(input('Enter a Positive number: '))
			if number > 0:
				return number
			else:
				print('The number must be positive, silly.')
		except ValueError:
			print('That was not a number.')
retrieve_positive_number()


# 4.14.6: Print sum
# Connor
# 2.19.19

def print_sum(x, y):
	print(x + y)

print_sum(48, 2345)
