# src/preprocess_images.py

import cv2
import numpy as np

def otsu_thresholding(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convertir l'image en niveaux de gris
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Appliquer un flou pour réduire le bruit
    _, thresholded_image = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Seuillage Otsu
    return thresholded_image

def sobel_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convertir en niveaux de gris
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Détection des bords dans la direction X
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Détection des bords dans la direction Y
    magnitude = cv2.magnitude(grad_x, grad_y)  # Calcul de la magnitude des gradients
    return magnitude

# Fonction pour appliquer un seuillage Otsu
def canny_with_preprocessing(image, low_threshold=50, high_threshold=150):
    # Convertir en niveaux de gris
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou pour réduire le bruit
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Appliquer l'algorithme de Canny avec des seuils ajustés
    edges = cv2.Canny(blurred_image, low_threshold, high_threshold)

    return edges


# Fonction pour isoler les marches en fonction de la couleur (exemple pour les couleurs claires)
def isolate_stairs(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_color = np.array([0, 0, 200])  # Plage pour les couleurs claires
    upper_color = np.array([180, 255, 255])  # Plage de couleur maximale
    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

# Fonction pour appliquer le Canny avec un seuil
def canny_with_preprocessing(image, low_threshold=50, high_threshold=150):
    # Convertir en niveaux de gris
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou pour réduire le bruit
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Appliquer l'algorithme de Canny avec des seuils ajustés
    edges = cv2.Canny(blurred_image, low_threshold, high_threshold)

    return edges


# Fonction de filtrage morphologique (érosion + dilatation)
def morphological_filter(image):
    kernel = np.ones((5,5), np.uint8)
    image_eroded = cv2.erode(image, kernel, iterations=1)
    image_dilated = cv2.dilate(image_eroded, kernel, iterations=1)
    return image_dilated

# Fonction de prétraitement pour l'image (c'est-à-dire, appliquer tout le prétraitement dans un ordre donné)
def preprocess_image(image, threshold=50):
    # Appliquer les différentes étapes de prétraitement
    image_otsu = otsu_thresholding(image)  # Appliquer Otsu
    image_isolated = isolate_stairs(image)  # Isoler les marches
    edges = canny_with_preprocessing(image)  # Appliquer Canny
    edges_filtered = morphological_filter(edges)  # Appliquer le filtre morphologique
    
    # Retourner l'image prétraitée (ici, nous retournons les contours filtrés pour la détection des marches)
    return edges_filtered
def canny_with_otsu(image):
    thresholded_image = otsu_thresholding(image)  # Appliquer Otsu pour le seuillage
    edges = cv2.Canny(thresholded_image, 50, 150)  # Appliquer Canny sur l'image seuillée
    return edges
def sobel_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = cv2.magnitude(grad_x, grad_y)
    return magnitude
