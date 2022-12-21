def section_string_to_range(section_string):
    section_split = section_string.split("-")
    section_range = range(int(section_split[0]), int(section_split[1])+1)
    return section_range

def range_contains_other_range(range1, range2):
    return all(e in range2 for e in range1) or all(e in range1 for e in range2)

def ranges_overlap(range1, range2):
    return any(e in range2 for e in range1)

def solve(pairs):
    count1 = 0
    count2 = 0

    for pair in pairs:
        range1 = section_string_to_range(pair[0])
        range2 = section_string_to_range(pair[1])
        if range_contains_other_range(range1, range2):
            count1 += 1
        if ranges_overlap(range1, range2):
            count2 += 1
    return count1, count2


if __name__ == "__main__":
    with open("input", "r") as f:
       input = f.read().strip()

    pairs = [ i.split(",") for i in input.split("\n") ]

    count1, count2 = solve(pairs)

    print(f"Part A: {count1}")
    print(f"Part B: {count2}")
