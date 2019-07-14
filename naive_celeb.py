# coding=utf-8


def naive_celeb(G):
    """
    朴素版明星问题, u为明星候选人, v为观众
    :param G:
    :return:
    """
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v:  # 他自己接着循环
                continue
            if G[u][v]:  # 获选人认识你，那么他不是明星
                break
            if not G[v][u]: # 你不认识获选人, 那边他也不是明星
                break
        else:
            return u
    return None


if __name__ == '__main__':
    from random import randrange
    from random import seed
    seed(1000)
    n = 100
    G = [[randrange(2) for _ in range(n)] for i in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = True
        G[c][i] = False
    print(naive_celeb(G))