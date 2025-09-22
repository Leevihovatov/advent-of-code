def main():
    with open("input13.txt", "r") as f:
        data = f.read().split('\n\n')
    
    silver = 0
    gold = 0

    data = [x.splitlines() for x in data]
    ver = []
    # Create a transpose of the data so you can go through columns the say way as rows
    for i,pattern in enumerate(data):
        for j,line in enumerate(pattern):
            data[i][j] = list(line)
        ver.append(list(map(list, zip(*pattern))))

    # Part 1, doesn't take into consideration the fact that other side of the reflection
    # has be on the edge. Realized this in the part 2, but part 1 didn't need this :D
    # Comments on part 2 function
    def find_reflection(pattern):
        max_reflection = 0
        reflection_index = 0
        for l in range(len(pattern)-1):
            current_reflection = 0
            if pattern[l] == pattern[l+1]:
                current_reflection += 1
                for r in range(1,len(pattern)-2):
                    if (l-r) < 0 or (l+r+1) > len(pattern)+1:
                        if current_reflection > max_reflection:
                            max_reflection = current_reflection
                            reflection_index = l
                        break
                    try:
                        if pattern[l-r] == pattern[l+r+1]:
                            current_reflection += 1
                        else:
                            break
                    except:
                        if current_reflection > max_reflection:
                            max_reflection = current_reflection
                            reflection_index = l
                        break
        return max_reflection, reflection_index
    
    # There may be some parts where it's impossible for the code to go xD
    def find_smudge_reflection(pattern):
        max_reflection = 0
        reflection_index = 0
        for l in range(len(pattern)-1):
            on_edge = False
            smudge = False # if smudge has been found
            current_reflection = 0
            if pattern[l] == pattern[l+1]: # Check consecutive rows to find possible place for line
                current_reflection += 1
                for r in range(1,len(pattern)):
                    # Go outwards from the line
                    if (l-r) < 0 or (l+r+1) >= len(pattern): # If over the edge from one side
                        if smudge and on_edge:
                            if current_reflection > max_reflection:
                                max_reflection = current_reflection
                                reflection_index = l
                        break
                    else:
                        if pattern[l-r] == pattern[l+r+1]: # Matching row
                            if (l-r) == 0 or (l+r+1) == len(pattern)-1:
                                on_edge = True
                            current_reflection += 1
                        else: # Not matching row
                            diff = 0
                            # Find if there is one character difference (smudge)
                            # And then actions depending if it had already been found 
                            # or/and we are on the edge of the pattern
                            for c in range(len(pattern[0])):
                                if pattern[l-r][c] != pattern[l+r+1][c]:
                                    diff += 1
                            if diff == 1 and not smudge:
                                smudge = True
                                current_reflection += 1
                                if (l-r) == 0 or (l+r+1) == len(pattern)-1:
                                    on_edge = True
                            elif smudge and on_edge:
                                if current_reflection > max_reflection:
                                    max_reflection = current_reflection
                                    reflection_index = l
                                break
                            else:
                                break
            else:
                diff = 0
                for c in range(len(pattern[0])):
                    if pattern[l][c] != pattern[l+1][c]:
                        diff += 1
                # If the reflection center rows have the smudge
                if diff == 1:
                    smudge = True
                    current_reflection += 1
                    if l == 0 or (l+1) == (len(pattern)-1): # On the edge
                        if current_reflection > max_reflection:
                            max_reflection = current_reflection
                            reflection_index = l
                    else: # Go outwards from the line
                        for r in range(1,len(pattern)):
                            if (l-r) < 0 or (l+r+1) >= len(pattern):
                                if smudge and on_edge:
                                    if current_reflection > max_reflection:
                                        max_reflection = current_reflection
                                        reflection_index = l
                                break
                            else:
                                if pattern[l-r] == pattern[l+r+1]:
                                    if (l-r) == 0 or (l+r+1) == len(pattern)-1:
                                        on_edge = True
                                    current_reflection += 1
                                else:
                                    diff = 0
                                    for c in range(len(pattern[0])):
                                        if pattern[l-r][c] != pattern[l+r+1][c]:
                                            diff += 1
                                    if diff == 1 and not smudge:
                                        smudge = True
                                        current_reflection += 1
                                        if (l-r) == 0 or (l+r+1) == len(pattern)-1:
                                            on_edge = True
                                    elif smudge and on_edge:
                                        if current_reflection > max_reflection:
                                            max_reflection = current_reflection
                                            reflection_index = l
                                        break
                                    else:
                                        break    
        return max_reflection, reflection_index
    
    # Go through the patterns and transposed patterns to find the reflections
    # In part 1 thought you need to find the biggest reflection (and it didn't need to touch the edge)
    # so that thing stuck until the end
    # In part 2 there is actually only one possible reflection so the other hm or vm is always zero
    for i in range(len(data)):
        hm, hind = find_reflection(data[i])
        vm, vind = find_reflection(ver[i])
        if vm >= hm:
            silver += vind+1
        else:
            silver += 100*(hind+1)
        
        hm, hind = find_smudge_reflection(data[i])
        vm, vind = find_smudge_reflection(ver[i])
        if vm >= hm:
            gold += vind+1
        else:
            gold += 100*(hind+1) 
    
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()