with open('data.txt', encoding='UTF-8') as document:
    totals = []
    no_cards = []
    for info in document:
        no_cards.append(1)
        game = info.split(":")[1].strip("\n")
        numbers = [x.split(" ") for x in game.split("|")]
        win = list(filter(None, numbers[0]))
        card = list(filter(None, numbers[1]))

        tot = 0
        for winner in win:
            if winner in card:
                tot += 1
        totals.append(tot)

print(no_cards)
print(totals)

for n in range(len(totals)):
    print(n)
    for i in range(0, totals[n]):
        # i+1
        no_cards[n + i + 1] += no_cards[n]
    print(no_cards)

print(sum(no_cards))
