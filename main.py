import csv

chemin_csv = r"C:\ODC\veille-python\pratique\code\datasetManager\datasets.csv"

# Tuple contenant les domaines de datasets
domaine_auto = ("Santé", "Finance", "Agriculture", "Transport", "Éducation")

#fonction affichage du menu
def afficher_menu():
    """Affiche le menu principal."""
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

# Fonction pour ajouter un dataset au catalogue
def ajouter_dataset(catalogue_data):
    """Demande les infos d'un dataset à l'utilisateur et l'ajoute au catalogue."""
    nom = input("Entrez le nom du dataset: ")

    domaine = input(f"Domaine du dataset {domaine_auto}: ")
    while domaine not in domaine_auto:
        print("Domaine invalide. Veuillez choisir parmi les domaines disponibles.")
        domaine = input(f"Domaine du dataset {domaine_auto}: ")

    # --- Gestion de l'exception : saisie non numérique ---
    try:
        nbr_lignes = int(input("Entrez le nombre de lignes du dataset: "))
        nbr_colonnes = int(input("Entrez le nombre de colonnes du dataset: "))
        taille = float(input("Entrez la taille du dataset (en Mo): "))
    except ValueError:
        print("Erreur : veuillez saisir un nombre valide pour les lignes, colonnes ou la taille. "
              "Ajout du dataset annulé.")
        return

    format = input("Entrez le format du dataset (CSV, JSON): ")
    public = input("Le dataset est-il public ? (true/false): ")

    dataset = {
        "nom": nom,
        "domaine": domaine,
        "nbr_lignes": nbr_lignes,
        "nbr_colonnes": nbr_colonnes,
        "taille": taille,
        "format": format,
        "public": public
    }

    catalogue_data.append(dataset)

    print("\nRésumé du dataset ajouté:")
    print(f"Nom du dataset       : {dataset['nom']}")
    print(f"Domaine du dataset   : {dataset['domaine']}")
    print(f"Nombre de lignes     : {dataset['nbr_lignes']}")
    print(f"Nombre de colonnes   : {dataset['nbr_colonnes']}")
    print(f"Taille du dataset    : {dataset['taille']}")
    print(f"Format du dataset    : {dataset['format']}")
    print(f"Public du dataset    : {dataset['public']}")

# Fonction pour afficher les datasets
def afficher_datasets(catalogue_data):
    """Affiche la liste résumée des datasets du catalogue."""
    if not catalogue_data:
        print("Aucun dataset enregistré pour le moment.")
    else:
        print("\n--- Liste des datasets ---")
        for dataset in catalogue_data:
            print(f"- {dataset['nom']} | {dataset['domaine']} | "
                  f"{dataset['nbr_lignes']} lignes | {dataset['format']}")

# Fonction pour rechercher un dataset par son nom
def rechercher_dataset(catalogue_data):
    """Recherche un dataset par son nom et l'affiche s'il existe."""
    nom_recherche = input("Entrez le nom du dataset à rechercher: ")
    dataset_trouve = None
    for dataset in catalogue_data:
        if dataset["nom"] == nom_recherche:
            dataset_trouve = dataset
            break

    # --- Gestion de l'exception : dataset recherché inexistant ---
    try:
        if dataset_trouve is None:
            raise KeyError(nom_recherche)
        print(f"Dataset trouvé: {dataset_trouve['nom']}")
    except KeyError:
        print(f"Erreur : aucun dataset nommé '{nom_recherche}' n'a été trouvé.")

# Fonction pour trier les datasets par nom
def trier_dataset(catalogue_data):
    """Trie les datasets par nom."""
    catalogue_data.sort(key=lambda x: x["nom"])
    print("Les datasets ont été triés par nom.")

# Fonction suppression d'un dataset
def supprimer_dataset(catalogue_data):
    """Supprime un dataset du catalogue par son nom."""
    nom_suppression = input("Entrez le nom du dataset à supprimer: ")
    dataset_a_supprimer = None
    for dataset in catalogue_data:
        if dataset["nom"] == nom_suppression:
            dataset_a_supprimer = dataset
            break

    # --- Gestion de l'exception : dataset à supprimer inexistant ---
    try:
        if dataset_a_supprimer is None:
            raise KeyError(nom_suppression)
        catalogue_data.remove(dataset_a_supprimer)
        print(f"Dataset '{dataset_a_supprimer['nom']}' supprimé avec succès.")
    except KeyError:
        print(f"Erreur : aucun dataset nommé '{nom_suppression}' n'a été trouvé.")

# Fonction pour modifier dataset
def modifier_dataset(catalogue_data):
    """Modifie un attribut d'un dataset existant."""
    nom_modification = input("Entrez le nom du dataset à modifier: ")
    dataset_a_modifier = None
    for dataset in catalogue_data:
        if dataset["nom"] == nom_modification:
            dataset_a_modifier = dataset
            break

    # --- Gestion de l'exception : dataset à modifier inexistant ---
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

# Fonction statistiques des datasets
def statistiques(catalogue_data):
    """Affiche des statistiques globales sur les datasets du catalogue."""
    if not catalogue_data:
        print("Aucun dataset enregistré pour le moment.")
        return

    total_datasets = len(catalogue_data)
    total_lignes = sum(dataset["nbr_lignes"] for dataset in catalogue_data)
    moyenne_colonnes = (sum(dataset["nbr_colonnes"] for dataset in catalogue_data) / total_datasets
                         if total_datasets > 0 else 0)
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

# Fonction sauvegarder les datasets dans un fichier CSV
def sauvegarder(catalogue_data):
    """Sauvegarde le catalogue de datasets dans un fichier CSV."""
    try:
        with open(chemin_csv, mode='w', newline='', encoding='utf-8') as fichier_csv:
            if catalogue_data:
                champs = catalogue_data[0].keys()
                lecteur_csv = csv.DictWriter(fichier_csv, fieldnames=champs)
                lecteur_csv.writeheader()
                lecteur_csv.writerows(catalogue_data)
        print("Les datasets ont été sauvegardés dans le fichier CSV avec succès.")
    except OSError as e:
        print(f"Erreur : impossible d'écrire dans le fichier '{chemin_csv}' ({e}).")

# Fonction recharger les datasets depuis un fichier CSV
def recharger():
    """Recharge le catalogue de datasets depuis le fichier CSV et le retourne."""
    catalogue_data = []
    # --- Gestion des exceptions : fichier inexistant / fichier vide ---
    try:
        with open(chemin_csv, mode='r', newline='', encoding='utf-8') as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            catalogue_data = [dict(row) for row in lecteur_csv]

        if not catalogue_data:
            print("Le fichier CSV est vide. Aucun dataset n'a été chargé.")
        else:
            print("Les datasets ont été rechargés depuis le fichier CSV avec succès.")
            print("\n--- Liste des datasets rechargés ---")
            for dataset in catalogue_data:
                print(f"-nom : {dataset['nom']}\n domaine : {dataset['domaine']}\n  "
                      f" lignes :  {dataset['nbr_lignes']}\n format : {dataset['format']}")

    except FileNotFoundError:
        print(f"Erreur : le fichier '{chemin_csv}' n'existe pas. Veuillez d'abord sauvegarder un catalogue (option 8).")
    except OSError as e:
        print(f"Erreur lors de la lecture du fichier : {e}")

    return catalogue_data


def main():
    catalogue_data = []
    afficher_menu()

    active = True
    while active:
        choix = input("Entrez votre choix (1-10): ")

        if choix == "1":
            ajouter_dataset(catalogue_data)
        elif choix == "2":
            afficher_datasets(catalogue_data)
        elif choix == "3":
            rechercher_dataset(catalogue_data)
        elif choix == "4":
            trier_dataset(catalogue_data)
        elif choix == "5":
            supprimer_dataset(catalogue_data)
        elif choix == "6":
            modifier_dataset(catalogue_data)
        elif choix == "7":
            statistiques(catalogue_data)
        elif choix == "8":
            sauvegarder(catalogue_data)
        elif choix == "9":
            catalogue_data = recharger()
        elif choix == "10":
            print("Au revoir !")
            active = False
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 10.")


if __name__ == "__main__":
    main()