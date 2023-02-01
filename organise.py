import shutil
import os
fromdir = "C:/Users/kush2/Downloads"
todir = "C:/Users/kush2/OneDrive/Desktop"
fileslist = os.listdir(fromdir)
#print(fileslist)
for filename in fileslist:
    name, extension = os.path.splitext(filename)
#    print(name)
#    print(extension)
    if extension == "":
        continue
    if extension in [".gif",".png",".jpg",".jpeg",".jfif"] :
        path1 = fromdir + "/" + filename
        path2 = todir + "/" + "images in downloads folder"
        path3 = todir + "/" + "images in downloads folder" + "/" + filename
        print("path 1 is ", path1)
        print("path 3 is ", path3)
        if os.path.exists(path2):
            print("moving the..."+filename)
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving the..."+filename)
            shutil.move(path1,path3)