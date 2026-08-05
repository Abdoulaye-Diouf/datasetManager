from menu import afficher_menu
from gestion import(ajouter_dataset,
                    afficher_datasets,
                    rechercher_dataset,
                    trier_dataset,
                    supprimer_dataset,
                    modifier_dataset,
                    statistiques,
                    sauvegarder,
                    recharger)
from statistiques import statistiques


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