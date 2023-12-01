with open('day1input.txt', encoding='UTF-8') as document:
    total = 0
    for line in document:
        numonly = ""
        cal_val = ""
        line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "th3e").replace(
            "four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace(
            "eight", "e8t").replace("nine", "n9e")
        for i in line:
            if i.isnumeric():
                numonly += i
        cal_val += numonly[0]
        cal_val += numonly[-1]
        total += int(cal_val)
        print(total)
