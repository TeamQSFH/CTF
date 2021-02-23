import zipfile

def main():
    parent_file_name = 'turtles128.zip'
    pswd = '0'
    global bits
    with zipfile.ZipFile(parent_file_name, 'r') as parent_file:

        parent_file.extractall(pwd=bytes(pswd, 'utf-8'))
        next_zip_name = parent_file.namelist()[0]  # getting the first child
        
        while True:
            try:
                if (pswd == '0'):
                    with zipfile.ZipFile(next_zip_name, 'r') as child_file:

                        child_file.extractall(pwd=bytes(pswd, 'utf-8'))  # extracting the zip

                        next_zip_name = child_file.namelist()[0]  # getting the next zip name
                        bits.append(int(pswd))
                        ##print(child_file)
                        print(pswd,end='')
                        pswd = '1'

                elif (pswd == '1'):
                    with zipfile.ZipFile(next_zip_name, 'r') as child_file:

                        child_file.extractall(pwd=bytes(pswd, 'utf-8'))

                        next_zip_name = child_file.namelist()[0]
                        bits.append(int(pswd))
                        ##print(child_file)
                        print(pswd,end='')
                        pswd = '1'

            except:
                if(pswd=='1'):
                    pswd='0'
                else:
                    pswd='1'

if __name__ == '__main__':
    main()
    bits = []
    print(bits)
