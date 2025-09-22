data = open("input4.txt","r",encoding="utf-8").read()
pairs = data.splitlines()
contained = 0

for p in pairs:
    e1 = [int(p.split(",")[0].split("-")[0]) , int(p.split(",")[0].split("-")[1])]
    e2 = [int(p.split(",")[1].split("-")[0]) , int(p.split(",")[1].split("-")[1])]

    if e1[0] >= e2[0] and e1[1] <= e2[1]:
        contained += 1
    elif e1[0] <= e2[0] and e1[1] >= e2[1]:
        contained += 1
print(contained)

# part 2
contained = 0
for p in pairs:
    #print(p)
    e1 = [int(p.split(",")[0].split("-")[0]) , int(p.split(",")[0].split("-")[1])]
    e2 = [int(p.split(",")[1].split("-")[0]) , int(p.split(",")[1].split("-")[1])]

    if e1[0] >= e2[0] and e1[0] <= e2[1]:
        contained += 1
    elif e1[1] >= e2[0] and e1[1] <= e2[1]:
        contained += 1
    elif e1[0] >= e2[0] and e1[1] <= e2[1]:
        contained += 1
    elif e1[0] <= e2[0] and e1[1] >= e2[1]:
        contained += 1
print(contained)