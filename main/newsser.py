from ftplib import FTP
import os
import env_platform
from dotenv import load_dotenv
load_dotenv(dotenv_path='./.env')
def newsse():
    ly=[]   
    '''YOUR FTP DETAILS'''
    ftp=FTP(os.getenv("FTP"))
    ftp.login()
    # user="root",passwd="123456"
    ftp.cwd('./')
    # print(ftp.dir)

    # os.chdir(os.getcwd()+'\\xxxxxxxxx')
    filename = "1.txt"
    localfile=open(filename,'wb')
    ftp.retrbinary('RETR '+filename,localfile.write,1024)
    print(" ")
    ftp.quit()
    localfile.close()

    filename="1.txt"
    file = open(filename, "r")

    for line in file:
        ly.append(line)
    os.chdir(os.getcwd()+'\\..')
    return ly