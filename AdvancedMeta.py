from exif import Image
from PIL.ExifTags import TAGS

def decimal_coords(d,m,s,dir1):
    decimal_degrees = d+ m / 60 + s / (60*60)
    if dir1 == "S" or dir1 == "W":
         decimal_degrees *= -1
    return decimal_degrees

def meta(photo):
    with open(photo, "rb") as src:
        img = Image(src)
    if img.has_exif:
        info = f" has the EXIF {img.exif_version}"
        try:
            ggps2=img.gps_longitude
            ggps=img.gps_latitude
            lat=decimal_coords(ggps[0],ggps[1],ggps[2],img.gps_longitude_ref)
            lon=decimal_coords(ggps2[0],ggps2[1],ggps[2],img.gps_latitude_ref)
            coords = (decimal_coords(ggps[0],ggps[1],ggps[2],img.gps_longitude_ref),decimal_coords(ggps2[0],ggps2[1],ggps[2],img.gps_latitude_ref))
            print("\nThe Location of the given Photo:")
            print(coords,'\n')
            tes=img.get_all()
            print(tes)
            
        except Exception as e:
            print ("NO GPS INFO but here are the rest of Meta\n")
            tes=img.get_all()
            #print(tes)

    else:
       info = "does not contain any EXIF information"
    print(f"Image {src.name}: {info}")
