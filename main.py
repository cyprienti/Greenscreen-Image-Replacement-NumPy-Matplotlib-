import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Du kannst dies zu 'Agg' ändern, wenn du keine GUI brauchst
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Lade das Bild mit der Person vor dem Greenscreen
    original = plt.imread('person_on_greenscreen.jpg')
    original_npa = np.array(original)
    og_shape = original_npa.shape

    # Lade den Wald-Hintergrund und passe die Größe an
    background = plt.imread('forest.jpg')
    background_npa = np.array(background)[:og_shape[0], :og_shape[1], :og_shape[2]]

    # Erstelle eine Maske für "nicht-grüne" Pixel (also die Person)
    mask = ~((original_npa[:, :, 1] > 100) &  # grüner Kanal stark
             (original_npa[:, :, 1] > original_npa[:, :, 0] * 1.2) &  # mehr als rot
             (original_npa[:, :, 1] > original_npa[:, :, 2] * 1.2))   # mehr als blau

    # Erstelle Bild mit schwarzem Hintergrund (nur Person sichtbar)
    selected_pixels_image = np.zeros_like(original_npa)
    selected_pixels_image[mask] = original_npa[mask]

    # Kombiniere mit Hintergrund
    combined_image = background_npa.copy()
    combined_image[mask] = original_npa[mask]

    # Zeige alle drei Bilder und speichere das Ergebnis
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(original_npa)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Selected Pixels")
    plt.imshow(selected_pixels_image)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("Combined Image")
    plt.imshow(combined_image)
    plt.axis('off')

    plt.tight_layout()
    plt.savefig("person_in_forest.png")
    plt.show()