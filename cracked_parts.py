import os
from PIL import Image, ImageDraw
import random

# Bildgröße und Hintergrundfarbe
width, height = 800, 800
background_color = (190, 190, 190)  # schwarz

# Ordner für die Bilder
output_folder = "generated_images"
os.makedirs(output_folder, exist_ok=True)  # Ordner erstellen, falls nicht vorhanden

# Funktion zur Erstellung eines Bildes
def create_image(filename):
    # Bild erstellen
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Anzahl der einzelnen Pixel und Pixelhaufen
    num_single_pixels = 120  # Anzahl einzelner weißer Pixel
    num_pixel_clusters = 40  # Anzahl der Pixelhaufen

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

    # Risse erzeugen
    num_cracks = random.randint(1, 2)  # Anzahl der Risse
    for _ in range(num_cracks):
        # Zufällige Startposition für jeden Riss
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        main_direction = random.choice([-1, 1])  # Links oder rechts

        # Länge und Dicke des Risses
        num_points = random.randint(10, 60)  # Anzahl der Punkte im Riss
        line_thickness = 2  # Dicke der Risslinie
        crack_color = (255, 255, 255)  # weiß

        for _ in range(num_points):
            # Zufällige Schritte in X- und Y-Richtung
            dx = main_direction * random.randint(5, 15)
            dy = random.randint(-10, 10)

            # Nächster Punkt des Risses
            next_x = x + dx
            next_y = y + dy

            # Zeichne den Riss
            if 0 <= next_x < width and 0 <= next_y < height:
                draw.line([(x, y), (next_x, next_y)], fill=crack_color, width=line_thickness)

            # Gelegentliche Verzweigungen
            if random.random() < 0.3:
                branch_length = random.randint(10, 40)
                branch_thickness = max(1, line_thickness - 1)
                branch_direction = random.choice([-1, 1])
                branch_end_x = next_x + branch_direction * branch_length
                branch_end_y = next_y + random.randint(-10, 10)
                
                if 0 <= branch_end_x < width and 0 <= branch_end_y < height:
                    draw.line([(next_x, next_y), (branch_end_x, branch_end_y)], fill=crack_color, width=branch_thickness)

            # Update Startpunkt
            x, y = next_x, next_y

    # Bild speichern
    image.save(filename)

# 10 Bilder erstellen und speichern
for i in range(1, 11):
    filename = os.path.join(output_folder, f"image_{i}.png")
    create_image(filename)
    print(f"{filename} wurde erstellt.")
