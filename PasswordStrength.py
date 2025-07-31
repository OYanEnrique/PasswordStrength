#Password Strength, Account creator and Log in
print('Checking the strength of your password')
user=input('Create a username:\n')
password= input('Create a password:\n')
length=len(password)
if length < 8:
	print('Weak Password, try a password with more caracters! ')
elif length <= 12:
		print('Ok Password, But it could have more caracters!\n')
else:
		print('Strong Password!\n')
		
	
while length <= 12:
	password=input('Create a password:\n')
	length=len(password)
	if length < 8:
		print('Weak Password, try a password with more caracters! ')
	elif length <= 12:
		print('Ok Password, But it could have more caracters!\n')
	else:
		print('Strong Password!\n')
		break

user_login=input('Enter your username:\n')
user_password=input('Enter your password:\n')
while user_login != user or user_password != password:	
	print('Invalid username or password')
	user_login=input('Enter your username:\n')
	user_password=input('Enter your password:\n')
if user_login == user and user_password == password:
	print('Logged in!')