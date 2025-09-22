import math

def main():
    with open("input05.txt", "r") as f:
        data = f.read()
    
    silver = 0
    gold = 0

    rules = data.split("\n\n")[0].splitlines()
    rule_dict = {} # Dict: page: [pages that should be after it]
    for i,r in enumerate(rules):
        before = r.split('|')[0]
        if before in rule_dict:
            continue
        else:
            after = []
            for j in range(i,len(rules)):
                if rules[j].split('|')[0] == before:
                    after.append(rules[j].split('|')[1])
            rule_dict[before] = after

    updates = data.split("\n\n")[1].splitlines()

    # returns list of [page, page that should be after but is before]
    def check_page_order(pages):
        incorrect = []
        for i in range(1,len(pages)):
            page = pages[i]
            if page in rule_dict:
                before_pages = pages[:i]
                for b in before_pages:
                    if b in rule_dict[page]:
                        incorrect.append([page,b])
        return incorrect

    for u in updates:
        pages = u.split(',')
        
        incorrect = check_page_order(pages)

        if len(incorrect) == 0:
            silver += int(pages[math.floor(len(pages)/2)])
        else:
            fixed = False
            while not fixed:
                for ic in incorrect:
                    pages.remove(ic[1])
                    p_index = pages.index(ic[0])
                    pages.insert(p_index+1,ic[1])

                incorrect = check_page_order(pages)
                
                if len(incorrect) == 0:
                    fixed = True

            gold += int(pages[math.floor(len(pages)/2)])

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()