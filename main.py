from gestor import Gestor
#from lote import Lote
#from proceso import Proceso

gestor = Gestor()

gestor.capturar_info()

gestor.empezar()
""""
for lote in gestor.lotes:
  for lista_pro in lote.listas_procesos:
    for pro in lista_pro:
      print(pro.nombre)
"""