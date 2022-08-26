import os
import shutil

from_dir = "C:/Users/Shree/Desktop"
to_dir = "C:/Users/Shree/Downloads"

listOfFiles = os.listdir(from_dir)
#print(listOfFiles)

for file_name in listOfFiles:
    name,ext = os.path.splitext(file_name)
    #print(name)
    #print(ext)
    if ext == '':
        continue
    if ext in ['.png','.jpg','jpeg']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+'imageFiles'
        path3 = to_dir+'/'+'imageFiles'+'/'+file_name
        if os.path.exists(path2):
            print('moving the file ',file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving the file ',file_name)
            shutil.move(path1,path3)