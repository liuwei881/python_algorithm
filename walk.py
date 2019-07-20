# coding=utf-8


def walk(G, s, S=set()):
    """
    地图漫步
    :param G:
    :param s:
    :param S:
    :return:
    """
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
    return P


def components(G):
    """
    找出连通分量
    :param G:
    :return:
    """
    comp = []
    seen = set()
    for u in G:
        if u in seen:
            continue
        C = walk(G, u)
        seen.update(C)
        comp.append(C)
    return comp