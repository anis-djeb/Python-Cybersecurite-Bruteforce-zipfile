# Python-Cybersecurity-Bruteforce-zipfile
> Ce projet est basé sur le programme de cybersécurité proposé par AIG sur Forage. Pour plus d'informations, veuillez visiter ce [lien](https://www.theforage.com/simulations/aig/cybersecurity-ku1i).

## Scénario
Un attaquant a exploité une vulnérabilité sur le serveur affecté et a commencé à installer un virus ransomware. Heureusement, l'équipe de détection et de réponse aux incidents a pu empêcher le ransomware de s'installer complètement, il n'a donc réussi qu'à chiffrer un seul fichier zip.  

De plus, lors de l'extraction du document depuis le fichier zip, l'utilisateur est invité à entrer un mot de passe.
En interne, le responsable de la sécurité des systèmes d'information (CISO) ne souhaite pas payer la rançon, car il n'y a aucune garantie que la clé de déchiffrement sera fournie ou que les attaquants ne frapperont pas à nouveau à l'avenir.  

À la place, nous souhaitons que vous réalisiez une attaque par force brute pour retrouver la clé de déchiffrement. D'après la négligence de l'attaquant, nous ne nous attendons pas à ce que la clé soit compliquée, car ils ont utilisé des payloads copiés-collés et ont immédiatement essayé d'utiliser le ransomware au lieu de se déplacer latéralement dans le réseau.

## Implémentation
### Importer et définir la première fonction  
* 'zf_handle' = gestionnaire du fichier Zip.  
* 'zf_handle.extractall(pwd=password)' : tente d'extraire tout le contenu du fichier ZIP en utilisant le mot de passe fourni. Si le mot de passe est correct, l'extraction réussira.  
* Mot de passe : paramètre utilisé pour tenter de déchiffrer le fichier ZIP protégé par mot de passe.

```python
from zipfile import ZipFile
# Utiliser une méthode pour tenter d'extraire le fichier zip avec un mot de passe donné
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False
```

### Exécution (itération sur les mots de passe, extraction du zip, gestion des succès/échecs)

* Définition de main() : fonction principale qui réalise l'attaque par force brute.  
* ZipFile enc.zip : ouvre le fichier ZIP nommé 'enc.zip' avec la classe ZipFile. Le gestionnaire de contexte (with) assure la fermeture correcte du fichier.  
* with open('rockyou.txt', 'rb') as f : ouvre le fichier 'rockyou.txt' en mode binaire, supposé contenir une liste de mots de passe, un par ligne.  
* for p in f : itère sur chaque ligne du fichier de mots de passe.  
* password = p.strip() : supprime les espaces en début et fin de chaîne.  
* Appelle attempt_extract avec le mot de passe courant. Si l'extraction réussit (mot de passe correct), affiche un message et quitte le programme. Sinon, affiche un message d'échec.  
* Le bloc if __name__ == "__main__": assure que main() s'exécute uniquement si le script est lancé directement.

```python
def main():
    print("[+] Début de l'attaque par force brute")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for p in f:
                password = p.strip()
                if attempt_extract(zf, password):
                    print('[+] Mot de passe correct trouvé : %s' % password)
                    exit(0)
                else:
                    print('[-] Mot de passe incorrect : %s' % password)

    print("[+] Mot de passe non trouvé dans la liste")

if __name__ == "__main__":
    main()
```

### Résultat  
* Le code extraira le fichier du zip et le document sera affiché dans le même répertoire où vous exécutez bruteforce.py.  
* Pour votre commodité, j'ai joint la sortie dans le dossier "Output".
