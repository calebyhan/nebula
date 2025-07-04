import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os

MODEL_PATH = "256/generator.keras"

# Load the generator model
model = tf.keras.models.load_model(MODEL_PATH, compile=False)
print("Generator model loaded.")

def generate_image(seed):
    tf.random.set_seed(seed)
    noise = tf.random.normal([1, 100])
    generated_image = model(noise, training=False)
    generated_image = (generated_image[0] + 1) / 2.0
    return generated_image.numpy()

def generate_grid(seed_start=0, grid_size=5):
    fig, axs = plt.subplots(grid_size, grid_size, figsize=(10, 10))
    plt.subplots_adjust(wspace=0.05, hspace=0.05)

    for i in range(grid_size):
        for j in range(grid_size):
            seed = seed_start + i * grid_size + j
            image = generate_image(seed)
            axs[i, j].imshow(image)
            axs[i, j].axis('off')

    plt.suptitle(f"{grid_size}x{grid_size} Image Grid from Seeds {seed_start}–{seed_start + grid_size**2 - 1}")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generate_grid(seed_start=42, grid_size=5)
