from __future__ import print_function

from ftplib import FTP

from termcolor import colored

import os
import time
import random
import env_platform
from dotenv import load_dotenv

from progress.bar import (FillingSquaresBar,PixelBar)

'''YOUR FTP SERVER DETAILS'''

# user="root",passwd="123456"

# ftp.cwd('./')
load_dotenv(dotenv_path='./.env')

def new_room(chatroom):
    ftp=FTP(os.getenv("FTP", None))
    ftp.login()
    ftp.mkd(chatroom)
    print("make new chatroom file dir")
    ftp.quit()

# TEMP=colored("WARNING","red")
# print(" [system]: "+TEMP+": Files can be exchanged between 2 users only")
global flnm

flnm=""
def sleep():
    t = 0.1
    t += t * random.uniform(-0.1, 0.1)  # Add some variance
    time.sleep(t)

def dwnldfile(chatroom):
    ftp=FTP(os.getenv("FTP", None))
    ftp.login()
    print(chatroom)
    ftp.cwd("./"+chatroom)
    print(ftp.dir())
    filename=input(colored(" [system]: filename: ","white"))
    time.sleep(1)
    ################################
        
    suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s]'
    bar = FillingSquaresBar(" [system]: downloading ", suffix=suffix)
    for i in bar.iter(range(100)):
        sleep()

    ##################################
    localfile=open(filename,'wb')
    ftp.retrbinary('RETR '+filename,localfile.write,1024)
    print(" ")
    time.sleep(0.9)
    print(colored(" [system]: file downloaded","white"))
    ftp.cwd("./../")
    localfile.close()
    ftp.quit()

    
 
def uploadfile(chatroom):
    ftp=FTP(os.getenv("FTP", None))
    ftp.login()
    ftp.cwd("./"+chatroom)
    filename = input(colored(" [system]: filename: ","white"))
    flnm=filename
    time.sleep(1)
    if os.path.isfile(filename):
        print("")
        print(" [system]: size: ",str(os.path.getsize(filename)))
        asw=input(colored(" [system]: are u sure to send {} (y/n): ".format(filename),"white"))
        if asw=='y':
            ################################
            suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s]'
            bar = PixelBar(" [system]: uploading ", suffix=suffix)
            for i in bar.iter(range(100)):
                sleep()
            ##################################
            ftp.storbinary('STOR '+filename, open(filename, 'rb'))
            time.sleep(1.2)
            print("")
            print(colored(" [system]: file uploded","white"))
            ftp.cwd("./../")
            ftp.quit()
        else:
            print(" [system]: operartion aborted")
            ftp.cwd("./../")
            ftp.quit()
            ftp
    else:
        print(" [system]: ERROR ! no such file named {} exists.".format(filename))

