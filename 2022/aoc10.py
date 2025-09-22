def main():
    data = open("input10.txt","r",encoding="utf-8").read()
    cycles = data.split()

    signalStrength = 1
    cycleNumber = 0
    silver = 0

    CRTpos = 1
    CRT = ""

    for cycle in cycles:
        cycleNumber += 1

        if (cycleNumber == 20) or ((cycleNumber-20) % 40) == 0:
            silver += signalStrength*cycleNumber

        if cycle == "noop" or cycle == "addx":
            pass
        else:
            signalStrength += int(cycle)

        if (CRTpos >= signalStrength) and (CRTpos <= signalStrength+2):
            CRT += "#"
        else:
            CRT += "."

        if (cycleNumber % 40) == 0:
            CRT += "\n"
            CRTpos = 1      
       
        CRTpos += 1
    
    print(silver)
    print(CRT)

main()
