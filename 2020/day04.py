def main():
    with open("input04.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    passports = []

    p = ''
    for d in data:
        p += d
        p += ' '

        if d == '':
            fields = {f.split(':')[0]: f.split(':')[1] for f in p.split()}

            passports.append(fields)

            p = ''

    fields = {f.split(':')[0]: f.split(':')[1] for f in p.split()}
    passports.append(fields)
    
    needed_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def check_fields(p):
        checks = []

        if p['byr'].isnumeric():
            checks.append(int(p['byr']) >= 1920 and int(p['byr']) <= 2002)
        else:
            checks.append(False)

        if p['iyr'].isnumeric():
            checks.append(int(p['iyr']) >= 2010 and int(p['iyr']) <= 2020)
        else:
            checks.append(False)

        if p['eyr'].isnumeric():
            checks.append(int(p['eyr']) >= 2020 and int(p['eyr']) <= 2030)
        else:
            checks.append(False)

        if p['hgt'].endswith('cm'):
            height = p['hgt'].replace('cm','')
            if height.isnumeric():
                checks.append(int(height) >= 150 and int(height) <= 193)
        elif p['hgt'].endswith('in'):
            height = p['hgt'].replace('in','')
            if height.isnumeric():
                checks.append(int(height) >= 59 and int(height) <= 76)
        else:
            checks.append(False)

        # Could also be done with regex, but lets try to not use any libraries
        if len(p['hcl']) == 7 and p['hcl'].startswith('#'):
            hexcode = p['hcl'][1:]
            hexcode = hexcode.replace('0','').replace('1','').replace('2','').replace('3','').replace('4','')
            hexcode = hexcode.replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
            hexcode = hexcode.replace('a','').replace('b','').replace('c','').replace('d','').replace('e','').replace('f','')

            checks.append(len(hexcode) == 0)
        else:
            checks.append(False)

        checks.append(p['ecl'] in eye_colors)

        checks.append(p['pid'].isnumeric() and len(p['pid']) == 9)

        return checks

    for p in passports:
        if all(k in p for k in needed_keys):
            silver += 1

            checks = check_fields(p)

            if all(checks):
                gold += 1

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()