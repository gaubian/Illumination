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
    inp = parse()
    while True:

