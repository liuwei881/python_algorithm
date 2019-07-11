# coding=utf-8


def max_perm(M):
    """
    寻找最大排列问题
    :param M:
    :return:
    """
    n = len(M)
    A = set(range(n))
    count = [0] * n
    for i in M:
        count[i] += 1
    Q = [i for i in A if count[i] == 0]
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A


if __name__ == '__main__':
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    print(max_perm(M))