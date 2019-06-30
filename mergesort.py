# coding=utf-8


def mergesort(seq):
    """
    归并排序
    :param seq:
    :return:
    """
    mid = len(seq) / 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


if __name__ == '__main__':
    import random
    seq = [random.randrange(100) for i in range(15)]
    print(mergesort(seq))