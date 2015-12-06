def solve(inpt):
    state = [0, 0]
    visited = [state]
    def step(x, state, visited):
        if x == ">": state = [state[0]+1,state[1]]
        if x == "<": state = [state[0]-1,state[1]]
        if x == "^": state = [state[0],state[1]+1]
        if x == "v": state = [state[0],state[1]-1]
        if state not in visited: visited.append(state)
        return state, visited
    for e in inpt:
        state, visited = step(e, state, visited)
    return len(visited)

x = ""
print(solve(x))
