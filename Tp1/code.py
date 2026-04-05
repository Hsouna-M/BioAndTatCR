from PIL import Image, ImageEnhance, ImageFilter, ImageOps
from matplotlib.gridspec import GridSpecFromSubplotSpec
import matplotlib.pyplot as plt


def part1():
    with Image.open("image.jpg") as img:
        plt.figure()
        plt.subplot(1, 1, 1)
        plt.title("Original")
        plt.axis("off")

        plt.imshow(img)

        img.save("Results/image_originale.png")
        plt.show()


def part2():
    with Image.open("image.jpg") as img:
        resized_img = img.resize((300, 150))

        plt.figure()

        plt.subplot(1, 2, 1)
        plt.imshow(img)
        plt.title("Original")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(resized_img)
        plt.title("Resized")
        plt.axis("off")

        resized_img.save("Results/resized_image.jpg")
        plt.show()


def part3():
    with Image.open("image.jpg") as img:
        enhancer = ImageEnhance.Brightness(img)

        bright_img = enhancer.enhance(1.5)
        plt.figure()

        plt.subplot(1, 2, 1)
        plt.imshow(img)
        plt.title("Original")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(bright_img)
        plt.title("Brighter Image")
        plt.axis("off")

        bright_img.save("Results/brighter_image.jpg")
        plt.show()


def part4():
    with Image.open("image.jpg") as img:
        gray = img.convert("L")

        plt.figure()

        plt.subplot(1, 2, 1)
        plt.imshow(img)
        plt.title("Original")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(gray, cmap="gray")
        plt.title("Grayscale")
        plt.axis("off")

        gray.save("Results/image_gris.png")
        plt.show()


def part5():
    with Image.open("Results/image_gris.png") as gris:
        binaire = gris.point(lambda x: 255 if x > 100 else 0)

        plt.figure()

        plt.subplot(1, 2, 1)
        plt.imshow(gris, cmap="gray")
        plt.title("Image gris")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(binaire, cmap="gray")
        plt.title("Image binaire")
        plt.axis("off")

        binaire.save("Results/image_binaire.jpg")
        plt.show()


def part6():
    with Image.open("Results/image_gris.png") as gris:
        edges = gris.filter(ImageFilter.FIND_EDGES)

        plt.figure()

        plt.subplot(1, 2, 1)
        plt.imshow(gris, cmap="gray")
        plt.title("Gris")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(edges, cmap="gray")
        plt.title("Edges")
        plt.axis("off")

        edges.save("Results/image_contours.png")
        plt.show()


def part7():
    with Image.open("image.jpg") as img:
        blur1 = img.filter(ImageFilter.GaussianBlur(1))
        blur2 = img.filter(ImageFilter.GaussianBlur(2))
        blur3 = img.filter(ImageFilter.GaussianBlur(3))

        plt.figure()
        plt.subplot(1, 4, 1)
        plt.imshow(img)
        plt.title("Original")
        plt.axis("off")

        plt.subplot(1, 4, 2)
        plt.imshow(blur1)
        plt.title("Blur 1 ")
        plt.axis("off")

        plt.subplot(1, 4, 3)
        plt.imshow(blur2)
        plt.title("Blur 2 ")
        plt.axis("off")

        plt.subplot(1, 4, 4)
        plt.imshow(blur3)
        plt.title("Blur 3 ")
        plt.axis("off")

        blur1.save("Results/blur1.png")
        blur2.save("Results/blur2.png")
        blur3.save("Results/blur3.png")

        plt.show()


def part8():
    with Image.open("Results/image_gris.png") as gris:
        hist = gris.histogram()

        plt.hist(hist, bins=30, color="skyblue", edgecolor="black")
        plt.show()


def part9():
    with Image.open("Results/image_gris.png") as gris:
        equalizedImage = ImageOps.equalize(gris)

        hist1 = gris.histogram()
        hist2 = equalizedImage.histogram()

        plt.figure()

        plt.subplot(1, 4, 1)
        plt.imshow(gris, cmap="gray")
        plt.title("Non Equalized")
        plt.axis("off")

        plt.subplot(1, 4, 2)
        plt.imshow(equalizedImage, cmap="gray")
        plt.title("Equalized")
        plt.axis("off")

        plt.subplot(1, 4, 3)
        plt.hist(hist1, bins=30, color="skyblue", edgecolor="black")

        plt.subplot(1, 4, 4)
        plt.hist(hist2, bins=30, color="skyblue", edgecolor="black")

        equalizedImage.save("Results/equilized_image.png")

        plt.show()


def main():
    # 1. Map input strings to actual function objects
    parts_map = {
        "part1": part1,
        "part2": part2,
        "part3": part3,
        "part4": part4,
        "part5": part5,
        "part6": part6,
        "part7": part7,
        "part8": part8,
        "part9": part9,
    }

    # 2. Keep asking until a valid part is entered
    while True:
        user_input = (
            input("Please enter the part (part1, part2, ... part9):").strip().lower()
        )

        if user_input in parts_map:
            # 3. Call the matched function
            parts_map[user_input]()
        else:
            print("Invalid input. Please try again.\n Options: part1..9\n")


if __name__ == "__main__":
    main()
