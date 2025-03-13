import os

# Chemin du dossier à lister
dossier = "/Users/antonin/Desktop/Programmation/Symfony"

# Lister les fichiers et dossiers
def lister_contenu(chemin):
    try:
        fichiers = os.listdir(chemin)  # Liste les fichiers/dossiers
        print(f"Contenu du dossier {chemin} :")
        for fichier in fichiers:
            print(f"- {fichier}")
    except FileNotFoundError:
        print("Le dossier spécifié n'existe pas.")
    except PermissionError:
        print("Accès refusé au dossier.")

# Exécuter la fonction
if __name__ == "__main__":
    lister_contenu(dossier)