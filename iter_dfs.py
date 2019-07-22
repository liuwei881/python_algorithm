# coding=utf-8


def iter_dfs(G, s):
    """
    迭代版的深度优先搜索
    :param G:
    :param s:
    :return:
    """
    S = set()
    Q = []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
        yield u