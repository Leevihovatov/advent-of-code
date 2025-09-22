data = open("input3.txt","r",encoding="utf-8").read()
sacks = data.splitlines()
sumOfPri = 0
errs = []
badges = []
chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in sacks:
    #print(i)
    c1 = i[:int((len(i)/2))]
    #print(c1)
    c1 = list(c1)
    c1 = list(dict.fromkeys(c1))
    c2 = i[int(len(i)/2):]
    #print(c2)
    c2 = list(c2)
    c2 = list(dict.fromkeys(c2))

    for j in c1:
        for k in c2:
            if j == k:
                errs.append(j)

#print(len(errs))
for e in errs:
    priority = chars.index(e) + 1
    sumOfPri += priority

print(sumOfPri)
##############################################
sumOfPri = 0

for i in range(0,300,3):
    c1 = sacks[i]
    c1 = list(c1)
    c1 = list(dict.fromkeys(c1))
    c2 = sacks[i+1]
    c2 = list(c2)
    c2 = list(dict.fromkeys(c2))
    c3 = sacks[i+2]
    c3 = list(c3)
    c3 = list(dict.fromkeys(c3))

    for j in c1:
        for k in c2:
            if j == k:
                for l in c3:
                    if j == l:
                        badges.append(j)

#print(len(errs))
for b in badges:
    priority = chars.index(b) + 1
    sumOfPri += priority
print(badges)
print(sumOfPri)