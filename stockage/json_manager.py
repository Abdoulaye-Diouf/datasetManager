# json_manager.py
import json

chemin_json = r"C:\ODC\veille-python\pratique\code\datasetManager\data\datasets.json"

# Fonction sauvegarder les datasets JSON dans un fichier JSON
def sauvegarder_json(catalogue_data, chemin=chemin_json):
    # Filtre et sauvegarde uniquement les datasets au format JSON
    datasets_json = [d for d in catalogue_data if str(d.get("format")).lower() == "json"]
    if not datasets_json:
        print("Aucun dataset JSON à sauvegarder.")
        return

    try:
        with open(chemin, mode='w', encoding='utf-8') as f_json:
            json.dump(datasets_json, f_json, indent=4, ensure_ascii=False)
        print(f" Success : {len(datasets_json)} dataset(s) JSON enregistrés dans '{chemin}'.")
    except OSError as e:
        print(f"Erreur d'écriture JSON : {e}")

# Fonction recharger les datasets depuis un fichier JSON
def recharger_json(chemin=chemin_json):
    # Recharge le catalogue de datasets depuis le fichier JSON et le retourne.
    datasets = []
    # --- Gestion des exceptions : fichier inexistant / fichier vide ---
    try:
        with open(chemin, mode='r', encoding='utf-8') as f_json:
            datasets = json.load(f_json)
        print(f" Success : {len(datasets)} dataset(s) JSON rechargé(s).")
    except FileNotFoundError:
        print(f" Note : Le fichier JSON '{chemin}' n'existe pas encore.")
    except (OSError, json.JSONDecodeError) as e:
        print(f"Erreur de lecture JSON : {e}")

    return datasets