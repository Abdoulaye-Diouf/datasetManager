# csv_manager.py
import csv

chemin_csv = r"C:\ODC\veille-python\pratique\code\datasetManager\data\datasets.csv"

# Fonction sauvegarder les datasets CSV dans un fichier CSV
def sauvegarder_csv(catalogue_data, chemin=chemin_csv):
    # Filtre et sauvegarde uniquement les datasets au format CSV
    datasets_csv = [d for d in catalogue_data if str(d.get("format")).lower() == "csv"]
    if not datasets_csv:
        print("Aucun dataset CSV à sauvegarder.")
        return
    
    try:
        with open(chemin, mode='w', newline='', encoding='utf-8') as f_csv:
            champs = datasets_csv[0].keys()
            writer = csv.DictWriter(f_csv, fieldnames=champs)
            writer.writeheader()
            writer.writerows(datasets_csv)
        print(f" Success : {len(datasets_csv)} dataset(s) CSV enregistrés dans '{chemin}'.")
    except OSError as e:
        print(f"Erreur d'écriture CSV : {e}")

# Fonction recharger les datasets depuis un fichier CSV
def recharger_csv(chemin=chemin_csv):
    # Recharge le catalogue de datasets depuis le fichier CSV et le retourne.
    catalogue_data = []
    # --- Gestion des exceptions : fichier inexistant / fichier vide ---
    try:
        with open(chemin, mode='r', newline='', encoding='utf-8') as f_csv:
            reader = csv.DictReader(f_csv)
            for row in reader:
                d = dict(row)
                d["nbr_lignes"] = int(d["nbr_lignes"])
                d["nbr_colonnes"] = int(d["nbr_colonnes"])
                d["taille"] = float(d["taille"])
                catalogue_data.append(d)
        print(f" Success : {len(catalogue_data)} dataset(s) CSV rechargé(s).")
    except FileNotFoundError:
        print(f" Note : Le fichier CSV '{chemin}' n'existe pas encore.")
    except OSError as e:
        print(f"Erreur de lecture CSV : {e}")

    return catalogue_data