def fibonacciFinder():
	print("Program der finder fibonacci tal!")
	range = input("Skriv max range der skal tjekkes: ")

	if range.isdigit():
		range = int(range)
		num1 = 0
		num2 = 1
		fibonacci = num2
		sum = 0

		while fibonacci <= range:
			num1, num2 = num2, fibonacci
			fibonacci = num1 + num2
			if fibonacci % 2 == 0:
				sum += fibonacci
				printfib = '{0:,}'.format(fibonacci)
				print(printfib, end="\n")
		sum = '{0:,}'.format(sum)
		print("Summen af de lige fibonacci numbers fra 0-1000 =", sum)
	else:
		print("Skriv et rigtigt tal")

fibonacciFinder()