# coding=utf-8


def dfs(G, s, d, f, S=None, t=0):
    """
    带时间戳的深度优先搜索
    :param G:
    :param s:
    :param d:
    :param f:
    :param S:
    :param t:
    :return:
    """
    if S is None:
        S = set()
    d[s] = t
    t += 1
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        t = dfs(G, u, d, f, S, t)
    f[s] = t
    t += 1
    return t