def get_input_sequence() -> str:
    with open("../input.txt", "r") as f:
        return f.readline()


def get_marker(sequence: str) -> int:
    for i in range(4, len(sequence)):
        sequence_slice = sequence[i - 4 : i]
        if len(set(sequence_slice)) == 4:
            return i


sequence = get_input_sequence()
print(get_marker(sequence))
