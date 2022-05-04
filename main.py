from PIL import Image
import glob
import os


max_file_size = 256 * 1000
list_images = glob.glob("input/*.png")
nb_image = len(list_images)

for image in list_images:
    default_size = [600, 600]

    img = Image.open(image)
    img_name = image.replace("input\\", '')
    img.thumbnail(tuple(default_size))
    img.save(f"output\\{img_name}", optimize=True, quality=100)

    while os.path.getsize(f"output\\{img_name}") > max_file_size:
        print(f"{list_images.index(image)}/{nb_image} | {img_name} - On essaye avec {default_size}")
        default_size[0] -= 5
        default_size[1] -= 5
        img.thumbnail(tuple(default_size))
        out_size = os.path.getsize(f"output\\{img_name}")
        img.save(f"output\\{img_name}", optimize=True, quality=100)
        print("La taille est de", out_size, "octets, soit", out_size - max_file_size, "octets en trop", end='\n\n')

print("C'est bon!")