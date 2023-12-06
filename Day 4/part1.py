with open('data.txt', encoding='UTF-8') as document:
    total = 0
    for i, info in enumerate(document):
        game = info.split(":")[1].strip("\n")
        numbers = [x.split(" ") for x in game.split("|")]
        win = list(filter(None, numbers[0]))
        card = list(filter(None, numbers[1]))

        tot = 0
        for winner in win:
            if winner in card:
                if tot == 0:
                    tot = 1
                else:
                    tot = tot * 2
        print(tot)
        total += tot

    print(total)
