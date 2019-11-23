# This script is created to automatically organize the shitloads of call recordings that I have
import os, time, shutil, calendar
def organizeFiles(f):
    ogname = dir + f
    #Splitting filenames with underscore and period to get the "date and time"
    try:
        f = f.split("_")[1].split(".")[0]
    except:
        return
    f = f[0:8]  #Slicing string to get only the date
    print(ogname)
    print(f)
    year = f[0:4]
    month = f[4:6]
    day = f[6:8]
    folder = dir + day + "-" + month + "-" + year
    if os.path.exists(folder):
        shutil.move(ogname, folder)
        print("Moved " + ogname + " to " + folder)
    else:
        os.mkdir(folder)
        print("Folder created " + folder)
        shutil.move(ogname, folder)
        print("Moved " + ogname + " to " + folder)

dir = input("Enter the complete path: ") + "\\"
files = os.listdir(dir)
for f in files:
    organizeFiles(f)
