from stegano import lsbset
from stegano.lsbset import generators
import os
from PIL import Image
import re
from typing import Sized
import sys



def Intres(photo):
    message=str(input("Enter the Excutable/Text/Script path: "))
    with open (message,'r')as f:
        f=open(message,'r')
        content=f.read(message)
    print("You Text is: ",content)
    image=Image.open(photo)
    secimg=lsbset.hide(image,content,generators.eratosthenes())
    secimg.save("test(0).png")
    secimg=lsbset.hide(image,content,generators.identity())
    secimg.save("test(1).png")

x=''
def extract(path):
    message=''
    try:
        x=path
        message=lsbset.reveal(path,generators.eratosthenes())
    except Exception as e:
        print(e)
        print("The photo didn't encrypted by eratosthenes ")
    try:
        message=lsbset.reveal(path,generators.identity())
    except Exception as e:
        print(e)
        print("The photo didn't encrypted by identity ")
    if message=='':
        return 0
    with open('message.txt','w') as f:
        #text_file=open('message.txt','w')
        f.write(message)
    print("\r\n ****Writing Results in the file****** \r\n")
    f.close()
    print("\r\n *****File Closed******\r\n")
