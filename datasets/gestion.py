# Tuple contenant les domaines de datasets
domaine_auto = ("Santé", "Finance", "Agriculture", "Transport", "Éducation")


# Fonction pour ajouter un dataset au catalogue
def ajouter_dataset(catalogue_data):
    #Demande les infos d'un dataset à l'utilisateur et l'ajoute au catalogue.
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



# Fonction pour rechercher un dataset par son nom
def rechercher_dataset(catalogue_data):
    #Recherche un dataset par son nom et l'affiche s'il existe.
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
    #Trie les datasets par nom.#
    catalogue_data.sort(key=lambda x: x["nom"])
    print("Les datasets ont été triés par nom.")


# Fonction suppression d'un dataset
def supprimer_dataset(catalogue_data):
    #Supprime un dataset du catalogue par son nom.
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
    #Modifie un attribut d'un dataset existant.
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