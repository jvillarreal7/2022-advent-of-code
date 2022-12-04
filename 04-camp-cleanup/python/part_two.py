def get_split_assignment_pairs() -> list[tuple[str]]:
    with open("../input.txt", "r") as f:
        return [tuple(line.strip("\n").split(",")) for line in f]


def get_expanded_assignment_pairs() -> list[tuple[list[int]]]:
    split_assignment_pairs = get_split_assignment_pairs()
    expanded_assignment_pairs = [
        (
            [
                unit
                for unit in range(
                    int(section[0].split("-")[0]), int(section[0].split("-")[1]) + 1
                )
            ],
            [
                unit
                for unit in range(
                    int(section[1].split("-")[0]), int(section[1].split("-")[1]) + 1
                )
            ],
        )
        for section in split_assignment_pairs
    ]
    return expanded_assignment_pairs


def is_assignment_pair_overlapping(assignment_pair: tuple[list[int]]) -> bool:
    first_assignment, second_assignment = assignment_pair[0], assignment_pair[1]

    if len(first_assignment) >= len(second_assignment):
        return any(unit in first_assignment for unit in second_assignment)
    return any(unit in second_assignment for unit in first_assignment)


def main():
    overlap_count = 0
    assignment_pairs = get_expanded_assignment_pairs()
    for assignment_pair in assignment_pairs:
        if is_assignment_pair_overlapping(assignment_pair):
            overlap_count += 1
    print(overlap_count)


main()
