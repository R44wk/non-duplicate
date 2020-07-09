# By rumpelstiltskin
from io import open

def clean ():
    print ("Welcome\n")
    path= input("Original path from file: ")
    fichero = open (path,"r")
    line = set (fichero.readlines())
    fichero.close()
    name = raw_input("Name of new file: ")
    new_file = open (name, "a")
    for l in line:        
        new_file.write(l)
    new_file.close()
    print ("File \'{}' successfully saved :) ". format(name))
clean()