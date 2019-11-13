import requests


def lister_parties(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep = requests.get(url_base+'lister/', params={'idul': idul})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if 'message' in rep:
            raise RuntimeError
        print(rep)
        return rep
    
    else:
        print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")

def débuter_partie(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if 'message' in rep:
            raise RuntimeError
        print(rep)
        return (rep['id'], rep['état'])
    
    else:
        print(f"Le POST sur {url_base+'debuter'} a produit le code d'erreur {rep.status_code}.")



lister_parties('daiba')