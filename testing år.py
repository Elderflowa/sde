inputUser = int(input("Enter a number: "))
originalTime = inputUser
år = inputUser // 525600
inputUser = inputUser % 525600
dage = inputUser // 1440
inputUser = inputUser % 1440
timer = inputUser // 60
inputUser = inputUser % 60
minutter =inputUser

print(originalTime, "minutter er lige med", år, "år", dage, "dage", timer, "timer og", minutter, "minutter")
