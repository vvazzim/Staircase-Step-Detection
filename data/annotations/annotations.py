import csv
import os

# Créer le répertoire 'annotations' s'il n'existe pas
annotations_dir = 'data/annotations'
os.makedirs(annotations_dir, exist_ok=True)

# Liste des annotations
annotations = [
    {"image_name": "Groupe1_Image1.jpg", "num_steps": 10},
    {"image_name": "Groupe1_Image2.jpg", "num_steps": 8},
    {"image_name": "Groupe1_Image3.jpg", "num_steps": 12},
    {"image_name": "Groupe1_Image4.jpg", "num_steps": 12},
    {"image_name": "Groupe1_Image5.jpg", "num_steps": 12},
    {"image_name": "Groupe1_Image6.jpg", "num_steps": 6},
    {"image_name": "Groupe1_Image7.jpg", "num_steps": 6},
    {"image_name": "Groupe1_Image8.jpg", "num_steps": 18},
    {"image_name": "Groupe1_Image9.jpg", "num_steps": 9},
    {"image_name": "Groupe1_Image10.jpg", "num_steps": 15},
]

# Créer et écrire dans le fichier CSV
csv_filename = os.path.join(annotations_dir, 'annotations.csv')
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['image_name', 'num_steps']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for annotation in annotations:
        writer.writerow(annotation)

print(f"Le fichier CSV a été créé et enregistré à l'emplacement suivant : {csv_filename}")
