import numpy as np
def main():
    with open("input08.txt", "r") as f:
        data = f.read().splitlines()
    
    s_antinodes = []
    antinodes = []
    antennas = {}
    for i,d in enumerate(data):
        data[i] = list(d)
        antinodes.append([0]*len(d))
        s_antinodes.append([0]*len(d))
        for j,c in enumerate(list(d)):
            if c != '.':
                if c in antennas:
                    antennas[c].append([i,j])
                else:
                    antennas[c] = [[i,j]]
    max_row = len(data)-1
    max_col = len(data[0])-1

    silver = 0
    gold = 0

    for a in antennas:
        for i,loc in enumerate(antennas[a]):
            for j in range(i+1,len(antennas[a])):
                dist = abs(np.subtract(loc,antennas[a][j]))
                all_ans = []
                all_ans.append(loc)
                all_ans.append(antennas[a][j])
                low_in_area = True
                high_in_area = True
                # Keep adding antinodes to diagonal directions until they are out of bounds
                # if-else: whether negative or positive diagonal
                if loc[1] < antennas[a][j][1]:
                    low_ans = [loc[0]-dist[0],loc[1]-dist[1]]
                    high_ans = [antennas[a][j][0]+dist[0],antennas[a][j][1]+dist[1]]
                    s_ans = [low_ans, high_ans]
                    while low_in_area:
                        if low_ans[0] >= 0 and low_ans[0] <= max_row and low_ans[1] >= 0 and low_ans[1] <= max_col:
                            all_ans.append(low_ans)
                            low_ans = [low_ans[0]-dist[0],low_ans[1]-dist[1]]
                        else:
                            low_in_area = False

                    while high_in_area:
                        if high_ans[0] >= 0 and high_ans[0] <= max_row and high_ans[1] >= 0 and high_ans[1] <= max_col:
                            all_ans.append(high_ans)
                            high_ans = [high_ans[0]+dist[0],high_ans[1]+dist[1]]
                        else:
                            high_in_area = False
                    
                else:
                    low_ans = [loc[0]-dist[0],loc[1]+dist[1]]
                    high_ans = [antennas[a][j][0]+dist[0],antennas[a][j][1]-dist[1]]
                    s_ans = [low_ans, high_ans]
                    while low_in_area:
                        if low_ans[0] >= 0 and low_ans[0] <= max_row and low_ans[1] >= 0 and low_ans[1] <= max_col:
                            all_ans.append(low_ans)
                            low_ans = [low_ans[0]-dist[0],low_ans[1]+dist[1]]
                        else:
                            low_in_area = False

                    while high_in_area:
                        if high_ans[0] >= 0 and high_ans[0] <= max_row and high_ans[1] >= 0 and high_ans[1] <= max_col:
                            all_ans.append(high_ans)
                            high_ans = [high_ans[0]+dist[0],high_ans[1]-dist[1]]
                        else:
                            high_in_area = False
                
                for an in s_ans:
                    if an[0] >= 0 and an[0] <= max_row and an[1] >= 0 and an[1] <= max_col:
                        s_antinodes[an[0]][an[1]] = 1

                for an in all_ans:
                    antinodes[an[0]][an[1]] = 1

    for row in s_antinodes:
        silver += sum(row)

    for row in antinodes:
        gold += sum(row)

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()