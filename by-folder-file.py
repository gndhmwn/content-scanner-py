import os
import sys
 

def list_files(start_path='.'):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = str(os.path.join(root, file))
            try:
                if val_2 in file_path:
                    print(file_path)

            except Exception as e:
                pass

val_1 = sys.argv[1]
val_2 = input('Keyword: ')
list_files(val_1)

