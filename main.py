#Q3
# nformation a l'utilisateur pour les metadonnées du dataset
nom = input("Entrez le nom du dataset: ")
domaine = input("Entrez le domaine du dataset: ")
nbr_lignes = int(input("Entrez le nombre de lignes du dataset: "))
nbr_colonnes = int(input("Entrez le nombre de colonnes du dataset: "))
taille = float(input("Entrez la taille du dataset (en Mo): "))
format = input("Entrez le format du dataset (CSV, JSON): ")
public = input("Le dataset est-il public ? (true/false): ")

#Q4
# Affichage des informations du dataset
print("\nRésumé formaté du dataset:")
print(f"Nom du dataset       : {nom}")
print(f"Domaine du dataset   : {domaine}")
print(f"Nombre de lignes     : {nbr_lignes}")
print(f"Nombre de colonnes   : {nbr_colonnes}")
print(f"Taille du dataset    : {taille}")
print(f"Format du dataset    : {format}")
print(f"Public du dataset    : {public}")
