range = 1000
num1 = 0
num2 = 1
fibonacci = num2
count = 1

while fibonacci <= range:
	print(fibonacci, end="\n")
	count += 1
	num1, num2 = num2, fibonacci
	fibonacci = num1 + num2