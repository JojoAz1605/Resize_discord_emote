from PIL import Image
import glob
import os


# Petites vérifications pour éviter que le programme plante
if not os.path.isdir("input"):  # Vérifie si input existe
    print("Le dossier 'input' n'existe pas, création...")
    os.mkdir("input/")
    print("Veuillez maintenant mettre vos images à redimensionner dans 'input/' et redémarrer ce programme.")
    exit()
elif len(os.listdir('input/')) == 0:  # Vérifie si input est vide
    print("Dossier 'input/' vide, veuillez mettre des images dedans pour commencer. Une fois fait, redémarrez ce programme.")
    exit()

if not os.path.isdir("output"):  # Vérifie si output existe
    print("Le dossier 'output' n'existe pas, création...")
    os.mkdir("output/")

max_file_size = 256 * 1000  # C'est en octets

# fait la liste des images dans input
list_images = glob.glob("input/*.png")
list_images += glob.glob("input/*.jpg")
list_images += glob.glob("input/*.jpeg")

nb_image = len(list_images)  # prend le nombre d'images que contient le dossier input

for image in list_images:  # pour chaque image dans la liste
    default_size = [600, 600]  # la première taille testée par le programme

    img = Image.open(image)  # on ouvre l'image
    img_name = image.replace("input\\", '')  # on prend son nom
    img.thumbnail(tuple(default_size))  # on la redimensionne
    img.save(f"output\\{img_name}", optimize=True, quality=100)  # on la sauvegarde

    while os.path.getsize(f"output\\{img_name}") > max_file_size:  # tant que la taille de l'image générée est supérieure à 256ko
        print(f"{list_images.index(image)}/{nb_image} | {img_name} - On essaye avec {default_size}")

        # on décrémente de 5 pixels en x et en y(image carrée)
        default_size[0] -= 5
        default_size[1] -= 5

        img.thumbnail(tuple(default_size))  # on redimensionne encore une fois l'image
        img.save(f"output\\{img_name}", optimize=True, quality=100)  # on la sauvegarde
        out_size = os.path.getsize(f"output\\{img_name}")  # on prend la taille de l'image générée
        print("La taille est de", out_size, "octets, soit", out_size - max_file_size, "octets en trop", end='\n\n')

print("C'est bon!")
