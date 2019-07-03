# coding=utf-8


def ins_sort_rec(seq, i):
    """
    插入排序递归版
    :param seq:
    :param i:
    :return:
    """
    if i == 0:
        return
    ins_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1


if __name__ == '__main__':
    seq = [2, 3, 1, 5, 7]
    ins_sort_rec(seq, len(seq)-1)
    print(seq)