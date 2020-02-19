def parse():
    tab = []
    [n, m] = list(map(int, input().split(',')))
    for i in range(m):
        l = list(map(int, input().split(',')))
        tab.append(l)
    return tab
