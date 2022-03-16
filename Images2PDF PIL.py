from PIL import Image

img1 = Image.open("1.jpg")
img2 = Image.open("2.jpg")
img3 = Image.open("3.jpg")
img1.convert("RGB")
img2.convert("RGB")
img3.convert("RGB")
img1.save(r"images.pdf", save_all=True, append_images=[img2, img3])