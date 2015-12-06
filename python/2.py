def solve_all(complete):
    def solve(l, w, h):
        s, f, c = l*w, w*h, h*l
        return 2*s + 2*f + 2*c + min(s, f, c)
    return sum(map(lambda e: solve(*e), complete))

x = []
print(solve_all(map(lambda e: [int(i) for i in e.split("x")], x)))
