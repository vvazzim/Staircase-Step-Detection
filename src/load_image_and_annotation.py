from src.utils import load_image_and_annotation
import cv2

# Exemple de chargement de la première image et de son annotation
image_name = 'Groupe1_Image1.jpg'  # Remplacer par l'image que tu veux tester
image, annotation = load_image_and_annotation(image_name)

# Affichage de l'image et du nombre de marches
cv2.imshow("Image", image)
print(f"Le nombre de marches pour {image_name} est : {annotation}")
cv2.waitKey(0)
cv2.destroyAllWindows()
