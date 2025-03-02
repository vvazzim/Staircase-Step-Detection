from src.utils import load_image_and_annotation
from src.detect_steps import detect_steps



from sklearn.metrics import mean_absolute_error
import cv2

import pandas as pd

def evaluate_detection():
    # Load annotations
    annotations_path = 'data/annotations/annotations.csv'
    annotations_df = pd.read_csv(annotations_path)
    
    errors = []
    for _, row in annotations_df.iterrows():

        image_name = row['image_name']
        image, annotation = load_image_and_annotation(image_name)
        
        contours = detect_steps(image)
        detected_steps = len(contours)
        
        error = mean_absolute_error([annotation], [detected_steps])
        errors.append(error)

        print(f"Image : {image_name}")
        print(f"Nombre de marches attendu : {annotation}")
        print(f"Nombre de marches détectées : {detected_steps}")

        # Affichage des résultats
        image_with_contours = image.copy()
        cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 3)
        cv2.imshow(f"Contours - {image_name}", image_with_contours)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
    
    avg_error = sum(errors) / len(errors)
    print(f"Erreur absolue moyenne : {avg_error}")
