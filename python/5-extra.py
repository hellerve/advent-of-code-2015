import re

def solve(x):
    def is_nice(string):
        def check_for_gapped_repeat(string):
            for i, e in enumerate(string):
                if len(string) <= i+2: continue
                if e == string[i+2]: return True
            return False
        def check_for_pair(string):
            for i, e in enumerate(string):
                pattern = string[i:i+2]
                if pattern in string[i+2:]: return True
            return False
        return (
            check_for_gapped_repeat(string) and
            check_for_pair(string)
        )
    nice = list(filter(is_nice, x))
    return len(nice)

x = []
print(solve(x))
