data = open("input6.txt","r",encoding="utf-8").read()
readChars = 0
l = 14
for i in range(l,len(data),1):
    code = data[i-l:i]
    code = list(dict.fromkeys(code))
    #print(code)
    if len(code)==l:
        readChars = i
        break

print(readChars)