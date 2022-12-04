def get_split_assignment_pairs() -> list[tuple[str]]:
    with open("../input.txt", "r") as f:
        return [tuple(line.strip("\n").split(",")) for line in f]


def get_expanded_assignment(raw_assignment: str) -> list[int]:
    return [
        unit
        for unit in range(
            int(raw_assignment.split("-")[0]),
            int(raw_assignment.split("-")[1]) + 1,
        )
    ]


def get_expanded_assignment_pairs() -> list[tuple[list[int]]]:
    split_assignment_pairs = get_split_assignment_pairs()
    expanded_assignment_pairs = [
        (
            get_expanded_assignment(raw_assignments[0]),
            get_expanded_assignment(raw_assignments[1]),
        )
        for raw_assignments in split_assignment_pairs
    ]
    return expanded_assignment_pairs


def is_assignment_pair_fully_overlapping(assignment_pair: tuple[list[int]]) -> bool:
    first_assignment, second_assignment = assignment_pair[0], assignment_pair[1]

    if len(first_assignment) == len(second_assignment):
        return first_assignment == second_assignment
    elif len(first_assignment) > len(second_assignment):
        return all(unit in first_assignment for unit in second_assignment)
    return all(unit in second_assignment for unit in first_assignment)


def main():
    full_overlap_count = 0
    assignment_pairs = get_expanded_assignment_pairs()
    for assignment_pair in assignment_pairs:
        if is_assignment_pair_fully_overlapping(assignment_pair):
            full_overlap_count += 1
    print(full_overlap_count)


main()
