
# affiche les messages d'accueil et les questions
print('\n\n***********************************************************\n')
print('                SIMPLON THEATER')
print('\n***********************************************************\n\n')

# initialisation
# crée la salle -> Creates a list containing 5 lists, each of 8 items, all set to 0
rangees = 8
colonnes = 9
Places = [['-' for x in range(rangees)] for y in range(colonnes)]

def choisir_la_place():
    print('Appuyer < X > pour sortir du programme.\n')
    nombre_place = input('1 - Combien de places voulez vous acheter ?')
    if (nombre_place =='X' or nombre_place =='x' ):
        quit()
    numero_rangee = input('2 - A quelle rangée voulez vous aller ?')
    if (numero_rangee =='X' or numero_rangee =='x' ):
        quit()
    print('\n\n***********************************************************')

    # verifie les places vide dans la rangée
    # calcul place vide
    vide = 0
    for rang in range(0, 8):
        if Places[int(numero_rangee)][rang] == '-':
            vide = vide + 1
    
    print(f"il y'a {vide} places vide en rangée {numero_rangee}.")

    if vide > int(nombre_place):
        # remplace des places vides
        p = 0
        for rang in range(colonnes):
            if p >= int(nombre_place):
                break
            if Places[rang][int(numero_rangee)] == '-':
                Places[rang][int(numero_rangee)] = 'X'
                p = p + 1

    
def affiche_la_salle():
    # affiche la salle
    for x in range(rangees):
        print(str(x) + ' | ', end='')
        for y in range(colonnes):
            place = Places[y][x]
            print('[ ' + place + ' ]', end='')
        print('')
    print('      ', end='')
    for y in range(colonnes):
            print(str(y) + '    ', end='') 
    print('\n\n***********************************************************\n\n')

while(True):
    affiche_la_salle()
    choisir_la_place()

