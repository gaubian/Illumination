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

def greedy():
    (G, n, m) = parse()
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

def output_sol(tab):
    for x in tab:
        print(x)
