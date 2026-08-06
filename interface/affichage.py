# affichage.py

# Fonction pour afficher les datasets séparés par format (CSV et JSON)
def afficher_datasets(catalogue_data):
    # Affiche la liste résumée des datasets du catalogue en séparant par format.
    if not catalogue_data:
        print("Aucun dataset enregistré pour le moment.")
        return

    datasets_csv = [d for d in catalogue_data if str(d.get("format")).lower() == "csv"]
    datasets_json = [d for d in catalogue_data if str(d.get("format")).lower() == "json"]
    autres_formats = [d for d in catalogue_data if str(d.get("format")).lower() not in ("csv", "json")]

    print("\n--- Datasets au format CSV ---")
    if datasets_csv:
        for dataset in datasets_csv:
            print(f"- {dataset['nom']} | {dataset['domaine']} | "
                  f"{dataset['nbr_lignes']} lignes | {dataset['format']}")
    else:
        print("Aucun dataset CSV.")

    print("\n--- Datasets au format JSON ---")
    if datasets_json:
        for dataset in datasets_json:
            print(f"- {dataset['nom']} | {dataset['domaine']} | "
                  f"{dataset['nbr_lignes']} lignes | {dataset['format']}")
    else:
        print("Aucun dataset JSON.")

    if autres_formats:
        print("\n--- Autres formats ---")
        for dataset in autres_formats:
            print(f"- {dataset['nom']} | {dataset['domaine']} | "
                  f"{dataset['nbr_lignes']} lignes | {dataset['format']}")