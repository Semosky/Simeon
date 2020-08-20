Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> simeon=[1,2,3,4,5]
>>> simeon_sq=[]
>>> for num in simeon:
	new_num=num**2
	simeon_sq.append(new_num)

	
>>> print(simeon_sq)
[1, 4, 9, 16, 25]
>>> is_eve=[]
>>> is_even=[]
>>> is_odd=[]
>>> is_a_factor_of_3=[]
>>> for num in simeon_sq:
	if num % 3==0
	
SyntaxError: invalid syntax
>>> is_even=[]
>>> is_odd=[]
>>> is_a_factor_of_3=[]
>>> for num in simeon_sq:
	if num % 3==0:
		is_a_factor_of_3.append(num)
	elif num % 2==0:
		is_even.append(num)
	else:
		is_odd.append(num)

		
>>> print(is_a_factor_of_3, is_even, is_odd)
[9] [4, 16] [1, 25]
>>> 