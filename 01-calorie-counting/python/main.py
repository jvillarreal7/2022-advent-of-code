with open("../input.txt", "r") as f:
    max_calories, current_calories = 0, 0
    for line in f:
        if line != "\n":
            current_calories += int(line)
        else:
            max_calories = max(max_calories, current_calories)
            current_calories = 0
    print(max_calories)
