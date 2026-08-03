#Tuble contenant les domaines de datasets
domaine_auto = ("Santé", "Finance", "Agriculture", "Transport", "Éducation") 

#liste pour stocker les datasets
catalogue_data = []


#Menu interactif pour l'utilisateur provisoirement
active = True
while active:
    print("\n ===== Menu =====")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. trier les datasets")
    print("5. Supprimer un dataset")
    print("6. Modifier un dataset")
    print("7. Quitter \n")

    choix = input("Entrez votre choix (1-7): ")

    #Q6 Dictionnaire pour stocker les datasets 
    if choix == "1":
        # Ajouter un dataset
        nom = input("Entrez le nom du dataset: ")

        domaine = input(f"Domaine du dataset {domaine_auto}: ")
        while domaine not in domaine_auto:
            print("Domaine invalide. Veuillez choisir parmi les domaines disponibles.")
            domaine = input(f"Domaine du dataset {domaine_auto}: ")

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

        # Ajout du dataset au catalogue
        catalogue_data.append(dataset)

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
        if not catalogue_data:
            print("Aucun dataset enregistré pour le moment.")
        else:
            print("\n--- Liste des datasets ---")
            for dataset in catalogue_data:
                print(f"- {dataset['nom']} | {dataset['domaine']} | "
                    f"{dataset['nbr_lignes']} lignes | {dataset['format']}")

    elif choix == "3":
        # Rechercher un dataset
        nom_recherche = input("Entrez le nom du dataset à rechercher: ")
        # Recherche du dataset dans le catalogue
        dataset_trouve = None
        for dataset in catalogue_data:
            if dataset["nom"] == nom_recherche:
                dataset_trouve = dataset
                break
        if dataset_trouve:
            print(f"Dataset trouvé: {dataset_trouve['nom']}")
        else:
            print("Dataset non trouvé.")

    elif choix == "4":
        # Trier les datasets 
        catalogue_data.sort(key=lambda x: x["nom"])
        print("Les datasets ont été triés par nom.")

    elif choix == "5":
        # Supprimer un dataset
        nom_suppression = input("Entrez le nom du dataset à supprimer: ")
        # Recherche du dataset dans le catalogue
        dataset_a_supprimer = None
        for dataset in catalogue_data:
            if dataset["nom"] == nom_suppression:
                dataset_a_supprimer = dataset
                break
        if dataset_a_supprimer:
            catalogue_data.remove(dataset_a_supprimer)
            print(f"Dataset '{dataset_a_supprimer['nom']}' supprimé avec succès.")
        else:
            print("Dataset non trouvé.")

   

    elif choix == "6":
        # Modifier un dataset
        nom_modification = input("Entrez le nom du dataset à modifier: ")
        # Recherche du dataset dans le catalogue
        dataset_a_modifier = None
        for dataset in catalogue_data:
            if dataset["nom"] == nom_modification:
                dataset_a_modifier = dataset
            break   
        if dataset_a_modifier:
            print(f"Dataset trouvé: {dataset_a_modifier['nom']}")
            attribut_a_modifier = input(
                "Quel attribut souhaitez-vous modifier ? "
                "(nom, domaine, nbr_lignes, nbr_colonnes, taille, format, public): "
            )
            if attribut_a_modifier in dataset_a_modifier:
                nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {attribut_a_modifier}: ")
                dataset_a_modifier[attribut_a_modifier] = nouvelle_valeur
                print(f"{attribut_a_modifier} du dataset '{dataset_a_modifier['nom']}' a été modifié avec succès.")
            else:
                print("Attribut invalide. Veuillez choisir un attribut valide.")
        else:
            print("Dataset non trouvé.")


    elif choix == "7":
        # Quitter le programme
        print("Au revoir !")
        active = False
  
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 7.")

    
