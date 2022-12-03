def get_item_priority(item: str) -> int:
    return ord(item) - 38 if item.isupper() else ord(item) - 96


def get_rucksacks() -> list[tuple[str]]:
    with open("../input.txt", "r") as f:
        return [
            (line[: len(line) // 2], line[len(line) // 2 :].strip("\n")) for line in f
        ]


def get_common_item(rucksack: tuple[str]) -> str:
    first_comp_set, second_comp_set = set(rucksack[0]), set(rucksack[1])
    try:
        return list(first_comp_set.intersection(second_comp_set))[0]
    except IndexError:
        print(rucksack)


def main():
    total_item_priority = 0
    rucksacks = get_rucksacks()
    for rucksack in rucksacks:
        common_item = get_common_item(rucksack)
        total_item_priority += get_item_priority(common_item)
    print(total_item_priority)


main()
