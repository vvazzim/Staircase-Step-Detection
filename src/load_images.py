import cv2
import pandas as pd
import os

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

# Exemple de chargement de la première image et de son annotation
image_name = annotations_df.iloc[0]['image_name']
image, annotation = load_image_and_annotation(image_name)

# Affichage de l'image et du nombre de marches
cv2.imshow("Image", image)
print(f"Le nombre de marches pour {image_name} est : {annotation}")
cv2.waitKey(0)
cv2.destroyAllWindows()
