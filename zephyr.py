from pipou import parse
import random

(tab, n, m) = parse()


GRAND_NOMBRE = 1000


# tab is an array of array st tab[i] is the list of lights for switch i
# n is the number of lights
# m is the number of switches


#output = open("output_greedy.txt", "r")
#output = open("output_quatrup.txt", "r")
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

    def aux(liste_a_changer, interrupteurs):
        if liste_a_changer == []:
            return interrupteurs

        else:
            interrupteursS = aux(liste_a_changer[1:], interrupteurs)
            maxiS = nombre_lampes_allumees(tab, n, list_output(interrupteursS))

            interrupteurs[liste_a_changer[0]] = not interrupteurs[liste_a_changer[0]]
            interrupteursN = aux(liste_a_changer[1:], interrupteurs)
            maxiN = nombre_lampes_allumees(tab, n, list_output(interrupteursN))

            if maxiS > maxiN:
                interrupteurs = interrupteursS[:]

            else:
                interrupteurs = interrupteursN[:]

            #print(interrupteurs)
            return interrupteurs

    return aux(liste_a_changer, interrupteurs)


def k_amelioration(k, m, n, output):
    #output = [random.randint(0,300),random.randint(0,300), random.randint(0, 300)]
    nombre_lampes = nombre_lampes_allumees(tab, n, output)
    output_maxi = output

    for i in range(GRAND_NOMBRE):
        if len(output) > 2:
            liste_a_changer = random.sample(list(range(m)), k-1) + random.sample(output, 1)
        else:
            liste_a_changer = random.sample(list(range(m)), k)

        #print(liste_a_changer)

        interrupteurs = amelioration(liste_a_changer, m, n, output)

        maxi = nombre_lampes_allumees(tab, n, list_output(interrupteurs))
        if maxi > nombre_lampes:
            nombre_lampes = maxi
            output_maxi = list_output(interrupteurs)

    return output_maxi

#while True:
#    liste = k_amelioration(5, m, n, output)
#    print(liste, nombre_lampes_allumees(tab, n, liste))
