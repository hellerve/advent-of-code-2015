import re

def solve(x):
    def is_nice(string):
        return (
            re.search("[aeiou].*[aeiou].*[aeiou]", string) and
            re.search("(.)\\1", string) and
            not re.search("ab|cd|pq|xy", string)
        )
    nice = list(filter(is_nice, x))
    return len(nice)

x = []
print(solve(x))
