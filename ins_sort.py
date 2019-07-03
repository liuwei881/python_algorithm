# coding=utf-8


def ins_sort(seq):
    """
    插入排序
    :param seq:
    :return:
    """
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1


if __name__ == '__main__':
    seq = [2, 3, 1, 5, 7]
    ins_sort(seq)
    print(seq)