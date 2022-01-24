# from datetime import timezone
# import time
import os
import datetime
from collections import OrderedDict
from requests import get
import subprocess


from mintsXU4 import mintsDefinitions  as mD

dataFolder = mD.dataFolder
jetsonID   = mD.jetsonID
# resolution = "640x480"
# resolution = "1280x720"
# resolution = "1920x1080"
# resolution = "2560x1440"
# resolution = "2048x1080"
resolution = "3840x2160"
# resolution = "7680x4320"

frameRate   = "60"


dateTime = datetime.datetime.now()

def directoryCheck(outputPath):
    exists = os.path.isfile(outputPath)
    directoryIn = os.path.dirname(outputPath)
    if not os.path.exists(directoryIn):
        print("Creating Directory @: " + outputPath)
        os.makedirs(directoryIn)
    return exists

def getCaptureDevice():
    fd = subprocess.Popen("v4l2-ctl --list-devices", shell=True, stdout=subprocess.PIPE)
    strIn1 = str(fd.stdout.read())
    strIn2 = strIn1.split('\\n\\n')
    for x in strIn2:
        if x.find("USB3.0 HD Video Capture")>0:
            strIn3 = x.split('\\n\\t')
            devIn = strIn3[1]
            print("Capture Device Found at: " + devIn)
            return devIn

def getWritePath(labelIn):
    # datetime = datetime.datetime.now()
    writePath = dataFolder+"/"+jetsonID+"/"+str(dateTime.year).zfill(4)  + "/" + str(dateTime.month).zfill(2)+ "/"+str(dateTime.day).zfill(2)+"/"+ "MINTS_"+ jetsonID+ "_" +labelIn + "_" + str(dateTime.year).zfill(4) + "_" +str(dateTime.month).zfill(2) + "_" +str(dateTime.day).zfill(2) + "_" +str(dateTime.hour).zfill(2)+  "_" +str(dateTime.minute).zfill(2)+  "_" +str(dateTime.second).zfill(2)+".mkv"
    directoryCheck(writePath)
    print("Write Path = " + writePath)

    return writePath;

def main():
    print("=============")
    print("    MINTS    ")
    print("=============")
    captDevice = getCaptureDevice() 
    writePath = getWritePath("captureMints")
    osRunString  = "ffmpeg -f v4l2 -framerate " +frameRate+ " -video_size " + resolution+ " -i "+ captDevice + " " + writePath
    print("Command: "+ osRunString)
    os.system(osRunString)

if __name__ == "__main__":
    main()

    

   

