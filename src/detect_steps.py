import cv2
import numpy as np

def detect_steps(image):
    # Vérifier si l'image a 3 canaux (en couleur)
    if len(image.shape) == 3:
        # Convertir en niveaux de gris si l'image est en couleur
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        # Si l'image est déjà en niveaux de gris, l'utiliser telle quelle
        gray_image = image
    
    # S'assurer que l'image est du type uint8
    gray_image = np.uint8(gray_image)

    # Appliquer l'algorithme de détection des contours (Canny)
    edges = cv2.Canny(gray_image, 50, 150)
    
    # Trouver les contours à partir de l'image en niveaux de gris
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours
