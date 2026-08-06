# datasets/profiler.py
import os
import csv
import json

# Fonction pour analyser un fichier réel (.csv ou .json) et calculer ses métadonnées
def analyser_fichier_reel(chemin_fichier):
    # Vérification de l'existence du fichier
    if not os.path.exists(chemin_fichier):
        print(f"Erreur : Le fichier '{chemin_fichier}' n'existe pas.")
        return None

    # 1. Calcul de la taille en Mo
    taille_octets = os.path.getsize(chemin_fichier)
    taille_mo = round(taille_octets / (1024 * 1024), 4)
    # Si le fichier est très petit, on s'assure d'avoir au moins une valeur lisible
    if taille_mo == 0:
        taille_mo = round(taille_octets / 1024, 2)

    # 2. Détection du format et calcul automatique des lignes et colonnes
    extension = os.path.splitext(chemin_fichier)[1].lower()
    nbr_lignes = 0
    nbr_colonnes = 0
    fmt = "INCONNU"

    try:
        if extension == ".csv":
            fmt = "CSV"
            with open(chemin_fichier, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, None)
                if header:
                    nbr_colonnes = len(header)
                nbr_lignes = sum(1 for _ in reader)

        elif extension == ".json":
            fmt = "JSON"
            with open(chemin_fichier, mode='r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    nbr_lignes = len(data)
                    if nbr_lignes > 0 and isinstance(data[0], dict):
                        nbr_colonnes = len(data[0].keys())

        return {
            "taille": taille_mo,
            "nbr_lignes": nbr_lignes,
            "nbr_colonnes": nbr_colonnes,
            "format": fmt
        }
    except Exception as e:
        print(f"Erreur lors du profilage du fichier : {e}")
        return None