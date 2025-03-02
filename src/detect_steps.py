import cv2
import numpy as np

def morphological_filter(contours, image_shape):
    # Créer une image noire de la même taille que l'image d'entrée
    filtered_image = np.zeros(image_shape, dtype=np.uint8)

    # Dessiner les contours sur l'image noire (les rendre blancs)
    cv2.drawContours(filtered_image, contours, -1, (255), thickness=cv2.FILLED)

    # Appliquer un noyau pour éroder l'image (réduire les petits contours)
    kernel = np.ones((5, 5), np.uint8)
    image_eroded = cv2.erode(filtered_image, kernel, iterations=1)
    
    # Appliquer une dilatation pour renforcer les contours importants
    image_dilated = cv2.dilate(image_eroded, kernel, iterations=1)

    return image_dilated



def filter_small_contours(contours, min_area=100):
    # Garder uniquement les contours dont la superficie est supérieure à min_area
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
    return filtered_contours



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
