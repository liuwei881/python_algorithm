# coding=utf-8

from collections import defaultdict


def counting_sort(A, key=lambda x: x):
    """
    计数排序
    :param A:
    :param key:
    :return:
    """
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for k in range(min(C), max(C)+1):
        B.extend(C[k])
    return B


if __name__ == '__main__':
    seq = [2, 3, 1, 5, 7]
    print(counting_sort(seq))