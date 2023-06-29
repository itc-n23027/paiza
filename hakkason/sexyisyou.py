M, N = map(int, input().split())


def sexyisyou(M, N):
    return M - N if M - N > 0 else 0


print(sexyisyou(M, N))
