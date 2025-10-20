def main():
    with open("input06.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 0
    gold = 0

    answers = ''
    people = 0
    for d in data:
        answers += d
        people += 1

        if d == '':
            people -= 1
            questions = set(list(answers))

            silver += len(questions)

            for q in questions:
                if answers.count(q) == people:
                    gold += 1

            answers = ''
            people = 0

    questions = set(list(answers))

    silver += len(questions)

    for q in questions:
        if answers.count(q) == people:
            gold += 1

    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()