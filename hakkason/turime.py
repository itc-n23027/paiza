p = int(input())


def turime(p):
    return p // 100 if p <= 1000 else p // 100 + 10


print(turime(p))
