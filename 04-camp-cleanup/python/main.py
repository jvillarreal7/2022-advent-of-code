def get_expanded_assignments() -> list[tuple[list[str]]]:
    with open("../input.txt", "r") as f:
        split_assignments = [tuple(line.strip("\n").split(",")) for line in f]
        expanded_assignments = [
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
            for section in split_assignments
        ]
        return expanded_assignments


def is_assignment_fully_overlapping(assignment: tuple[list[str]]) -> bool:
    first_assignment, second_assignment = assignment[0], assignment[1]

    if len(first_assignment) == len(second_assignment):
        return first_assignment == second_assignment
    elif len(first_assignment) > len(second_assignment):
        return all(unit in first_assignment for unit in second_assignment)
    return all(unit in second_assignment for unit in first_assignment)


def main():
    full_overlap_count = 0
    assignments = get_expanded_assignments()
    for assignment in assignments:
        if is_assignment_fully_overlapping(assignment):
            full_overlap_count += 1
    print(full_overlap_count)


main()
