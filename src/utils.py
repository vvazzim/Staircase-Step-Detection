import cv2
import os
import pandas as pd

# Chargement des annotations
annotations_path = 'data/annotations/annotations.csv'
annotations_df = pd.read_csv(annotations_path)

# Dossier contenant les images
images_dir = 'data/raw'

# Fonction pour charger les images et obtenir les annotations
def load_image_and_annotation(image_name):
    image_path = os.path.join(images_dir, image_name)
    image = cv2.imread(image_path)
    annotation = annotations_df[annotations_df['image_name'] == image_name]['num_steps'].values[0]
    return image, annotation
