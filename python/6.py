def solve(l):
    lit = [False] * 1000000
    def step(x, lit):
        def parse(x):
            els = x.split(",")
            return int(els[0]), int(els[1])
        split = x.split(" ")
        if split[0] == "toggle":
            lower, higher = parse(split[1]), parse(split[3])
            for i in range(lower[0], higher[0]+1):
                for j in range(lower[1], higher[1]+1):
                    lit[i+1000*j] = not lit[i+1000*j]
        else:
            lower, higher = parse(split[2]), parse(split[4])
            if split[1] == "on":
                for i in range(lower[0], higher[0]+1):
                    for j in range(lower[1], higher[1]+1):
                        lit[i+1000*j] = True
            if split[1] == "off":
                for i in range(lower[0], higher[0]+1):
                    for j in range(lower[1], higher[1]+1):
                        lit[i+1000*j] = False
        return lit
    for e in l:
        lit = step(e, lit)
    return len(list(filter(lambda x: x, lit)))

x = []
print(solve(x))
