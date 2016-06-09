import os
import ftplib
from Pillow import Image

def ftpcopier(filename,source,userId):
    ftp = ftplib.FTP('cestasnp.sk')
    ftp.login("cestasnp.sk",'kockovo1256')
    ftp.cwd('/web/images/stories/Ostatne/sledovanie_upload') 
    
    try:
        folderName = str(userId)
    except:
        folderName = userId
    if folderName in ftp.nlst():
        ftp.cwd('/web/images/stories/Ostatne/sledovanie_upload/%s' %folderName)       
    else:
        ftp.mkd(str(folderName))
        ftp.cwd('/web/images/stories/Ostatne/sledovanie_upload/%s' %folderName)
    
    os.chdir(source)
    try:
        image = Image.open(filename)
        w, h = image.size
        image = image.resize((w/3, h/3), Image.ANTIALIAS)
        image.save(filename, 'JPEG', quality=80)
    except:
        print("image resize failed")

    myfile = open(filename, 'r')
    ftp.storbinary("STOR " + filename, myfile)
    myfile.close()
    ftp.quit()


def ftpdeleter(filename,userId):
    ftp = ftplib.FTP('cestasnp.sk')
    ftp.login("cestasnp.sk",'kockovo1256')
    ftp.cwd('/web/images/stories/Ostatne/sledovanie_upload') 
    ftp.cwd('/web/images/stories/Ostatne/sledovanie_upload/%s' %userId)
    
    ftp.delete('%s' %filename)
    ftp.quit()
