def main():
    with open("input07.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    bags = {}
    bags_with_counts = {}
    my_bag = 'shiny gold'

    for d in data:
        big_bag = ' '.join(d.split('contain')[0].split()[:2])

        if ',' in d.split('contain')[1]:
            inside_bags = [' '.join(b.split()[1:3]) for b in d.split('contain')[1].split(',')]
            inside_bags_nro = [[' '.join(b.split()[1:3]), int(b.split()[0])] for b in d.split('contain')[1].split(',')]
        elif 'no other bags' in d.split('contain')[1]:
            inside_bags = []
            inside_bags_nro = []
        else:
            inside_bags = [' '.join(d.split('contain')[1].split()[1:3])]
            inside_bags_nro = [[' '.join(d.split('contain')[1].split()[1:3]), int(d.split('contain')[1].split()[0])]]

        bags[big_bag] = inside_bags
        bags_with_counts[big_bag] = inside_bags_nro

    def get_outer_bags(bag):
        outer_bags = []
        for b in bags:
            if bag in bags.get(b):
                outer_bags.append(b)
        return outer_bags

    good_bags = []

    investigate_bags = [my_bag]
    looked_bags = []

    while len(investigate_bags) > 0:
        next_investigate = []

        for ib in investigate_bags:
            new_bags = get_outer_bags(ib)
            
            good_bags += new_bags
            good_bags = list(set(good_bags))
            next_investigate += new_bags
            
            looked_bags.append(ib)

        next_investigate = list(set(next_investigate))
        investigate_bags = next_investigate
        investigate_bags = [ib for ib in investigate_bags if ib not in looked_bags]

    silver = len(good_bags)

    bags_to_count = ['shiny gold']

    while len(bags_to_count) > 0:
        next_bags_to_count = []

        for b in bags_to_count:
            if bags_with_counts[b] != []:
                for b2 in bags_with_counts[b]:
                    next_bags_to_count += [b2[0]]*b2[1]

            gold += 1

        bags_to_count = next_bags_to_count

    gold -= 1 # Remove the shiny gold bag itself from the count

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()