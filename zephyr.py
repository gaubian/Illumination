from pipou import parse

(tab, n, m) = parse()
# tab is an array of array st tab[i] is the list of lights for switch i
# n is the number of lights
# m is the number of switches

output = open("output.txt", "r")
output = output.read()

l = list(map(int, ouput.split(',')))

def nombre_lampes_allumees(tab, m, output):
    lampes = [0 for _ in range(m)]

    for switch in output:
        for lamp in tab[switch]:
            lampes[lamp] = 1 - lampes[lamp]

    return sum(lampes)
