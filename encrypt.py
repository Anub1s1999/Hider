from numpy.lib.npyio import save
import stegano
from stegano import exifHeader
from PIL import Image
from PIL.ExifTags import TAGS
import sys
from os import error, read, write
from typing import Sized
import StegPNG
from secret import read_secret


print("\n\n")
print("||\\            //||")
print("||\\\          // ||")
print("|| \\\        //  ||")
print("||  \\\      //   ||")
print("||   \\\    //    ||")
print("||    \\\  //     ||")
print("||     \\\//      ||")
print("||      \/       ||")


print("\n\n")

def Extractor(imagename):
        # path to the image or video
        try:
            # read the image data using PIL
            image = Image.open(imagename)
            # extract EXIF data
            exifdata = image.getexif()
        except Exception as e:
            print(e)
        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")

def Hider(img,file):
    try:
        sec=read_secret(file)
        disappear=exifHeader.hide(img,"enco.jpg",secret_file=file)
        #print(exifHeader.reveal(img))
    except Exception as e:
        print(e)

def Decryptor(img):
    try:
        dec=exifHeader.reveal(img).decode("UTF-8")
        print(dec)
        with open('Textmess.txt','w') as f: 
            f.write(dec)
            f.close()
        
    except Exception as e:
        print(e)
