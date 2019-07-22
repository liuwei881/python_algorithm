# coding=utf-8


def traverse(G, s, qtype=set):
    """
    通用性的图遍历函数
    :param G:
    :param s:
    :param qtype:
    :return:
    """
    S = set()
    Q = qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u