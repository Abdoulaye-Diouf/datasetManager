
# Fonction statistiques des datasets
def statistiques(catalogue_data):
    #Affiche des statistiques globales sur les datasets du catalogue.#
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