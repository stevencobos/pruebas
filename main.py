inicio = 'Para la resolucion del problema necetamos tener los siguientes datos'
print(inicio)

#Datos Algoritmicos
Dato_1 = float(input('ingrese el diametro de la polea en centimetros (cm): '))
Dato_2 = float(input('ingrese el largo de la puerta en metros (mts): '))
Dato_3 = (Dato_2*100/Dato_1)
Dato_4 = (Dato_2*100/Dato_1/3)
#1m = 100cm


#problemas
Pro_1 = ('¿Cuántas vueltas deben darse para cerrar la puerta completamente?\n Respuesta:')
print(Pro_1)
sol_1 = 'la respuesta es:' ,Dato_3
print(sol_1)

pro_2 = 'Como cada Chewbacca solo puede girar la polea 3 veces antes de caer exhausto ¿Cuántos Chewbaccas se necesitan para cerrar la puerta?\n Respuesta:'
print(pro_2)

sol_2 = 'La respuesta es:', Dato_4
print(sol_2)

Pro_3 = 'Si se desea cerrar la puerta en un número máximo de minutos, que también nos dan, ¿A qué velocidad deben girar la polea (cms/seg) para poder cerrarla en ese tiempo?'
print(Pro_3)

Dato_5 = float(input('ingrese el tiempo maximo que desea:'))
Dato_6 = Dato_5*60
#1min= 60seg
def velocidad (cm_seg):
  vuel_seg_1 = (cm_seg*Dato_1)
  var_2 = (Dato_2*100)
  total = (vuel_seg_1/var_2)
  print('el resultado es:' , total, 'cm/seg')
velocidad (Dato_6)