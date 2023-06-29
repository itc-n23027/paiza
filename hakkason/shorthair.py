N = int(input())
S = input()


def hair(N, S):
    return "\n".join([S for i in range(N)])


print(hair(N, S))
