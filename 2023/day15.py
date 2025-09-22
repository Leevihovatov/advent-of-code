def main():
    with open("input15.txt", "r") as f:
        data = f.read().replace('\n','').split(',')
    
    silver = 0
    gold = 0

    def calculate_hash(a):
        value = 0
        for c in a:
            value += ord(c)
            value *= 17
            value = value % 256
        return value

    boxes = [[] for i in range(256)]
    
    for a in data:
        value = calculate_hash(a)
        silver += value
        
        if '-' in a: # Remove if in the box
            label = calculate_hash(a[:-1])
            for j,b in enumerate(boxes[label]):
                if b[0] == a[:-1]:
                    boxes[label].pop(j)
        else:
            label = calculate_hash(a[:-2])
            exists = False
            for j,b in enumerate(boxes[label]): # Change focal length if already in the box
                if b[0] == a[:-2]:
                    boxes[label][j][1] = a[-1]
                    exists = True
                    break
            if not exists: # Add if not in the box
                boxes[label].append([a[:-2],a[-1]])

    # Calculate focusing powers
    for i,box in enumerate(boxes):
        for j,b in enumerate(box):
            gold += (i+1)*(j+1)*int(b[1])

    
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()