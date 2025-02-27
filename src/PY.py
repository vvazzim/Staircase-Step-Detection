import cv2
import os

image_path = os.path.abspath(os.path.join('data', 'Groupe1_Image1.jpg'))

print(f"Chemin absolu de l'image : {image_path}")
# Load and print all images in the data directory
data_directory = os.path.join('data')
for filename in os.listdir(data_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Add more extensions if needed
        image_path = os.path.abspath(os.path.join(data_directory, filename))
        print(f"Chemin absolu de l'image : {image_path}")
        image = cv2.imread(image_path)
        if image is not None:
            print(image.shape)
        else:
            print(f"Erreur de lecture de l'image : {filename}")


if image is not None:
    print(image.shape)
else:
    print("Erreur de lecture de l'image.")
