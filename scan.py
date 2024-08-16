import os
import sys
from datetime import datetime as dt


def currentDateTime():
    date_format = '%Y-%m-%d %H:%M:%S'
    date_str = dt.now().strftime(date_format)
    return date_str

def createLog(x,y):
    now = currentDateTime().replace(' ','_')
    log = open(f'./result/{y}_{now}.txt', 'a')
    log.write(x)

def checkContent(start_path='.'):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = str(os.path.join(root, file))
            try:
                with open(file_path, 'r') as file:
                    file_content = file.read()

                    if f'.{val_2}' in file_path:
                        payloads = open('payload.txt', 'r')
                        for payload in payloads.read().splitlines():
                            if payload in file_content:
                                result = f'{file_path} ==> {payload}'
                                createLog(f'{result}\n',val_2)
                                print(result)

            except Exception as e:
                # print(f"An error occurred: {e}")
                pass

val_1 = sys.argv[1]
val_2 = sys.argv[2]

checkContent(val_1)





