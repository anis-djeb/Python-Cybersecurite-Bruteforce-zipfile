"""
Programme de cybersécurité Forage AIG
Modèle de départ pour attaque par force brute
"""

from zipfile import ZipFile

# Méthode pour tenter d'extraire le fichier zip avec un mot de passe donné
def tenter_extraction(zf_handle, mot_de_passe):
    try:
        zf_handle.extractall(pwd=mot_de_passe)
        return True
    except:
        return False

def main():
    print("[+] Début de l'attaque par force brute")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for p in f:
                # Logique ici
                # Parcourir les mots de passe dans rockyou.txt
                # Tenter d'extraire le fichier zip avec chaque mot de passe
                mot_de_passe = p.strip()
                # Gérer extraction réussie ou échec
                if tenter_extraction(zf, mot_de_passe):
                    print('[+] Mot de passe correct trouvé : %s' % mot_de_passe)
                    exit(0)
                else:
                    print('[-] Mot de passe incorrect : %s' % mot_de_passe)
    # Mot de passe non trouvé dans la liste
    print("[+] Mot de passe non trouvé dans la liste")

if __name__ == "__main__":
    main()
