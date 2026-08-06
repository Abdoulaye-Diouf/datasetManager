# datasets/gestion.py
from datasets.profiler import analyser_fichier_reel

# Tuple contenant les domaines de datasets
domaine_auto = ("Santé", "Finance", "Agriculture", "Transport", "Éducation")

# Fonction pour ajouter un dataset au catalogue (Mode Manuel ou Auto-Profilage)
def ajouter_dataset(catalogue_data):
    print("\n--- Mode d'ajout ---")
    print("1. Saisie manuelle classique")
    print("2. Import automatique depuis un fichier réel (Bonus)")
    choix_mode = input("Choisissez le mode (1 ou 2): ").strip()

    nom = input("Entrez le nom du dataset: ")

    domaine = input(f"Domaine du dataset {domaine_auto}: ")
    while domaine not in domaine_auto:
        print("Domaine invalide. Veuillez choisir parmi les domaines disponibles.")
        domaine = input(f"Domaine du dataset {domaine_auto}: ")

    public = input("Le dataset est-il public ? (true/false): ")

    # --- MODE 2 : PROFILAGE AUTOMATIQUE ---
    if choix_mode == "2":
        chemin_fichier = input("Entrez le chemin du fichier (.csv ou .json): ").strip('\"\'')
        info_auto = analyser_fichier_reel(chemin_fichier)

        if info_auto is None:
            print("Échec de la détection automatique. Ajout annulé.")
            return

        nbr_lignes = info_auto["nbr_lignes"]
        nbr_colonnes = info_auto["nbr_colonnes"]
        taille = info_auto["taille"]
        format_data = info_auto["format"]

        print(f" Détection réussie : {nbr_lignes} lignes | {nbr_colonnes} colonnes | {taille} Mo | Format: {format_data}")

    # --- MODE 1 : SAISIE MANUELLE CLASSIQUE ---
    else:
        try:
            nbr_lignes = int(input("Entrez le nombre de lignes du dataset: "))
            nbr_colonnes = int(input("Entrez le nombre de colonnes du dataset: "))
            taille = float(input("Entrez la taille du dataset (en Mo): "))
        except ValueError:
            print("Erreur : veuillez saisir un nombre valide. Ajout annulé.")
            return
        format_data = input("Entrez le format du dataset (CSV, JSON): ")

    dataset = {
        "nom": nom,
        "domaine": domaine,
        "nbr_lignes": nbr_lignes,
        "nbr_colonnes": nbr_colonnes,
        "taille": taille,
        "format": format_data,
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
# Adaptation de modifier_dataset pour inclure la conversion automatique
def modifier_dataset(catalogue_data):
    # Modifie un attribut d'un dataset existant
    nom_modification = input("Entrez le nom du dataset à modifier: ")
    dataset_a_modifier = next((d for d in catalogue_data if d["nom"] == nom_modification), None)

    if dataset_a_modifier is None:
        print(f"Erreur : aucun dataset nommé '{nom_modification}' n'a été trouvé.")
        return

    print(f"Dataset trouvé: {dataset_a_modifier['nom']}")
    attribut_a_modifier = input(
        "Quel attribut souhaitez-vous modifier ? "
        "(nom, domaine, nbr_lignes, nbr_colonnes, taille, format, public): "
    ).strip().lower()

    if attribut_a_modifier == "format":
        # Bascule automatique du format
        ancien_fmt = dataset_a_modifier["format"]
        nouveau_fmt = "JSON" if str(ancien_fmt).upper() == "CSV" else "CSV"
        dataset_a_modifier["format"] = nouveau_fmt
        print(f" Format modifié avec succès : {ancien_fmt} ➔ {nouveau_fmt}.")
        print(" N'oubliez pas de sauvegarder (Option 8) pour migrer le dataset dans le bon fichier.")

    elif attribut_a_modifier in dataset_a_modifier:
        nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {attribut_a_modifier}: ")

        try:
            if attribut_a_modifier in ("nbr_lignes", "nbr_colonnes"):
                nouvelle_valeur = int(nouvelle_valeur)
            elif attribut_a_modifier == "taille":
                nouvelle_valeur = float(nouvelle_valeur)

            dataset_a_modifier[attribut_a_modifier] = nouvelle_valeur
            print(f"{attribut_a_modifier} du dataset '{dataset_a_modifier['nom']}' a été modifié avec succès.")
        except ValueError:
            print("Erreur : la nouvelle valeur saisie n'est pas un nombre valide. Modification annulée.")
    else:
        print("Attribut invalide. Veuillez choisir un attribut valide.")


    
# Fonction pour convertir le format d'un dataset (CSV <-> JSON)
def convertir_format_dataset(catalogue_data):
    # Permet de basculer un dataset de CSV vers JSON ou de JSON vers CSV
    nom_conversion = input("Entrez le nom du dataset à convertir : ")
    dataset = next((d for d in catalogue_data if d["nom"] == nom_conversion), None)

    if not dataset:
        print(f"Erreur : aucun dataset nommé '{nom_conversion}' n'a été trouvé.")
        return

    format_actuel = str(dataset.get("format")).upper()

    if format_actuel == "CSV":
        dataset["format"] = "JSON"
        print(f" Le dataset '{dataset['nom']}' a été converti : CSV ➔ JSON.")
    elif format_actuel == "JSON":
        dataset["format"] = "CSV"
        print(f" Le dataset '{dataset['nom']}' a été converti : JSON ➔ CSV.")
    else:
        nouveau_fmt = input("Format inconnu. Choisissez le nouveau format (CSV ou JSON) : ").strip().upper()
        if nouveau_fmt in ("CSV", "JSON"):
            dataset["format"] = nouveau_fmt
            print(f" Le dataset '{dataset['nom']}' est maintenant au format {nouveau_fmt}.")
        else:
            print("Format invalide. Conversion annulée.")
            return

    print(" Note : Effectuez une sauvegarde (Option 8) pour appliquer le transfert dans le fichier correspondant.")