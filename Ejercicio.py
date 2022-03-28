'''En un centro de inmunizacion se hizo un registro donde una cierta cantidad de personas asistieron a una
 jornada de vacunacion. Para ello se realiza una encuesta a un conjunto W de personas a quienes se les solicita
suministren la siguiente información: 
NOMBRE, GÉNERO, EDAD Y VACUNA
Se le pide a usted que desarrolle un programa donde procese la información, almacenada en un archivo de nombre REDES.TXT y
genere dos archivos de nombre VACUNADOS.TXT y NOVACUNADOS.TXT, con los nombres de las
personas que fueron vacunadas con alguna de las tres vacunas proporcionadas consideradas en el estudio o los que no usan
ninguna de las vacunas consideradas en el
estudio respectivamente, además...
determine e imprima por pantalla:
✓ Cantidad de personas que le colocaron una de las tres vacunas respectivamente
considerados en la encuesta
✓ Porcentaje de personas que fueron inmunizadas con alguna de las tres vacunas
considerados en la encuesta
✓ Nombre y edad de la primera persona que usa la vacuna Sinopharm
Consideraciones:
o El género se tomará como 1 =Femenino y 2 = Másculino
o Los valores para las vacunas son 1 =SputnikV, 2 =Verocell, 3=Sinopharm y
4=Ninguno u otro
Actividades a Desarrollar:
1. Identifique los datos de entrada y salida, colocándolos en esta tabla con el tipo de
dato
'''

#inicializacion
linea = 1
cont1 = 0
cont2 = 0
cont3= 0
band = 0

arch1 = open('Datos.txt','r')
arch2 = open('vacunados.txt','w')
arch3 = open('novacunados.txt','w')

contenido = arch1.readlines()

w = int(contenido[0])

for i in range(w):
    
    lista = contenido[linea].split(',')
    linea += 1
    
    nombre = str(lista[0])
    genero =str(lista[1])
    edad = int(lista[2])
    vacuna = int(lista[3])
 
    if vacuna ==4:
        arch3.write(str(nombre) + '\n')
        
    else: 
        arch2.write(str(nombre)  + '\n')
        
        if vacuna == 1:
            cont1 += 1
            S = 'SputnikV'
        elif vacuna == 2:
            cont2 += 1
            v = 'Verocell'
        else:
            cont3 += 1
            s = 'Sinopharm'
            
            if band == 0:
                nombre_primer = nombre
                edad_primer = edad
                band = 1
    
por = (cont2 + cont3 + cont1)/w *100

print(' %d personas usan %s' % (cont1,S))
print(' %d personas usan %s' % (cont2,v))
print(' %d personas usan %s' % (cont3,s))

print('el %.2f' % por, '% de personas usan una de las tres vacunas' )

print('la primera persona encuestada que usa la Sinopharm es %s con %d años de edad' %(nombre_primer,edad_primer))

if cont1 > cont2 and cont1 > cont3:
    print('la vacuna mas usada es ', S)
elif cont2 > cont1 and cont2 > cont3:
    print('la vacuna mas usada ', v)
else:
    print('la vacuna mas usada es ', s)
arch1.close()
arch2.close()
arch3.close()