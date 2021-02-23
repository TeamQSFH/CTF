#!/usr/bin/python3

import sys
import zipfile

ouput = ""
def unzip(file_name):
    with zipfile.ZipFile(file_name) as myzip:
        out=[]
        file = myzip.namelist()[0]
        try:
            password = b'0'
            myzip.extractall('out', pwd=password)
        
            if '.zip' in file:
                print("0")
                #print('Unzipping, '+file+ ' with 0')
                #global output(append("1"))
                
                unzip('out/' + file)
                out.append("0")
                

        except:
            password = b'1'
            myzip.extractall ('out', pwd=password)
            
            if '.zip' in file:
                print("1")
                #print('Unzipping, '+file+ 'with 1')
                unzip('out/' + file)
                out.append("1")
    
    return(out)
        


output = unzip('turtles128.zip')
print(output)
