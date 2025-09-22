def main():
    with open("input23.txt", "r") as f:
        data = f.read()
    
    silver = 0
    gold = 0

    computers = list(set(data.replace('\n',',').replace('-',',').split(',')))
    connections = {}

    for c in computers:
        connections[c] = []

    pairs = data.splitlines()

    for p in pairs:
        connections[p.split('-')[0]].append(p.split('-')[1])
        connections[p.split('-')[1]].append(p.split('-')[0])

    max_conn = 0
    max_conn_coms = ""

    for c in connections:
        connected = [c, connections[c][0]]
        possible = connections[c][1:]

        for p in possible:
            conn_to_others = True
            for i in range(1,len(connected)):
                if connected[i] not in connections[p]:
                    conn_to_others = False
                    break

            if conn_to_others:
                connected.append(p)

        if len(connected) > max_conn:
            max_conn = len(connected)
            connected.sort()
            max_conn_coms = ",".join(connected)

    gold = max_conn_coms

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()