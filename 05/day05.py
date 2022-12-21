def main():
    with open("input", "r") as f:
       input = f.read()

    stack_lines, move_lines = [ x.splitlines() for x in input.split('\n\n') ]

    print(f"Part A: {solve(stack_lines, move_lines)}")
    print(f"Part B: {solve(stack_lines, move_lines, part2=True)}")


def solve(stack_lines, move_lines, part2=False):

    # Parse the last row of stacks, get the digits, get max value
    num_of_stacks = max(int(s) for s in stack_lines[-1].split())

    # Set up empty stacks
    stacks = [[] for _ in range(num_of_stacks)]

    # Parse the stack lines and append crates to stacks
    for line in stack_lines[::-1]:
        for i, crate in enumerate(line[1::4]):
            if crate.isupper():
                stacks[i].append(crate)

    moves = []

    # Parse the move lines and add digits
    for move in move_lines:
        moves.append( [int(m) for m in move.split() if m.isdigit()] )

    # Let's move the crates
    for move_amount, move_from, move_to in moves:

        crate_mover = []
        for _ in range(move_amount):
            crate = stacks[move_from-1].pop()
            crate_mover.append(crate)
 
        # Reverse the crates we're moving if part 2
        if part2:
            crate_mover.reverse()
            
        stacks[move_to-1].extend(crate_mover)

    # Return top of stacks
    return(''.join(s[-1] for s in stacks))


if __name__ == "__main__":
    main()
