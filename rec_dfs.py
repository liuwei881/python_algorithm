# coding=utf-8


def rec_dfs(G, s, S=None):
    """
    递归版的深度优先搜索
    :param G:
    :param s:
    :param S:
    :return:
    """
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        rec_dfs(G, u, S)