import os
import sys


if __name__ == '__main__':
    dir_root:str = "C:\Mironchik"
    count:int = 0
    size_total:int = 0
    for dir_current, dirs_current, files_current in os.walk(dir_root):
        for file in filter(lambda f:f[-3:] == '.py', files_current):
            # if file[-3:] == '.py':
                name = f"{dir_current}/{file}"
                size:int = os.path.getsize(name)
                print(name, size)
                count+=1
                size_total+=size
    print("count: ", count,'  ',  "size: ", size, '  ')

