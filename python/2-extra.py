def solve_all(complete):
    def solve(l, w, h):
        s = sorted([l, w, h])
        return l * w * h + s[0] * 2 + s[1] * 2
    return sum(map(lambda e: solve(*e), complete))

x = []
print(solve_all(map(lambda e: [int(i) for i in e.split("x")], x)))
