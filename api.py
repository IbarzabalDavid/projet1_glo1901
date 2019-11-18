"""Ceci est mon api"""
import requests


def lister_parties(idul):
    """Ceci me permet de lister les parties"""
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(url_base+'lister/', params={'idul': idul})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if 'message' in rep:
            raise RuntimeError(rep['message'])
        return rep
    print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")

def débuter_partie(idul):
    """Ceci debute la partie"""
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if 'message' in rep:
            raise RuntimeError(rep['message'])
        return (rep['id'], rep['état'])
    print(f"Le POST sur {url_base+'debuter'} a produit le code d'erreur {rep.status_code}.")

def jouer_coup(id_partie, type_coup, position):
    """Ceci est pour jouer un coup"""
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    temp = 'type'
    rep = requests.post(url_base+'jouer/', data={'id': id_partie, temp: type_coup, 'pos': position})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if 'message' in rep:
            raise RuntimeError(rep['message'])
        if 'gagnant' in rep:
            raise StopIteration(rep['gagnant'])
        return rep['état']
    print(f"Le POST sur {url_base+'debuter'} a produit le code d'erreur {rep.status_code}.")
