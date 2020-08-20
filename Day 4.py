Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list=[1,2,3,4,5]
>>> my_list[0]
1
>>> my_list[1]
2
>>> my_list[2]
3
>>> my_list[3]
4
>>> my_list[4]
5
>>> for my_data in my_list:
	print{my_data}
	
SyntaxError: invalid syntax
>>> for my_data in my_list
SyntaxError: invalid syntax
>>> for my_data in my_list:
	print(my_data)

	
1
2
3
4
5
>>> my_data
5
>>> print(my_data)
5
>>> for w in range(0,10):
	print(w)

	
0
1
2
3
4
5
6
7
8
9
>>> user_1={'username':'semosky','id':101}
>>> user_2={'username':'simeon','id':102}
>>> user_3={'username':'onyebuchi','id':103}
>>> user_4={'username':'nwani','id':104}
>>> user_5={'username':'adebayo','id':105}
>>> my_users=[user_1,user_2,user_3,user_4,user_5]
>>> for user in my_users:
	print(user)

	
{'username': 'semosky', 'id': 101}
{'username': 'simeon', 'id': 102}
{'username': 'onyebuchi', 'id': 103}
{'username': 'nwani', 'id': 104}
{'username': 'adebayo', 'id': 105}
>>> for user in my_users:
	print(user['username'])

	
semosky
simeon
onyebuchi
nwani
adebayo
>>> user_2={'username':'simeon','id':102,'email':'simeon@gmail.com'}
>>> user_3={'username':'onyebuchi','id':103,'email':'onyebuchi@gmail.com'}
>>> user_5={'username':'adebayo','id':105,'email':'adebayo@gmail.com'}
>>> my_users=[user_1,user_2,user_3,user_4,user_5]
>>> for user in my_users:
	print(user['email'])

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    print(user['email'])
KeyError: 'email'
>>> for user in my_users:
	if 'email' in user:
		print(user['email'])

		
simeon@gmail.com
onyebuchi@gmail.com
adebayo@gmail.com
>>> selected_user={}
>>> my_user_lookup=2
>>> for user in my_users:
	if 'id' in user:
		if user['id']==my_user_lookup:
			selected_user=user
			print(selected_user)

			
>>> 
>>> print(selected_user)
{}
>>> 
>>> selected_user={}
>>> my_user_lookup=102
>>> for user in my_users:
	if 'id' in user:
		if user['id']==my_user_lookup:
			selected_user=user

			
>>> print(selected_user)
{'username': 'simeon', 'id': 102, 'email': 'simeon@gmail.com'}
>>> for user in my_user:
	if 'id' in user:
		if user['103']:
			print(103)

			
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    for user in my_user:
NameError: name 'my_user' is not defined
>>> simeon={}
>>> lookup=103
>>> for user in my_user:
	if 'id' in user:
		if user['id']==lookup:
			simeon=user

			
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    for user in my_user:
NameError: name 'my_user' is not defined
>>> 
>>> simeon={}
>>> lookup=103
>>> for user in my_users:
	if 'id' in user:
		if user['id']==lookup:
			simeon=user

			
>>> print(simeon)
{'username': 'onyebuchi', 'id': 103, 'email': 'onyebuchi@gmail.com'}
>>> simeon={}
>>> lookup='onyebuchi@gmail.com'
>>> for user in my_users:
	if 'email' in user:
		if user['email']==lookup:
			simeon=user

			
>>> print(simeon)
{'username': 'onyebuchi', 'id': 103, 'email': 'onyebuchi@gmail.com'}
>>> user_2={'username':'simeon','id':102,'email':'simeon@gmail.com','age':'20'}
>>> user_3={'username':'onyebuchi','id':103,'email':'onyebuchi@gmail.com','age':'20'}
>>> user_5={'username':'adebayo','id':105,'email':'adebayo@gmail.com,'age':'20'}
>>> my_users=[user_1,user_2,user_3,user_4,user_5]
	    
SyntaxError: multiple statements found while compiling a single statement
>>> user_2={'username':'simeon','id':102,'email':'simeon@gmail.com','age':'20'}
>>> user_3={'username':'onyebuchi','id':103,'email':'onyebuchi@gmail.com','age':'20'}
>>> user_5={'username':'adebayo','id':105,'email':'adebayo@gmail.com,'age':'20'}
	
SyntaxError: invalid syntax
>>> user_5={'username':'adebayo','id':105,'email':'adebayo@gmail.com,'age':'20'}
	
SyntaxError: invalid syntax
>>> my_users=[user_1,user_2,user_3,user_4,user_5]
>>> print(my_users)
[{'username': 'semosky', 'id': 101}, {'username': 'simeon', 'id': 102, 'email': 'simeon@gmail.com', 'age': '20'}, {'username': 'onyebuchi', 'id': 103, 'email': 'onyebuchi@gmail.com', 'age': '20'}, {'username': 'nwani', 'id': 104}, {'username': 'adebayo', 'id': 105, 'email': 'adebayo@gmail.com'}]
>>> for user in my_users:
	if 'age' in user:
		print(user['age'])

		
20
20
>>> simeon={}
>>> lookup=20
>>> for user in my_users:
	if 'age' in user:
		if user['age]==lookup:
			
SyntaxError: EOL while scanning string literal
>>> simeon={}
>>> lookup=20
>>> for user in my_users:
	if 'age' in user:
		if user['age']==lookup:
			simeon=user

			
>>> print(simeon)
{}
>>> simeon={}
>>> lookup='20'
>>> for user in my_users:
	if 'age' in user:
		if user['age']==lookup:
			simeon=user

			
\
>>> print(simeon)
{'username': 'onyebuchi', 'id': 103, 'email': 'onyebuchi@gmail.com', 'age': '20'}
>>> user_2={'username':'simeon','id':102,'email':'simeon@gmail.com','age':20}
>>> user_3={'username':'onyebuchi','id':103,'email':'onyebuchi@gmail.com','age':20}
>>> my_users=[user_1,user_2,user_3,user_4,user_5]
>>> print(my_user)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    print(my_user)
NameError: name 'my_user' is not defined
>>> print(my_users)
[{'username': 'semosky', 'id': 101}, {'username': 'simeon', 'id': 102, 'email': 'simeon@gmail.com', 'age': 20}, {'username': 'onyebuchi', 'id': 103, 'email': 'onyebuchi@gmail.com', 'age': 20}, {'username': 'nwani', 'id': 104}, {'username': 'adebayo', 'id': 105, 'email': 'adebayo@gmail.com'}]
>>> for x in range(0,30):
	for user in my_users:
		if user['age']==x:
			print(user)

			
Traceback (most recent call last):
  File "<pyshell#131>", line 3, in <module>
    if user['age']==x:
KeyError: 'age'
>>> for x in range(0,30):
	print(x)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
>>> if user in my_users:
	if 'age' in user:
		if user['age']== x:
			print(x)

			
>>> print(x)
29
>>> for x in range(0,30):
	for user in my_user:
		if 'age' in user:
			if user['age']== x:
				print(x)

				
Traceback (most recent call last):
  File "<pyshell#149>", line 2, in <module>
    for user in my_user:
NameError: name 'my_user' is not defined
>>> for x in range(0,30):
	for user in my_users:
		if 'age'in user:
			if user['age']==x:
				print(x)

				
20
20
>>> for x in range(0,30):
	for user in my_users:
		if user['age']==x:
			print(user)

			
Traceback (most recent call last):
  File "<pyshell#160>", line 3, in <module>
    if user['age']==x:
KeyError: 'age'
>>> for x in range(101,106):
	for user in my_users:
		if user['id']==x:
			print(user)

			
{'username': 'semosky', 'id': 101}
{'username': 'simeon', 'id': 102, 'email': 'simeon@gmail.com', 'age': 20}
{'username': 'onyebuchi', 'id': 103, 'email': 'onyebuchi@gmail.com', 'age': 20}
{'username': 'nwani', 'id': 104}
{'username': 'adebayo', 'id': 105, 'email': 'adebayo@gmail.com'}
>>> for x in range(10,21):
	for user in my_users:
		if 'age' in user:
			if user['age']==x:
				print(user)

				
{'username': 'simeon', 'id': 102, 'email': 'simeon@gmail.com', 'age': 20}
{'username': 'onyebuchi', 'id': 103, 'email': 'onyebuchi@gmail.com', 'age': 20}
>>> 