# This script is created to automatically organize the shitloads of call recordings that I have

import os, time, shutil, calendar
#for i in range (1,20):
#    f = open("Someshit_2019"+str(i)+"10_sommoreshit", "x+")
#    f.write("Random")
#    f.close
dir = input("Enter the complete path: ") + "\\"
files = os.listdir(dir)
for f in files:
    # moddate = time.ctime(os.path.getctime(f))
    #  print(repr(moddate))
    # splitdate = moddate.split()
    # print(splitdate[1])
    ogname = dir + f
    print(ogname)
    #Splitting filenames with underscore and period to get the "date and time"
    try:
        # block raising an exception
        f = f.split("_")[1].split(".")[0]
    except:
        continue # doing nothing on exception
    #Slicing string to get only the date
    f = f[0:8]
    print(ogname)
    print(f)
    year = f[0:4]
    month = f[4:6]
    day = f[6:8]
    folder = dir + day + "-" + calendar.month_abbr[int(month)] + "-" + year
    if os.path.exists(folder):
        shutil.move(ogname, folder)
        print("Moved " + f + " to " + folder)
    else:
        os.mkdir(folder)
        print("Folder created " + folder)
        shutil.move(ogname, folder)
        print("Moved " + ogname + " to " + folder)
