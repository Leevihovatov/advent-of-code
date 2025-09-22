data = open("input7.txt","r",encoding="utf-8").read()
lines = data.splitlines()
gg = 0
sames = 0
dirsNow = []
allDirs = []
sizes = []

for i in lines:
    line = i.split()
    #print(dirsNow)
    if line[1] == "cd":
        if line[2] == "..":
            del dirsNow[-1]
        else:
            try: # if same named dirs
                ind = allDirs.index(line[2])
                dir = line[2] + str(sames)
                allDirs.append(dir)
                dirsNow.append(dir)
                sizes.append(0)
                sames += 1
            except ValueError:
                try:
                    ind = allDirs.index(line[2])
                except ValueError:
                    allDirs.append(line[2])
                    sizes.append(0)
                dirsNow.append(line[2])
    elif (line[0] == "dir") or (line[1] == "ls"):
        gg += 1 # :D
    else:
        b = int(line[0])
        for d in dirsNow:
            i = allDirs.index(d)
            sizes[i] += b
#print(allDirs)
print(sizes)

total = 0
for s in sizes:
    if s <= 100000:
        total += s
print(total)

need = 30000000-(70000000-sizes[0])
sizes.sort()
for s in sizes:
    if s>=need:
        print(s)
        break