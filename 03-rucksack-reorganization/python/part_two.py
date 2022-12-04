def get_item_priority(item: str) -> int:
    return ord(item) - 38 if item.isupper() else ord(item) - 96


def get_rucksack_groups() -> list[tuple[str]]:
    with open("../input.txt", "r") as f:
        group_counter = 0
        temp_group, final_group = [], []
        for line in f:
            line = line.strip("\n")
            if group_counter % 3 == 2:
                temp_group.append(line)
                final_group.append(tuple([rucksack for rucksack in temp_group]))
                group_counter = 0
                temp_group = []
            else:
                temp_group.append(line)
                group_counter += 1
        return final_group


def get_common_item(rucksack_group: tuple[str]) -> str:
    first_rucksack_set, second_rucksack_set, third_rucksack_set = (
        set(rucksack_group[0]),
        set(rucksack_group[1]),
        set(rucksack_group[2]),
    )
    return list(first_rucksack_set & second_rucksack_set & third_rucksack_set)[0]


def main():
    total_item_priority = 0
    rucksack_groups = get_rucksack_groups()
    for group in rucksack_groups:
        common_item = get_common_item(group)
        total_item_priority += get_item_priority(common_item)
    print(total_item_priority)


main()
