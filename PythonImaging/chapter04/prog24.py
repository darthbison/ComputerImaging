from PIL import Image, ImageOps

im1 = Image.open("/home/pi/DIP/Dataset/5.1.12.tiff")

im2 = ImageOps.colorize(im1, (125, 150, 134), (10, 12, 17))

im2.show()
