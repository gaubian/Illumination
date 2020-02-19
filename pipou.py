# tab is an array of array st tab[i] is the list of lights for switch i
# n is the number of lights
# m is the number of switches
def parse():
    tab = []
    [n, m] = list(map(int, input().split(',')))
    for i in range(m):
        l = list(map(int, input().split(',')))
        tab.append(l)
    return (tab, n, m)

def greedy(G, n, m):
    lights = n * [False]
    switches = m * [False]
    while True:
        b = False
        for i in range(m):
            nb = 0
            for j in G[i]:
                if not lights[j]:
                    nb += 1
            if 2 * nb > len(G[i]):
                b = True
                switches[i] = not switches[i]
                for j in G[i]:
                    lights[j] = not lights[j]
        if not b:
            break
    return [i for i in range(m) if switches[i]]

def count_score(G, n, m, tab):
    lights = n * [False]
    for i in tab:
        for j in G[i]:
            lights[j] = not lights[j]
    return len([i for i in range(n) if lights[i]])

def output_sol(tab):
    for x in tab:
        print(x)

def analysis(G, n, m):
    revG = [[] for i in range(n)]
    for i in range(m):
        for j in G[i]:
            revG[j].append(i)
    print(sorted([len(tab) for tab in revG]))

#(G, n, m) = parse()
#analysis(G, n, m)
#sol = greedy(G, n, m)
#output_sol(sol)
