def main():
    with open("input08.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    top_n = 1000

    boxes = {}
    groups = []

    for i,b in enumerate(data):
        groups.append([i])

        coords = [int(x) for x in b.split(',')]
        coords_dict = {
            'x': coords[0],
            'y': coords[1],
            'z': coords[2]
        }
        boxes[i] = coords_dict


    distances = []
    for i in range(len(boxes)-1):
        for j in range(i+1, len(boxes)):
            if i != j:
                pair = (i, j)
                dist = ((boxes[i]['x']-boxes[j]['x'])**2 + (boxes[i]['y']-boxes[j]['y'])**2 + (boxes[i]['z']-boxes[j]['z'])**2) ** (0.5)
                distances.append([dist, pair])

    distances = sorted(distances, key=lambda x: x[0])

    for i,d in enumerate(distances):
        pair = d[1]

        group_1 = None
        group_2 = None

        for g in groups:
            if group_1 and group_2:
                break

            if pair[0] in g:
                group_1 = g
            if pair[1] in g:
                group_2 = g

        if group_1 != group_2:
            new_group = group_1 + group_2
            groups.remove(group_1)
            groups.remove(group_2)
            groups.append(new_group)

        if i == top_n - 1:
            groups = sorted(groups, key=lambda x: len(x), reverse=True)
            silver = len(groups[0]) * len(groups[1]) * len(groups[2])

        if len(groups) == 1:
            break

    gold = boxes[pair[0]]['x'] * boxes[pair[1]]['x']

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()