import cv2
import numpy as np
import os
import pandas as pd

# Chargement des annotations
annotations_path = 'data/annotations/annotations.csv'
annotations_df = pd.read_csv(annotations_path)

# Dossier contenant les images
images_dir = 'data/raw'

# Fonction pour charger les images et obtenir les annotations
def load_image_and_annotation(image_name):
    # Charger l'image
    image_path = os.path.join(images_dir, image_name)
    image = cv2.imread(image_path)

    # Récupérer l'annotation correspondante
    annotation = annotations_df[annotations_df['image_name'] == image_name]['num_steps'].values[0]
    
    return image, annotation

# Fonction de prétraitement
def preprocess_image(image):
    # Redimensionner l'image
    resized_image = cv2.resize(image, (800, 600))  # Dimension choisie, ajuste si nécessaire
    
    # Convertir en niveaux de gris
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    
    # Égaliser l'histogramme pour améliorer le contraste
    equalized_image = cv2.equalizeHist(gray_image)
    
    # Appliquer un flou gaussien pour réduire le bruit
    blurred_image = cv2.GaussianBlur(equalized_image, (5, 5), 0)
    
    return blurred_image

# Traiter toutes les images
for _, row in annotations_df.iterrows():
    image_name = row['image_name']
    image, annotation = load_image_and_annotation(image_name)

    # Appliquer le prétraitement
    preprocessed_image = preprocess_image(image)

    # Affichage de l'image traitée
    cv2.imshow(f"Preprocessed Image - {image_name}", preprocessed_image)
    print(f"Le nombre de marches pour {image_name} est : {annotation}")
    
    # Attendre la touche pour passer à l'image suivante
    cv2.waitKey(0)

cv2.destroyAllWindows()
