def get_input_sequence() -> str:
    with open("../input.txt", "r") as f:
        return f.readline()


def get_characters_processed_before_marker(sequence: str) -> int:
    for i in range(14, len(sequence)):
        sequence_slice = sequence[i - 14 : i]
        if len(set(sequence_slice)) == 14:
            return i


sequence = get_input_sequence()
print(get_characters_processed_before_marker(sequence))
