# coding=utf-8


def celeb(G):
    """
    明星问题正常版， c为候选人
    :param G:
    :return:
    """
    n = len(G)
    u, v = 0, 1 # 从获选人选出前面两个人
    for c in range(2, n+1):
        if G[u][v]:
            u = c   # 如果u认识v那么u就不是明星将下一个候选人给u
        else:
            v = c   # 同上如果u不认识v，那么u有可能是明星, v不是明星, 下一个候选人给v
    if u == n:
        c = v   # 如果u到最后了也不是明星, 只能将v给候选人了
    else:
        c = u   # 跟上面相反
    #   上面将候选人确认了
    for v in range(n):
        if c == v:
            continue
        if G[c][v]:
            break
        if not G[v][c]:
            break
    else:
        return c
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
    print(celeb(G))