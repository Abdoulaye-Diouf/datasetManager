import csv
chemin_csv = r"C:\ODC\veille-python\pratique\code\datasetManager\datasets.csv"

#Tuble contenant les domaines de datasets
domaine_auto = ("Santé", "Finance", "Agriculture", "Transport", "Éducation") 

#liste pour stocker les datasets
catalogue_data = []


#Menu interactif pour l'utilisateur provisoirement
print("\n ===== Menu =====")
print("1. Ajouter un dataset")
print("2. Afficher les datasets")
print("3. Rechercher un dataset")
print("4. trier les datasets")
print("5. Supprimer un dataset")
print("6. Modifier un dataset")
print("7. Voir les statistiques des datasets")
print("8. Sauvegarder les datasets dans un fichier CSV")
print("9. Recharger les datasets depuis un fichier CSV")
print("10. Quitter \n")


active = True
while active:
    

    choix = input("Entrez votre choix (1-10): ")

    #Q6 Dictionnaire pour stocker les datasets 
    if choix == "1":
        # Ajouter un dataset
        nom = input("Entrez le nom du dataset: ")

        domaine = input(f"Domaine du dataset {domaine_auto}: ")
        while domaine not in domaine_auto:
            print("Domaine invalide. Veuillez choisir parmi les domaines disponibles.")
            domaine = input(f"Domaine du dataset {domaine_auto}: ")

        # Gestion des exceptions pour les entrées numériques
        try:
            nbr_lignes = int(input("Entrez le nombre de lignes du dataset: "))
            nbr_colonnes = int(input("Entrez le nombre de colonnes du dataset: "))
            taille = float(input("Entrez la taille du dataset (en Mo): "))
        except ValueError:
            print("Erreur : veuillez entrer des valeurs numériques valides.")
            continue

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

        # Gestion des exceptions pour l'affichage des informations du dataset trouvé
        try:
            if dataset_trouve:
                print(f"Dataset trouvé: {dataset_trouve['nom']}")
            else:
                print("Dataset non trouvé.")
        except KeyError:
            print("Erreur : le dataset trouvé ne contient pas toutes les informations attendues.")

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

        # Gestion des exceptions pour la suppression du dataset
        try:   
            if dataset_a_supprimer:
                catalogue_data.remove(dataset_a_supprimer)
                print(f"Dataset '{dataset_a_supprimer['nom']}' supprimé avec succès.")
            else:
                print("Dataset non trouvé.")
        except ValueError:
            print("Erreur : le dataset à supprimer n'a pas été trouvé dans le catalogue.")
   

    elif choix == "6":
        # Modifier un dataset
        nom_modification = input("Entrez le nom du dataset à modifier: ")
        # Recherche du dataset dans le catalogue
        dataset_a_modifier = None
        for dataset in catalogue_data:
            if dataset["nom"] == nom_modification:
                dataset_a_modifier = dataset
            break 

        # Gestion des exceptions pour la modification du dataset
        try:
            if dataset_a_modifier is None:
                raise KeyError(nom_modification)
            print(f"Dataset trouvé: {dataset_a_modifier['nom']}")
            attribut_a_modifier = input(
                "Quel attribut souhaitez-vous modifier ? "
                "(nom, domaine, nbr_lignes, nbr_colonnes, taille, format, public): "
            )
            if attribut_a_modifier in dataset_a_modifier:
                nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {attribut_a_modifier}: ")

                # --- Gestion de l'exception : saisie non numérique lors de la modification ---
                if attribut_a_modifier in ("nbr_lignes", "nbr_colonnes"):
                    nouvelle_valeur = int(nouvelle_valeur)
                elif attribut_a_modifier == "taille":
                    nouvelle_valeur = float(nouvelle_valeur)

                dataset_a_modifier[attribut_a_modifier] = nouvelle_valeur
                print(f"{attribut_a_modifier} du dataset '{dataset_a_modifier['nom']}' a été modifié avec succès.")
            else:
                print("Attribut invalide. Veuillez choisir un attribut valide.")
        except KeyError:
            print(f"Erreur : aucun dataset nommé '{nom_modification}' n'a été trouvé.")
        except ValueError:
            print("Erreur : la nouvelle valeur saisie n'est pas un nombre valide. Modification annulée.")


    elif choix == "7":
        # les statistiques des datasets
        if not catalogue_data:
            print("Aucun dataset enregistré pour le moment.")
        else:
            total_datasets = len(catalogue_data)
            total_lignes = sum(dataset["nbr_lignes"] for dataset in catalogue_data)
            moyenne_colonnes = sum(dataset["nbr_colonnes"] for dataset in catalogue_data) / total_datasets if total_datasets > 0 else 0
            total_taille = sum(dataset["taille"] for dataset in catalogue_data)
            data_public = sum(1 for dataset in catalogue_data if dataset["public"].lower() == "true")
            data_prive = total_datasets - data_public
            nb_csv = sum(1 for dataset in catalogue_data if dataset["format"].lower() == "csv")
            nb_json = sum(1 for dataset in catalogue_data if dataset["format"].lower() == "json")
            rp_domaine = {}
            for dataset in catalogue_data:
                domaine = dataset["domaine"]
                if domaine in rp_domaine:
                    rp_domaine[domaine] += 1
                else:
                    rp_domaine[domaine] = 1

            print("\n--- Statistiques des datasets ---")
            print(f"Nombre total de datasets : {total_datasets}")
            print(f"Nombre total de lignes   : {total_lignes}")
            print(f"Moyenne de colonnes      : {moyenne_colonnes:.2f}")
            print(f"Taille totale des datasets : {total_taille} Mo")
            print(f"Datasets publics : {data_public}")
            print(f"Datasets privés : {data_prive}")
            print(f"Nombre de datasets au format CSV : {nb_csv}")
            print(f"Nombre de datasets au format JSON : {nb_json}")
            print("Répartition des datasets par domaine :")
            for domaine, count in rp_domaine.items():
                print(f"- {domaine} : {count} datasets")

    elif choix == "8":
        # Sauvegarder les datasets dans un fichier CSV
        with open(chemin_csv, mode='w', newline='', encoding='utf-8') as fichier_csv:
            if catalogue_data:
                champs = catalogue_data[0].keys()
                lecteur_csv = csv.DictWriter(fichier_csv, fieldnames=champs)
                lecteur_csv.writeheader()
                lecteur_csv.writerows(catalogue_data)
        print("Les datasets ont été sauvegardés dans le fichier CSV avec succès.")

    

    elif choix == "9":
        # Recharger et Affichager des datasets depuis un fichier CSV
        # Gestion des exceptions pour la lecture du fichier CSV
        try:
            with open(chemin_csv, mode='r', newline='', encoding='utf-8') as fichier_csv:
                lecteur_csv = csv.DictReader(fichier_csv)
                catalogue_data = [dict(row) for row in lecteur_csv]
            print("Les datasets ont été rechargés depuis le fichier CSV avec succès.")

            # afficher les datasets rechargés
            if not catalogue_data:
                print("Aucun dataset enregistré pour le moment.")
            else:
                print("\n--- Liste des datasets rechargés ---")
                for dataset in catalogue_data:
                    print(f"-nom : {dataset['nom']}\n domaine : {dataset['domaine']}\n  "
                        f" lignes :  {dataset['nbr_lignes']}\n format : {dataset['format']}")

        except FileNotFoundError:
            print("Erreur : le fichier CSV n'existe pas.")
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier CSV : {e}")
      

    elif choix == "10":
        # Quitter le programme
        print("Au revoir !")
        active = False
  
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 10.")