from PIL import Image

def DeleteMeta(image):
    photo = Image.open(image)

    # next 3 lines strip exif
    data = list(photo.getdata())
    image_without_exif = Image.new(photo.mode, photo.size)
    image_without_exif.putdata(data)
    image_without_exif.save('image_file_without_exif.jpg')
    print ("Removing MetaData is Done\n")
