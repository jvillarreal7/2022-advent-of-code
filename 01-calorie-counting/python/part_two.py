with open("../input.txt", "r") as f:
    current_calories = 0
    elves_calories = []
    for line in f:
        if line != "\n":
            current_calories += int(line)
        else:
            elves_calories.append(current_calories)
            current_calories = 0
    else:
        elves_calories.append(current_calories)
    print(sum(sorted(elves_calories)[::-1][:3]))
