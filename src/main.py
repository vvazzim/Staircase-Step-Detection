import cv2
import os
from src.preprocess_images import canny_with_otsu, sobel_edge_detection  # Importer les méthodes de prétraitement
from src.detect_steps import detect_steps, morphological_filter, filter_small_contours  # Importer la fonction detect_steps et les autres outils
from src.utils import load_image_and_annotation

def main():
    # Dossier contenant les images
    data_directory = os.path.join('data', 'raw')

    for filename in os.listdir(data_directory):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Ajouter d'autres extensions si nécessaire
            image_path = os.path.join(data_directory, filename)
            print(f"Chargement de l'image : {image_path}")

            # Charger l'image et son annotation
            image, annotation = load_image_and_annotation(filename)

            # Appliquer le prétraitement à l'image (Canny ou Sobel, selon le test)
            print(f"Prétraitement de l'image {filename}...")
            preprocessed_image_canny = canny_with_otsu(image)  # Utilisation de Canny avec Otsu
            preprocessed_image_sobel = sobel_edge_detection(image)  # Utilisation de Sobel

            # Afficher l'image prétraitée (avant la détection des contours)
            print(f"Affichage de l'image prétraitée pour Canny et Sobel...")
            cv2.imshow(f"Image Canny Prétraitée - {filename}", preprocessed_image_canny)
            cv2.imshow(f"Image Sobel Prétraitée - {filename}", preprocessed_image_sobel)
            cv2.waitKey(0)  # Attendre une touche avant de passer à l'image suivante

            # Détection des contours pour Canny
            print(f"Résultats Canny - {filename}:")
            contours_canny = detect_steps(preprocessed_image_canny)  # Détection des contours avec Canny
            contours_canny = filter_small_contours(contours_canny)  # Filtrer les petits contours
            contours_canny_image = morphological_filter(contours_canny, image.shape)  # Appliquer le filtre morphologique
            print(f"Nombre de marches détectées : {len(contours_canny)}")

            # Détection des contours pour Sobel
            print(f"Résultats Sobel - {filename}:")
            contours_sobel = detect_steps(preprocessed_image_sobel)  # Détection des contours avec Sobel
            contours_sobel = filter_small_contours(contours_sobel)  # Filtrer les petits contours
            contours_sobel_image = morphological_filter(contours_sobel, image.shape)  # Appliquer le filtre morphologique
            print(f"Nombre de marches détectées : {len(contours_sobel)}")

            # Affichage des résultats pour Canny et Sobel
            image_with_canny_contours = image.copy()
            cv2.drawContours(image_with_canny_contours, contours_canny, -1, (0, 255, 0), 3)
            cv2.imshow(f"Contours Canny - {filename}", image_with_canny_contours)

            image_with_sobel_contours = image.copy()
            cv2.drawContours(image_with_sobel_contours, contours_sobel, -1, (0, 255, 0), 3)
            cv2.imshow(f"Contours Sobel - {filename}", image_with_sobel_contours)

            cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
