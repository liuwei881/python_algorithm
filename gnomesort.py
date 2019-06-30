# coding=utf-8


def gnomesort(seq):
    """
    侏儒排序
    :param seq:
    :return:
    """
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1
    return seq


if __name__ == '__main__':
    import random
    seq = [random.randrange(100) for i in range(50)]
    print(gnomesort(seq))