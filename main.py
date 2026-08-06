# main.py
from interface.menu import afficher_menu
from datasets.gestion import (
    ajouter_dataset,
    rechercher_dataset,
    trier_dataset,
    supprimer_dataset,
    modifier_dataset
)
from stockage.csv_manager import sauvegarder_csv, recharger_csv
from stockage.json_manager import sauvegarder_json, recharger_json
from datasets.statistiques import statistiques
from interface.affichage import afficher_datasets

def main():
    catalogue_data = []

    active = True
    while active:
        afficher_menu()
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
            # Sauvegarde automatique : les CSV vont dans CSV, les JSON vont dans JSON
            sauvegarder_csv(catalogue_data)
            sauvegarder_json(catalogue_data)
        elif choix == "9":
            # Recharge depuis les deux fichiers et combine la liste
            catalogue_data = []
            catalogue_data.extend(recharger_csv())
            catalogue_data.extend(recharger_json())
        elif choix == "10":
            print("Au revoir !")
            active = False
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 10.")


if __name__ == "__main__":
    main()