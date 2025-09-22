maxCalories = 0
secCalories = 0
thirdCalories = 0
calories = 0
empty = 0

file = open("input1.txt","r",encoding="utf-8")

while True:
        rivi = file.readline()
        rivi = rivi.rstrip("\n")      
        if len(rivi) == 0:
            empty += 1
            if calories > maxCalories:
                thirdCalories = secCalories
                secCalories = maxCalories
                maxCalories = calories
            elif calories >secCalories:
                thirdCalories = secCalories
                secCalories = calories
            elif calories > thirdCalories:
                thirdCalories = calories
            calories = 0
            if empty == 2:
                break
        else:
            calories += int(rivi)
            empty = 0

print(maxCalories)
max3Calories = maxCalories + secCalories + thirdCalories
print(max3Calories)