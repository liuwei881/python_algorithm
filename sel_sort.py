# coding=utf-8


def sel_sort(seq):
    """
    选择排序
    :param seq:
    :return:
    """
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]
    return seq


if __name__ == '__main__':
    seq = [2, 3, 1, 5, 7]
    print(sel_sort(seq))