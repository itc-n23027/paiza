n, m = map(int, input().split())


def kyutoisyou(n, m):
    return "ok" if m % n == 0 else "ng"


print(kyutoisyou(n, m))
