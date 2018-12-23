from PIL import Image

InFile = "%d.bmp"
OutFile = "%d.ico"

for num in range(1, 9):
    Image.open(InFile % num).save(OutFile % num)
