from PIL import Image
import numpy as np
from sklearn.ensemble import IsolationForest
import os

# Pfad zu den "in Ordnung"-Bildern und zu den zu überprüfenden Bildern
normal_images_folder = "random_images"
generated_images_folder = "generated_images"

# Funktion zur Extraktion von Merkmalen (z. B. Anzahl der weißen Pixel)
def extract_features(image):
    image = image.convert("L")  # In Graustufen umwandeln
    np_image = np.array(image)
    # Anzahl der weißen Pixel als Merkmal (Pixelwert > 200 zählt als "weiß")
    white_pixel_count = np.sum(np_image > 200)
    return [white_pixel_count]

# Lade die "in Ordnung"-Bilder und extrahiere deren Merkmale
normal_features = []
for filename in os.listdir(normal_images_folder):
    if filename.endswith(".png"):
        image_path = os.path.join(normal_images_folder, filename)
        image = Image.open(image_path)
        features = extract_features(image)
        normal_features.append(features)

# Trainiere das Anomalie-Erkennungsmodell
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(normal_features)

# Statistik-Variablen
total_images = 0
anomalous_images = 0
normal_images = 0

# Überprüfe die Bilder im Ordner "generated_images"
for filename in os.listdir(generated_images_folder):
    if filename.endswith(".png"):
        total_images += 1
        image_path = os.path.join(generated_images_folder, filename)
        image = Image.open(image_path)
        features = extract_features(image)

        # Anomalie-Erkennung durchführen
        prediction = model.predict([features])

        if prediction[0] == -1:
            anomalous_images += 1
            print(f"{filename}: Anomalie erkannt (Riss).")
        else:
            normal_images += 1
            print(f"{filename}: Kein Riss erkannt (in Ordnung).")

# Statistik ausgeben
print("\n--- Statistik ---")
print(f"Gesamtanzahl überprüfter Bilder: {total_images}")
print(f"Anzahl Bilder mit Rissen: {anomalous_images}")
print(f"Anzahl Bilder ohne Risse: {normal_images}")
