#!/usr/bin/python3

import sys
import zipfile


def unzip(file_name):
    with zipfile.ZipFile(file_name) as myzip:
        out=[]
        file = myzip.namelist()[0]
        try:
            password = b'0'
            myzip.extractall('out', pwd=password)       
            if '.zip' in file:
                print("0")
                unzip('out/' + file)
                               
        except:
            password = b'1'
            myzip.extractall ('out', pwd=password)            
            if '.zip' in file:
                print("1")
                unzip('out/' + file)
                
    return(out)
        

output = unzip('turtles128.zip')
