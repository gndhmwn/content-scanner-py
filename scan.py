import os
import sys
from datetime import datetime as dt
import time


date = '2024-10-30'
ExpirationDate = time.strftime("%Y-%m-%d")
class Timedelta(object):
    @property
    def isoformat(self):
           return str()

def banner():
    front = '''
     _                                                        
    /   ._   _    _.  _|_   _    _|    |_                     
    \_  |   (/_  (_|   |_  (/_  (_|    |_)  \/                
                                            /                 
          ___                      __                ___  ___ 
    |\ |   |   |\ |    |   /\     (_    /\   \    /   |    |  
    | \|  _|_  | \|  \_|  /--\    __)  /--\   \/\/   _|_   |  

    '''
    print(front)
    time.sleep(3)

def currentDateTime():
    date_format = '%Y%m%d_%H%M'
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

if ExpirationDate >= date or ExpirationDate == date:
    print('Renew License Soon')
    quit()
else:
    banner()
    checkContent(val_1)
    







