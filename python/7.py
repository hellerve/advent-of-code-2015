"Let's try and write something obfuscated, convoluted and strange, shall we?"
import operator

def solve(l):
    gates = {}
    def _solve(val, expr, gates):
        if type(expr) is list:
            args = []
            for e in expr[1]:
                if type(e) is str:
                    try:
                        gates = _solve(e, gates[e], gates)
                        if type(gates[e]) is list:
                            return gates
                        args.append(gates[e])
                    except KeyError as e:
                        return gates
                else:
                    args.append(e)
            gates[val] = expr[0](*args) & 65535
        return gates
    def _destructure(e, gates):
      "What's readability?"
      logic = {
          "AND": operator.and_,
          "OR": operator.or_,
          "NOT": operator.invert,
          "LSHIFT": operator.lshift,
          "RSHIFT": operator.rshift,
          "NOOP": lambda x: x
      }
      if e[0].isnumeric() and len(e) == 3:
        gates[e[2]] = int(e[0])
      elif e[0] == "NOT":
        if e[1].isnumeric():
            gates[e[3]] = logic[e[0]](int(e[1]))
        else:
            gates[e[3]] = [logic[e[0]], [e[1]]]
      elif len(e) == 5:
        if e[0].isnumeric() and e[2].isnumeric():
            gates[e[4]] = logic[e[1]](int(e[0]), int(e[2]))
        elif e[0].isnumeric():
            gates[e[4]] = [logic[e[1]], [int(e[0]), e[2]]]
        elif e[2].isnumeric():
            gates[e[4]] = [logic[e[1]], [e[0], int(e[2])]]
        else:
            gates[e[4]] = [logic[e[1]], [e[0], e[2]]]
      elif e[0].isalpha():
        gates[e[2]] = [logic["NOOP"], [e[0]]]
      return gates

    for e in l: 
        gates = _destructure(e.split(), gates)
    while type(gates["a"]) != int:
        for val, expr in gates.items():
            gates = _solve(val, expr, gates)

    return gates["a"]

x = []

print(solve(x))
