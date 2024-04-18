from PIL import Image
import random

def encrypt_image(input_image, output_image):
    # Load the input image
    image = Image.open(input_image)
    pixels = image.load()
    width, height = image.size

    # Create a list of pixel coordinates
    pixel_list = list(pixels)
    random.shuffle(pixel_list)

    # Swap pixel values
    for i in range(len(pixel_list)):
        x1, y1 = pixel_list[i]
        x2, y2 = pixel_list[(i + 1) % len(pixel_list)]
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

    # Save the encrypted image
    image.save(output_image)

def decrypt_image(input_image, output_image):
    # Encryption and decryption are the same process
    encrypt_image(input_image, output_image)

def main():
    mode = input("Enter 'encrypt' or 'decrypt': ").lower()
    input_image = input("Enter the input image file path: ")
    output_image = input("Enter the output image file path: ")

    if mode == "encrypt":
        encrypt_image(input_image, output_image)
    elif mode == "decrypt":
        decrypt_image(input_image, output_image)
    else:
        print("Invalid mode selected. Please try again.")

if __name__ == "__main__":
    main()