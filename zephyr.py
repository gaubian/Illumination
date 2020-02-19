from pipou import parse
import random

(tab, n, m) = parse()


GRAND_NOMBRE = 1000


# tab is an array of array st tab[i] is the list of lights for switch i
# n is the number of lights
# m is the number of switches


#output = open("output_greedy.txt", "r")
#output = open("output_quadrup.txt", "r")
output = open("output_mauvais.txt", "r")

output = output.read()

output = list(map(int, output.split('\n')[:-1]))

def nombre_lampes_allumees(tab, n, output):
    lampes = [0 for _ in range(n)]

    for switch in output:
        for lamp in tab[switch]:
            lampes[lamp] = 1 - lampes[lamp]

    return sum(lampes)


#print(nombre_lampes_allumees(tab, n, output))
def list_output(interrupteurs):
    return [i for i in range(m) if interrupteurs[i]]

def list_interrupteurs(output):
    interrupteurs = [False for _ in range(m)]

    for switch in output:
        interrupteurs[switch] = True

    return interrupteurs


def amelioration(liste_a_changer, m, n, output):
    '''teste toutes les possibilités pour les interrupteurs de liste_a_changer
    et sélectionne la meilleure'''  
    interrupteurs = list_interrupteurs(output)

    def aux(liste_a_changer, maxi, interrupteurs):
        if liste_a_changer == []:
            return nombre_lampes_allumees(tab, n, list_output(interrupteurs)), interrupteurs

        else:
            maxiS, interrupteursS = aux(liste_a_changer[1:], maxi, interrupteurs)
            interrupteurs[liste_a_changer[0]] = not interrupteurs[liste_a_changer[0]]
            maxiN, interrupteursN = aux(liste_a_changer[1:], maxi, interrupteurs)

            if maxiS > maxi:
                maxi = maxiS
                interrupteurs = interrupteursS[:]
                interrupteurs[liste_a_changer[0]] = not interrupteurs[liste_a_changer[0]]

            if maxiN > maxi:
                maxi = maxiN
                interrupteurs = interrupteursN[:]

            else:
                interrupteurs[liste_a_changer[0]] = not interrupteurs[liste_a_changer[0]]

            return maxi, interrupteurs

    return aux(liste_a_changer, nombre_lampes_allumees(tab, n, output), interrupteurs)


def k_amelioration(k, m, n, output):
    nombre_lampes = nombre_lampes_allumees(tab, n, output)

    for i in range(GRAND_NOMBRE):
        liste_a_changer = random.sample(list(range(m)), k)

        maxi, interrupteurs = amelioration(liste_a_changer, m, n, output)
        
        if maxi > nombre_lampes:
            nombre_lampes = maxi
            output = list_output(interrupteurs)

    return output

print(k_amelioration(1, m, n, output))
