def ascii_value_to_priority(char):
    if char.isupper():
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1

def get_item_in_common(string_a, string_b):
    item_in_common = ''.join(
        set(string_a).intersection(string_b)
    )
    return item_in_common

def solve_part_1(backpacks):
    sum_of_priorities = 0

    for backpack in backpacks:
        half_index = len(backpack)//2
        compartment_a = backpack[:half_index]
        compartment_b = backpack[half_index:]

        item_in_common = get_item_in_common(compartment_a, compartment_b)
        sum_of_priorities += ascii_value_to_priority(item_in_common)

    return sum_of_priorities

def solve_part_2(backpacks):
    groups = []
    group = []
    for group_index, backpack in enumerate(backpacks):
        group.append(backpack)
        if ((group_index + 1) % 3) == 0 and group_index > 0:
            groups.append(group)
            group = []

    sum_of_priorities = 0
    for group in groups:
        item_in_common = get_item_in_common(group[0], group[1])
        item_in_common = get_item_in_common(item_in_common, group[2])
        sum_of_priorities += ascii_value_to_priority(item_in_common)

    return sum_of_priorities


if __name__ == "__main__":
    
    with open("input", "r") as f:
       input = f.read().strip()

    backpacks = input.split("\n")

    print(f"Part A: {solve_part_1(backpacks)}")
    print(f"Part B: {solve_part_2(backpacks)}")
