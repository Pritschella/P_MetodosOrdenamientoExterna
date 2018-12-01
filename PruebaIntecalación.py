'''
Created on 30/11/2018

@author: acer
'''
archivo3 = open("ArchivoSalida2.txt", "w")
archivo1 = open("Archivo1.txt", "r")
archivo2 = open("Archivo2.txt", "r")
repetir = True

lineaArchivo1 = archivo1.readline()
lineaArchivo2 = archivo2.readline()

while(repetir):
    if(int(lineaArchivo1) < int(lineaArchivo2)):
        archivo3.write(lineaArchivo1)
        lineaArchivo1 = archivo1.readline()
        if(lineaArchivo1 == ""):
            archivo3.write("\n")
            archivo3.write(lineaArchivo2)
            lineaArchivo2 = archivo2.readline()
            while(lineaArchivo2 != ""):
                archivo3.write(lineaArchivo2)
                lineaArchivo2 =  archivo2.readline()
            repetir = False
    elif(int(lineaArchivo1) > int(lineaArchivo2)):
        archivo3.write(lineaArchivo2)
        lineaArchivo2 = archivo2.readline()
        if(lineaArchivo2 == ""):
            archivo3.write("\n")
            archivo3.write(lineaArchivo1)
            lineaArchivo1 = archivo1.readline()
            while(lineaArchivo1 != ""):
                archivo3.write(lineaArchivo1)
                lineaArchivo1 =  archivo1.readline()
            repetir = False
    else:
        archivo3.write(lineaArchivo1)
        archivo3.write(lineaArchivo2)
        lineaArchivo1 = archivo1.readline()
        if(lineaArchivo1 == ""):
            archivo3.write("\n")
            archivo3.write(lineaArchivo2)
            lineaArchivo2 = archivo2.readline()
            while(lineaArchivo2 != ""):
                archivo3.write(lineaArchivo2)
                lineaArchivo2 =  archivo2.readline()
            repetir = False
        lineaArchivo2 = archivo2.readline()
        if(lineaArchivo2 == ""):
            archivo3.write("\n")
            archivo3.write(lineaArchivo1)
            lineaArchivo1 = archivo1.readline()
            while(lineaArchivo1 != ''):
                archivo3.write(lineaArchivo1)
                lineaArchivo1 = archivo1.readline()
            repetir = False
                
archivo2.close
archivo1.close
archivo3.close

print("Archivos combinados y ordenados correctamente")
    
                
                
                
                    
