def main():
    with open("input", "r") as f:
       input = f.read()
        
    print(f"Part A: {solve(input, 4)}")
    print(f"Part B: {solve(input, 14)}")

def solve(input, scope):
    for i in range(len(input)):
        if len(set(input[i:i+scope])) == scope:
            return i+scope

if __name__ == "__main__":
    main()
