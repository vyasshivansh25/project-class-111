import os
import shutil
from_dir="C:/Users/USER/Downloads"
to_dir="C:/pdf 111"
list_files=os.listdir(from_dir)
#print(list_files)
for file_name in list_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)