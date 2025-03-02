# Staircase Step Detection

## Description
Ce projet consiste à détecter et compter le nombre de marches dans des images d'escaliers en utilisant des techniques de vision par ordinateur, principalement avec la bibliothèque OpenCV. L'objectif est de créer un système automatisé capable de détecter les marches dans une image capturée par un téléphone et de compter leur nombre.

## Fonctionnalités
- Chargement des images à partir d'un répertoire.
- Prétraitement des images pour les rendre adaptées à la détection.
- Détection des bords à l'aide de l'algorithme Canny.
- Détection et comptage des marches dans les images.
- Évaluation des performances en comparant les résultats de détection avec les annotations réelles.

## Installation

### Prérequis
- Python 3.x
- OpenCV
- Pandas
- NumPy
- scikit-learn (pour l'évaluation)

### Étapes d'installation
1. Clonez ce repository :
   ```bash
   git clone https://github.com/ton_nom_utilisateur/staircase-step-detection.git
   cd staircase-step-detection
2. Créez un environnement virtuel et activez-le :
    python -m venv venv
    source venv/bin/activate  # Pour Linux/Mac
    venv\Scripts\activate     # Pour Windows
3. Installez les dépendances :
    pip install -r requirements.txt
### Dépendances
    opencv-python : Pour la manipulation d'images et la détection des bords.
    pandas : Pour la gestion des annotations (CSV).
    numpy : Pour les calculs numériques.
    scikit-learn : Pour l'évaluation de la détection avec l'erreur absolue.
### Utilisation
    Chargement des images et des annotations : Le projet charge les images depuis le répertoire data/raw et les annotations depuis le fichier data/annotations/annotations.csv.

    Prétraitement des images : Le prétraitement des images inclut le redimensionnement, la conversion en niveaux de gris, l'égalisation de l'histogramme et l'application d'un flou gaussien.

    Détection des marches : Le système utilise l'algorithme Canny pour détecter les bords, puis les contours sont extraits pour compter les marches présentes dans l'image.

    Évaluation des performances : Le nombre de marches détectées est comparé avec les annotations réelles pour calculer l'erreur absolue moyenne.
### Exécution
    Pour traiter toutes les images et voir les résultats de la détection, exécutez simplement le script de détection :
    python src/evaluate_detection.py
    Cela va :

    1. Charger chaque image.
    2. Appliquer le prétraitement.
    3. Détecter les marches et les afficher.
    4. Comparer le nombre de marches détectées avec les annotations et calculer l'erreur.
### Structure du projet
    Escalier_Project/
    ├── src/                      # Code source principal
    │   ├── load_images.py        # Chargement des images et des annotations
    │   ├── preprocess_images.py  # Prétraitement des images
    │   ├── detect_steps.py       # Détection des marches (Canny, contours)
    │   └── evaluate_detection.py # Affichage des résultats et évaluation
    ├── data/
    │   ├── raw/                  # Dossier contenant les images brutes
    │   ├── processed/            # Dossier pour les images traitées
    │   └── annotations/          # Dossier pour le fichier annotations.csv
    │       └── annotations.csv   # Fichier des annotations
    ├── README.md                 # Documentation du projet
    ├── requirements.txt          # Liste des dépendances
    └── .gitignore                # Fichiers à ignorer par Git
### Auteurs
    WASSIM

### Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails. """

Sauvegarde du contenu dans un fichier README.md
readme_path = '/mnt/data/README.md' with open(readme_path, 'w') as readme_file: readme_f
