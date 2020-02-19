from pipou import parse

(tab, n, m) = parse()
# tab is an array of array st tab[i] is the list of lights for switch i
# n is the number of lights
# m is the number of switches

output = open("output_greedy.txt", "r")
output = output.read()

output = list(map(int, output.split('\n')[:-1]))

def nombre_lampes_allumees(tab, n, output):
    lampes = [0 for _ in range(n)]

    for switch in output:
        for lamp in tab[switch]:
            lampes[lamp] = 1 - lampes[lamp]

    return sum(lampes)


print(nombre_lampes_allumees(tab, n, output))