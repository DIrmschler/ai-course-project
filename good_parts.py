from PIL import Image, ImageDraw
import random
import os

# Ordner für die Bilder erstellen, falls nicht vorhanden
output_folder = "random_images"
os.makedirs(output_folder, exist_ok=True)

# Bildgröße und Hintergrundfarbe
width, height = 800, 800
background_color = (190, 190, 190)  # schwarz

# Anzahl der einzelnen Pixel und Pixelhaufen
num_single_pixels = 120  # Anzahl einzelner weißer Pixel
num_pixel_clusters = 40  # Anzahl der Pixelhaufen

# Generiere 100 Bilder
for i in range(100):
    # Bild erstellen
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Einzelne weiße Pixel zufällig platzieren
    for _ in range(num_single_pixels):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=(255, 255, 255))  # weißer Pixel

    # Weiße Pixelhaufen zufällig platzieren
    for _ in range(num_pixel_clusters):
        # Zentrum des Pixelhaufens
        center_x = random.randint(0, width - 1)
        center_y = random.randint(0, height - 1)

        # Bestimme Größe des Clusters
        cluster_size = random.randint(25, 55)  # Anzahl der Pixel im Cluster

        for _ in range(cluster_size):
            # Zufällige Position im Umkreis des Zentrums
            offset_x = random.randint(-5, 5)
            offset_y = random.randint(-5, 5)
            pixel_x = center_x + offset_x
            pixel_y = center_y + offset_y

            # Sicherstellen, dass die Pixel innerhalb des Bildes liegen
            if 0 <= pixel_x < width and 0 <= pixel_y < height:
                draw.point((pixel_x, pixel_y), fill=(255, 255, 255))  # weißer Pixel im Cluster

    # Bild speichern
    file_name = f"random_image_{i+1:03d}.png"  # z. B. random_image_001.png
    image_path = os.path.join(output_folder, file_name)
    image.save(image_path)

print(f"100 Bilder wurden im Ordner '{output_folder}' gespeichert.")

for _ in range(cluster_size):
        # Zufällige Position im Umkreis des Zentrums
        offset_x = random.randint(-5, 5)
        offset_y = random.randint(-5, 5)
        pixel_x = center_x + offset_x
        pixel_y = center_y + offset_y

        # Sicherstellen, dass die Pixel innerhalb des Bildes liegen
        if 0 <= pixel_x < width and 0 <= pixel_y < height:
            draw.point((pixel_x, pixel_y), fill=(255, 255, 255))  # weißer Pixel im Cluster

# Bild speichern und anzeigen
image.save("random_pixels_and_clusters.png")
image.show()
