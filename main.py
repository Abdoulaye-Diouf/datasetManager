# #Q3
# # nformation a l'utilisateur pour les metadonnées du dataset
# nom = input("Entrez le nom du dataset: ")
# domaine = input("Entrez le domaine du dataset: ")
# nbr_lignes = int(input("Entrez le nombre de lignes du dataset: "))
# nbr_colonnes = int(input("Entrez le nombre de colonnes du dataset: "))
# taille = float(input("Entrez la taille du dataset (en Mo): "))
# format = input("Entrez le format du dataset (CSV, JSON): ")
# public = input("Le dataset est-il public ? (true/false): ")

# #Q4
# # Affichage des informations du dataset
# print("\nRésumé formaté du dataset:")
# print(f"Nom du dataset       : {nom}")
# print(f"Domaine du dataset   : {domaine}")
# print(f"Nombre de lignes     : {nbr_lignes}")
# print(f"Nombre de colonnes   : {nbr_colonnes}")
# print(f"Taille du dataset    : {taille}")
# print(f"Format du dataset    : {format}")
# print(f"Public du dataset    : {public}")

#Q5
#Menu interactif pour l'utilisateur provisoirement
active = True
while active:
    print("\n ===== Menu =====")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. Quitter \n")

    choix = input("Entrez votre choix (1-4): ")

    #Q6 Dictionnaire pour stocker les datasets 
    if choix == "1":
        # Ajouter un dataset
        nom = input("Entrez le nom du dataset: ")
        domaine = input("Entrez le domaine du dataset: ")
        nbr_lignes = int(input("Entrez le nombre de lignes du dataset: "))
        nbr_colonnes = int(input("Entrez le nombre de colonnes du dataset: "))
        taille = float(input("Entrez la taille du dataset (en Mo): "))
        format = input("Entrez le format du dataset (CSV, JSON): ")
        public = input("Le dataset est-il public ? (true/false): ")

        # Stockage des informations du dataset dans un dictionnaire
        dataset = {
            "nom": nom,
            "domaine": domaine,
            "nbr_lignes": nbr_lignes,
            "nbr_colonnes": nbr_colonnes,
            "taille": taille,
            "format": format,
            "public": public
        }

        # Affichage des informations du dataset ajouté
        print("\nRésumé du dataset ajouté:")
        print(f"Nom du dataset       : {dataset['nom']}")
        print(f"Domaine du dataset   : {dataset['domaine']}")
        print(f"Nombre de lignes     : {dataset['nbr_lignes']}")
        print(f"Nombre de colonnes   : {dataset['nbr_colonnes']}")
        print(f"Taille du dataset    : {dataset['taille']}")
        print(f"Format du dataset    : {dataset['format']}")
        print(f"Public du dataset    : {dataset['public']}")

    elif choix == "2":
        # Afficher les datasets (fonctionnalité à implémenter)
        print("Affichage des datasets (fonctionnalité à implémenter)")

    elif choix == "3":
        # Rechercher un dataset (fonctionnalité à implémenter)
        print("Recherche d'un dataset (fonctionnalité à implémenter)")

    elif choix == "4":
        # Quitter le programme
        print("Au revoir !")
        active = False
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

    
