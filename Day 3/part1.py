with open("schematic.txt") as data:
    current_no = ""
    list_of_numbers = []
    list_of_symbols = []
    for y, line in enumerate(data):
        line += "."
        for x, character in enumerate(line):
            if character.isdigit():
                if current_no == "":
                    start = (x, y)
                current_no += character
            else:
                if current_no != "":
                    list_of_numbers.append((current_no, start))
                    current_no = ""
                if character not in ".":
                    location = (x, y)
                    list_of_symbols.append(location)

    # print(list_of_numbers)
    # print(list_of_symbols)
total = 0
for number, coordinate in list_of_numbers:
    x1 = coordinate[0] - 1
    x2 = coordinate[0] + len(number)
    y1 = coordinate[1] - 1
    y2 = coordinate[1] + 1
    # print(f"The rectangle for {number} is ({x1, y1}) to ({x2, y2}).")
    for symbol in list_of_symbols:
        if x1 <= symbol[0] <= x2 and y1 <= symbol[1] <= y2:
            total += int(number)
            print(f"{number} with  rectangle ({x1, y1}) to ({x2, y2}) is next to {symbol}")
            break

print()
print(total)
