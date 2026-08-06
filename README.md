#  DatasetManager

**Application console Python pour la gestion d'un catalogue de datasets (CSV & JSON)**

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Status](https://img.shields.io/badge/status-terminé-brightgreen.svg)
![License](https://img.shields.io/badge/license-Éducatif-lightgrey.svg)

---

##  Contexte

Une entreprise spécialisée en Intelligence Artificielle souhaite disposer d'une application console permettant à ses Data Scientists de gérer un catalogue de datasets (CSV et JSON) avant leur traitement avec Pandas.

**DatasetManager** répond à ce besoin en proposant : enregistrement des caractéristiques d'un dataset, recherche, statistiques, sauvegarde, rechargement automatique et gestion robuste des erreurs.

> Projet réalisé dans le cadre de la **formation en Intelligence Artificielle — Orange Digital Center (ODC) / Sonatel Academy**, Promo I IA — Année 2026.

---

##  Fonctionnalités

| # | Fonctionnalité | Description |
|---|-----------------|--------------|
| 1 |  Ajouter un dataset | Saisie manuelle ou **import automatique** depuis un fichier réel (`.csv` / `.json`) |
| 2 |  Afficher les datasets | Liste résumée du catalogue |
| 3 |  Rechercher un dataset | Recherche par nom |
| 4 |  Trier les datasets | Tri alphabétique par nom |
| 5 |  Supprimer un dataset | Suppression sécurisée d'un élément du catalogue |
| 6 |  Modifier un dataset | Mise à jour d'un attribut, y compris **conversion de format** (CSV ↔ JSON) |
| 7 |  Statistiques | Nombre total de lignes, moyenne de colonnes, répartition par format/domaine, etc. |
| 8 |  Sauvegarder | Export du catalogue vers `datasets.csv` / `datasets.json` |
| 9 |  Recharger | Restauration du catalogue depuis les fichiers de stockage |
| 10 | Quitter | Fermeture propre de l'application |

###  Fonctionnalités bonus

- **Profilage automatique (Auto-Discovery)** : détection automatique de la taille, du nombre de lignes/colonnes et du format d'un fichier réel via `profiler.py`.
- **Transcodeur CSV ↔ JSON** : conversion dynamique du format d'un dataset avec dispatching automatique lors de la sauvegarde.

---

##  Architecture du projet

Le projet suit une architecture modulaire en **packages Python**, respectant le principe de séparation des responsabilités :

```
datasetManager/
│
├── main.py                  # Point d'entrée de l'application
│
├── data/                     # Fichiers de données persistées
│   ├── datasets.csv
│   └── datasets.json
│
├── datasets/                 # Logique métier & analyse
│   ├── __init__.py
│   ├── gestion.py            # CRUD, tri, sauvegarde, rechargement, conversion
│   ├── statistiques.py       # Calculs et rapports statistiques
│   └── profiler.py           # Profilage automatique de fichiers (bonus)
│
├── interface/                 # Couche présentation
│   ├── __init__.py
│   ├── menu.py                # Affichage du menu interactif
│   └── affichage.py           # Mise en forme de l'affichage
│
└── stockage/                  # Persistance des données
    ├── __init__.py
    ├── csv_manager.py         # Lecture/écriture CSV
    └── json_manager.py        # Lecture/écriture JSON
```

| Module | Rôle | Fonctions principales |
|--------|------|------------------------|
| `main.py` | Point d'entrée, orchestration | `main()` |
| `interface/menu.py` | Affichage du menu | `afficher_menu()` |
| `datasets/gestion.py` | Logique métier, CRUD, persistance | `ajouter_dataset()`, `afficher_datasets()`, `rechercher_dataset()`, `modifier_dataset()`, `supprimer_dataset()`, `trier_dataset()`, `sauvegarder()`, `recharger()`, `convertir_format_dataset()` |
| `datasets/statistiques.py` | Calculs d'agrégation | `statistiques()` |
| `datasets/profiler.py` | Profilage automatique de fichiers | `analyser_fichier_reel()` |

---

##  Prérequis

- **Python 3.10+** (testé avec Python 3.13)
- Aucune dépendance externe : le projet repose uniquement sur les modules natifs (`csv`, `json`, `os`)

---

##  Installation & exécution

```bash
# 1. Cloner ou télécharger le projet
git clone <url-du-repo>
cd datasetManager

# 2. Lancer l'application
python main.py
```

Au lancement, un menu interactif s'affiche et reste actif jusqu'au choix de l'option **Quitter** :

```
===== Menu =====
1. Ajouter un dataset
2. Afficher les datasets
3. Rechercher un dataset
4. Trier les datasets
5. Supprimer un dataset
6. Modifier un dataset
7. Voir les statistiques des datasets
8. Sauvegarder les datasets dans un fichier CSV
9. Recharger les datasets depuis un fichier CSV
10. Quitter
```

---

##  Gestion des erreurs

L'application a été conçue pour ne jamais s'arrêter brutalement :

- **Saisie invalide** (texte au lieu d'un nombre) → interception via `ValueError`
- **Fichier manquant** lors du rechargement → interception via `FileNotFoundError`
- **Fichier vide** → vérification avant traitement
- **Dataset ou attribut introuvable** → vérification défensive avant toute opération

---

##  Concepts Python mis en œuvre

Ce projet a permis de couvrir progressivement l'ensemble des fondamentaux du langage :

`Types de base & E/S` · `Structures de contrôle` · `Dictionnaires` · `Tuples` · `Listes & CRUD` · `Compréhensions` · `Fichiers (CSV)` · `Exceptions` · `Fonctions & docstrings` · `Modules` · `Packages`

---

##  Auteur

**Mr. Abdoulaye Diouf**
Apprenant — Formation IA, Orange Digital Center / Sonatel Academy (Promo I IA — 2026)

**Formateur :** Prof. Amadou Dieng

---

##  Licence

Projet réalisé à des fins pédagogiques dans le cadre de la formation IA de l'Orange Digital Center / Sonatel Academy.