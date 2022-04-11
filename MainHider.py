#from _typeshed import FileDescriptor
from typing import Text
from numpy import fromfile
import decode
import secret
import StegPNG
import encrypt
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e","--encrypt",help="Encrypts the message into Image",action='store_true')
    parser.add_argument("-d","--decrypt",help="Decrypts the message into Image",action='store_true')
    parser.add_argument("-png","--pngphoto",help="Indintify the photo extention")
    parser.add_argument("-jpg","--jpgphoto",help="Photo Extention of jpeg or jpg")
    #parser.add_argument("-i","--intensive",help="Intensive Encryption",action='store_true')
    parser.add_argument("-f",'--file', help= 'paste path to message.txt file',type=str)
    args = parser.parse_args()
    #test=str(args.file)
    #print('Attention',str(test))
    if args.pngphoto:
        if args.encrypt:
            try:
                StegPNG.Intres(args.pngphoto)  #hiding
            finally:
                secret.encode(args.pngphoto,args.file) #hiding
        else: 
            try:
                StegPNG.extract(args.pngphoto) #appearing
            finally:
                decode.decode(args.pngphoto,'txt')
    else:
        if args.encrypt :
            encrypt.Hider(args.jpgphoto,args.file)
        else:
                encrypt.Decryptor(args.jpgphoto)
                print("\r\nBefore The Decryption \r\n")
                encrypt.Extractor(args.jpgphoto)
if __name__=="__main__":
    main()
