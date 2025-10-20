def main():
    with open("input03.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    height = len(data)
    width = len(data[0])
 
    slopes = [[1,1], [1,3], [1,5], [1,7], [2,1]]

    all_trees = []

    for s in slopes:
        pos = [0,0]
        s_trees = 0
        while pos[0] < height:

            if data[pos[0]][pos[1]] == '#':
                s_trees += 1

            pos = [pos[0] + s[0], pos[1] + s[1]]
            
            if pos[1] > width-1:
                pos[1] = pos[1] % width
        
        all_trees.append(s_trees)

    silver = all_trees[1]
    gold = 1
    for t in all_trees:
        gold *= t

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()