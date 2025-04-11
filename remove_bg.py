from rembg import remove
from PIL import Image

with open('glibi.jpg','rb') as img_file: #glibi.jpg is your picture file
    input_image = img_file.read()

output_image = remove(input_image)

with open('output.png','wb') as output_file: #output.png is your name of file when complete
    output_file.write(output_image)
