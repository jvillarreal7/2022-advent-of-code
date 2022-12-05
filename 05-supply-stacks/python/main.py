import re


def get_input_content() -> str:
    content = ""
    with open("../input.txt", "r") as f:
        for line in f:
            content += line
        return content


def get_stack_quantity(input_content: str) -> int:
    for line in input_content.splitlines():
        if line.startswith(" 1"):
            return len(line.lstrip(" ").split())


def get_instruction_collection(input_content: str) -> list[dict[str, int]]:
    instruction_collection = []
    for line in input_content.splitlines():
        instructions = {}
        if line.startswith("move"):
            split_line = line.split(" ")
            (
                instructions["quantity"],
                instructions["source"],
                instructions["destination"],
            ) = (
                int(split_line[1]),
                int(split_line[3]) - 1,
                int(split_line[5]) - 1,
            )
            instruction_collection.append(instructions)
    return instruction_collection


def get_pattern_matches(input_content: str) -> list[tuple[str]]:
    pattern_matches = re.findall(r"(\s{4})|\[(\S)]", input_content, re.MULTILINE)
    return pattern_matches


def get_horizontal_stacks_group(
    input_content: str, stack_quantity: int
) -> list[list[str]]:
    pattern_matches = get_pattern_matches(input_content)
    stack_group, temp_group, group_counter = [], [], 0
    for match in pattern_matches:
        if group_counter % stack_quantity == stack_quantity - 1:
            temp_group.append(match[1])
            stack_group.append(temp_group)
            temp_group = []
            group_counter = 0
        else:
            temp_group.append(match[1])
            group_counter += 1
    return stack_group[::-1]


def build_initial_stacks(
    horizontal_stacks_group: list[list[str]], stack_quantity: int
) -> list[list[str]]:
    stacks = [[] for i in range(stack_quantity)]
    for i, stack in enumerate(stacks):
        for group in horizontal_stacks_group:
            for j, element in enumerate(group):
                if i == j and element:
                    stack.append(element)
    return stacks


def apply_instructions(
    instruction_collection: list[dict[str, int]], stacks: list[list[str]]
) -> list[list[str]]:
    for instruction in instruction_collection:
        quantity, source, destination = (
            instruction["quantity"],
            instruction["source"],
            instruction["destination"],
        )
        for _ in range(quantity):
            stacks[destination].append(stacks[source].pop())
    return stacks


def get_top_crate_message(stacks: list[list[str]]) -> str:
    message = "".join([stack[len(stack) - 1] for stack in stacks])
    return message


def main():
    content = get_input_content()
    quantity = get_stack_quantity(content)
    horizontal_group = get_horizontal_stacks_group(content, quantity)
    initial_stacks = build_initial_stacks(horizontal_group, quantity)
    instruction_collection = get_instruction_collection(content)
    stacks_after_instructions = apply_instructions(
        instruction_collection, initial_stacks
    )
    top_crate_message = get_top_crate_message(stacks_after_instructions)
    print(top_crate_message)


main()
