def main():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()
    
    for i,d in enumerate(data):
        for j,c in enumerate(d):
            if c == 'S':
                pos = [i,j]

    silver = 0
    gold = 0

    paths = [[pos]]
    scores = [0]
    min_scores = {}
    min_paths = {}
    full_paths = []
    full_score = 999999
    while paths != []:

        """ print('****************')
        for pa in paths:
            print(pa) """

        new_paths = []
        new_scores = []
        candidates = []
        for i, p in enumerate(paths):
            #print(p)
            last = p[-1]
            candidates = [[last[0]-1,last[1]], [last[0],last[1]+1], [last[0]+1,last[1]], [last[0],last[1]-1]]
            for c in candidates:
                if data[c[0]][c[1]] == 'E':
                    if p[-2][0] != c[0] and p[-2][1] != c[1]:
                        path_score = scores[i]+1001
                    else:
                        path_score = scores[i]+1

                    if path_score < full_score:
                        full_score = path_score
                        full_paths.append(p+[c])
                elif data[c[0]][c[1]] == '.' and c not in p:
                    if len(p) > 1:
                        if p[-2][0] != c[0] and p[-2][1] != c[1]:
                            path_score = scores[i]+1001
                        else:
                            path_score = scores[i]+1
                    else:
                        if last[0] != c[0]:
                            path_score = scores[i]+1001
                        else:
                            path_score = scores[i]+1
                    
                    better = True
                    if str(c) in min_scores:
                        if path_score == min_scores[str(c)]:
                            print(c)
                            min_scores[str(c)] = path_score
                            min_paths[str(c)].append(p+[c])
                        elif path_score < min_scores[str(c)]:
                            min_scores[str(c)] = path_score
                        else:
                            better = False
                    else:
                        min_scores[str(c)] = path_score
                        min_paths[str(c)] = [p+[c]]

                    if path_score < full_score and better:
                        new_scores.append(path_score)
                        new_paths.append(p+[c])

        paths = new_paths
        scores = new_scores
        #print(f'{num} {pos}')

    print(min_paths['[8, 3]'])

    silver = full_score

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()