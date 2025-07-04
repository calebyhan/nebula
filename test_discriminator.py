import tensorflow as tf
import numpy as np
import sys
import os
from PIL import Image
import matplotlib.pyplot as plt

size = 128

MODEL_PATH = f"{size}/discriminator.keras"

def preprocess_image(image_path, target_size=(size,size)):
    img = Image.open(image_path).convert('RGB')
    img = img.resize(target_size)
    img_array = np.array(img).astype(np.float32)
    img_array = (img_array / 127.5) - 1.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def main(image_path):
    if not os.path.exists(MODEL_PATH):
        print(f"Discriminator model not found at {MODEL_PATH}")
        return

    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
        return

    discriminator = tf.keras.models.load_model(MODEL_PATH, compile=False)
    print("Discriminator model loaded.")

    img = preprocess_image(image_path)

    pred = discriminator(img, training=False)
    score = tf.reduce_mean(pred).numpy()
    print(f"Discriminator output score for image: {score}")

    plt.imshow((img[0] + 1) / 2)
    plt.title(f"Discriminator Score: {score:.4f}")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_discriminator.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    main(image_path)
