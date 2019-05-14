# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:43:48 2019
This is a simple pythong file watcher.
This script will check if any ".blend" file appear in the a folder, 
if it does, will move the file to a target folder.
@author: alice
"""
from ftplib import FTP
import os 
import time
import os.path

from ftplib import FTP 
import os
import fileinput
#import shutil

#####################create your paths######################
#-----------------------------------------------------------
#there are paths, "pathWatch" is the folder you are watching.
#pathTarget is where any .blend files will be move to.
# you can set them to be whatever your files shall be at.

pathWatch=r'C:\Users\alice\Desktop\testingJason'
pathTarget=r'C:\Users\alice\Desktop\targetFolder'


#####################Checking Fucntions######################
#-----------------------------------------------------------

#this function, when call, will RETURN the name of the .blend file in the folder
def blendFileExist():
    #ListFile is a list with all the files in the folder
    listFiles=os.listdir(pathWatch)
    for file in listFiles:
        if '.blend' in file:
                return file
#-----------------------------------------------------------

#this funciton will take one input -the file name and will move that file to target folder    
def moveFile(fileName):
   oldLocation = pathWatch + '\\' + str(fileName) 
   newLocation = pathTarget+ '\\' + str(fileName)
   
   os.rename(oldLocation,newLocation)
#   shutil.move(oldLocation,newLocation)

#-----------------------------------------------------------

    
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('ec2-18-220-233-157.us-east-2.compute.amazonaws.com', 21) 
    ftp.login()
     
    ftp.cwd('/upload')
    
    fp = open(localfile, 'rb')
    ftp.storbinary('STOR %s' % os.path.basename(oldFile), fp, 1024)
    fp.close()



#####################Flow Fucntions#########################
#-----------------------------------------------------------
#checkinf every 3 seconds and attempt to move the file

if __name__ == "__main__":
    while True:
        try:
            moveFile(blendFileExist())
        except:
            pass
        time.sleep(3)
