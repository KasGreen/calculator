def add_numbers(num1, num2):
	return(num1 + num2)

def subtract_numbers(num1, num2):
	return(num1 - num2)

def multiply_numbers(num1, num2):
	return(num1 * num2)

def divide_numbers(num1, num2):
	if num2 == 0:
		print('Cannot divide by 0')
		return
	return(num1 / num2)

def mod_numbers(num1, num2):
	return(num1 % num2)

def power_of_numbers(num1, num2):
	return(num1 ** num2)

continueCalc = True
while continueCalc == True:
	result = 0
	valid_user_option = False
	valid_num1 = False
	valid_num2 = False
	while valid_user_option == False:
		user_option = input('Would you like to +, -, *, /, % or ^: ')
		if not user_option:
			print('Please enter an operator')
		elif user_option != '+' and user_option != '-' and user_option != '*' and user_option != '/' and user_option != '%' and user_option != '^':
			print('Please enter a valid operator')
		else:
			valid_user_option = True

	while valid_num1 == False:
		try:
			num1 = float(input('Please enter your first number: '))
		except ValueError:
			print('Please enter a number')
		else:
			valid_num1 = True

	while valid_num2 == False:
		try:
			num2 = float(input('Please enter your second number: '))
		except ValueError:
			print('Please enter a number')
		else:
			valid_num2 = True

	if user_option == '+':
		result = add_numbers(num1, num2)
	elif user_option == '-':
		result = subtract_numbers(num1, num2)
	elif user_option == '*':
		result = multiply_numbers(num1, num2)
	elif user_option == '/':
		result = divide_numbers(num1, num2)
	elif user_option == '%':
		result = mod_numbers(num1, num2)
	elif user_option == '^':
		result = power_of_numbers(num1, num2)

	print(result)
	validAnswer = ''
	while validAnswer != 'y' and validAnswer != 'n':
		validAnswer = input('Would you like to perform another calculation y/n: ')
		if validAnswer == 'y':
			break
		if validAnswer == 'n':
			continueCalc = False