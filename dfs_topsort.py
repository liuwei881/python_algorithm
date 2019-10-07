# coding=utf-8


def dfs_topsort(G):
    """
    基于深度优先搜索的拓扑排序
    :param G:
    :return:
    """
    S, res = set(), []

    def recurse(u):
        if u in S: return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res