# coding=utf-8


def sel_sort_rec(seq, i):
    """
    选择排序递归版
    :param seq:
    :param i: len(seq) -1
    :return:
    """
    if i == 0:
        return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]:
            max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i-1)
    return seq


if __name__ == '__main__':
    seq = [2, 3, 1, 5, 7]
    print(sel_sort_rec(seq, len(seq)-1))