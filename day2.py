red = 12
green = 13
blue = 14
all_games = []
total = 0

with open("sample.txt", encoding="utf-8") as data_in:
    for line in data_in:
        game_data = line.split(":")
        games = game_data[1].split(";")
        game_data[1:] = [games]
        all_games.append(game_data)

        max_red = 0
        max_blue = 0
        max_green = 0

        for pull in game_data[1]:
            red_count = "0"
            blue_count = "0"
            green_count = "0"
            hand = pull.split(",")

            for item in hand:
                if "red" in item:
                    for i in item:
                        if i.isnumeric():
                            red_count += i
                elif "blue" in item:
                    for i in item:
                        if i.isnumeric():
                            blue_count += i
                elif "green" in item:
                    for i in item:
                        if i.isnumeric():
                            green_count += i
            red_count = int(red_count)
            blue_count = int(blue_count)
            green_count = int(green_count)
            if red_count > max_red:
                max_red = red_count
            if blue_count > max_blue:
                max_blue = blue_count
            if green_count > max_green:
                max_green = green_count
        game_power = max_red * max_green * max_blue
        print("Game power is: ", game_power)
        total += game_power
print(total)


# for play in all_games:
#     game_no = ""
#     for j in play[0]:
#         if j.isnumeric():
#             game_no += j
#     print(game_no)
#     game_no = int(game_no)
#     total += game_no
# print()
#
# print(total)
