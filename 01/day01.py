with open("input", "r") as f:
   input = f.read().strip()

def parse_input(input):
    return [
        sum(int(calories) for calories in elf.split("\n")) 
        for elf in input.split("\n\n") 
    ]

calories_sorted = sorted(parse_input(input))

print(f"Part A: {calories_sorted[-1]}")
print(f"Part B: {sum(calories_sorted[-3:])}")
