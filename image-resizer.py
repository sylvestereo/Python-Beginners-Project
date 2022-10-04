from PIL import Image

def resize_image(size1, size2):
    image = Image.open('qrimg.png')

    print(f'Current size: {image.size}')

    resized_image = image.resize((size1, size2))

    resized_image.save('qrimg22'+ str(size1) +'.png')

size1 = int(input('Enter length: '))
size2 = int(input('Enter Width: '))
resize_image(size1, size2)