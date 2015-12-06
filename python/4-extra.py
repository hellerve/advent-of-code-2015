from hashlib import md5

def solve(x):
    k = 0
    while not md5((x + str(k)).encode("utf-8")).hexdigest().startswith("000000"):
        k += 1
    return k

x = "ckczppom"
print(solve(x))
