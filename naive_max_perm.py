# coding=utf-8


def naive_max_perm(M, A=None):
    """
    寻找最大排列的递归算法的朴素实现
    :param M:
    :param A:
    :return:
    """
    if not A:
        A = set(range(len(M)))
    if len(A) == 1:
        return A
    B = set(M[i] for i in A)
    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A


if __name__ == '__main__':
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    print(naive_max_perm(M))