import argparse


import api


def analyser_commande():
    # créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description = "Jeux Quoridor - phase 1")
    
    # insérer ici avec les bons appels à la méthode add_argument
    parser.add_argument('idul', help = 'IDUL du joueur.')
    parser.add_argument('-l', '--lister', help = 'Lister les identifiants de vos 20 dernières parties', action = 'store_true')
    return parser.parse_args()

def afficher_damier_ascii(dico):
    tabMv = [[' 'for i in range(8)]for i in range(17)]
    tabMh = [[' 'for i in range(35)]for i in range(8)]
    tabJ = [['.'for i in range(9)]for i in range(9)]
    for i in dico['joueurs']:
        if i['nom'] == 'automate':
            tabJ[9-(i['pos'][1])][(i['pos'][0])-1]='2'
        else:
            tabJ[9-(i['pos'][1])][(i['pos'][0])-1]='1'
    for i in dico['murs']['verticaux']:
        tabMv[int(17-(i[1]*2)+1)][i[0]-2] = '|'
        tabMv[int(17-(i[1]*2))][i[0]-2] = '|'
        tabMv[int(17-(i[1]*2)-1)][i[0]-2] = '|'
    for i in dico['murs']['horizontaux']:
        for b in range(6):
            tabMh[9-i[1]][int(i[0]*4)-4+b] = '-'
    counter = 18
    print(f'Légende: 1={dico["joueurs"][0]["nom"]}, 2=automate')
    print(' ' * 3 + '-' * 35)
    for i in range(17):
        a = ""
        if i % 2 == 0:
            for j in range(36):
                if j == 0:
                    a += f"{str(int(counter/2))} |"
                elif j % 2 == 1:
                    a += ' '
                elif (j+2) % 4 == 0:
                    a += tabJ[int(i/2)][int((j-1)/4)]
                else:
                    a += tabMv[i][int(j/4)-1]
        else:
            a = '  |'
            for j in range(35):
                if (j-3) % 4 == 0 and tabMv[i][int((j-3)/4)] != ' ':
                    a += tabMv[i][int((j-3)/4)]
                else:
                    a += tabMh[int((i-1)/2)][j]
        print(f"{a}|")
        counter -= 1
    print('--|' + '-'*35)
    print('  | 1   2   3   4   5   6   7   8   9')



test = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": [9, 9]}, 
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ], 
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [8, 9]], 
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
}
afficher_damier_ascii(test)