range = 1000
num1 = 0
num2 = 1
fibonacci = num2
# = 1
sum = 0

#WHILE STATEMENT FOR FINDE DE FØRSTE 1000 FIBONACCI
#while count <= range:

while fibonacci <= range:
	#count += 1
	num1, num2 = num2, fibonacci
	fibonacci = num1 + num2
	if fibonacci % 2 == 0:
		print(fibonacci, end="\n")
		sum += fibonacci

print("Summen af de lige fibonacci numbers fra 0-1000 =", sum)