import os
import shutil

from_dir = "C:/Users/Shree/Desktop"
to_dir = "C:/Users/Shree/Downloads"

listOfFiles = os.listdir(from_dir)

for file in listOfFiles:
    name,ext = os.path.splitext(file)
    if ext == '':
        continue
    if ext in ['.pdf','.doc','.txt','.docx']:
        path1 = from_dir+'/'+file
        path2 = to_dir+'/'+'DocumentFiles'
        path3 = to_dir+'/'+'DocumentFiles'+'/'+file
        #print('path1',path1)
        #print('path3',path3)
        if os.path.exists(path2):
            print('moving.....')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving.....')
            shutil.move(path1,path3)