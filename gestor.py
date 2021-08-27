import time
#from os import system

from lote import Lote
from proceso import Proceso

class Gestor:
  def __init__(self):
    self.procesos = []
    self.lotes = []
    self.procesos_terminados = []
    self.lotes_terminados = 0

  def capturar_info(self):
    self.num_proceso = int(input("Número de procesos: "))
    num_proc_act = 0

    for i in range(self.num_proceso):
      proceso = Proceso()
      num_proc_act += 1
      self.procesos.append(proceso)

      if num_proc_act == 4:
        lote = Lote()
        lote.listas_procesos.append(self.procesos)
        self.lotes.append(lote)
        num_proc_act = 0
        self.procesos = []
    
    if len(self.procesos) > 0:
      lote = Lote()
      lote.listas_procesos.append(self.procesos)      
      self.lotes.append(lote)
  
  def terminar_proceso(self, proceso):
    num_proc_terminado = 0    
    num_lote = 1
    self.procesos_terminados.append(proceso)

    for proceso in self.procesos_terminados:

      if num_proc_terminado == 4:
        print("***************")
        num_lote += 1
        num_proc_terminado = 0

      num_proc_terminado += 1
      print(f"ID:{proceso.num_programa}")
      print(f"Operación:{proceso.operacion}")
      print("Resultado: ")
  
  def ejecutar_proceso(self, proceso):
    print(f"Nombre:{proceso.nombre}")
    print(f"Operación:{proceso.operacion}")
    print(f"Tiempo:{proceso.TME}")
    print(f"ID:{proceso.num_programa}")

    num_seconds = proceso.TME 

    def mostrar_tiempo():
      print(f'\rTiempo Transcurrido: ', end=f'{countdown}', flush=True)
      print(f' Tiempo Restante:', end=f'{num_seconds-countdown}', flush=True)  

    for countdown in range(num_seconds + 1):
      if countdown > 0:
          mostrar_tiempo()
          time.sleep(1)

    self.terminar_proceso(proceso)

  def listar_procesos(self, lote):
    print("Lote en Ejecución: ")
    for lista_pro in lote.listas_procesos:
      lista_pro2 = lista_pro.copy()
      for pro in lista_pro: # for pro in lista_pro

        proceso_a_ejecutar = lista_pro2.pop(0)

        for p in lista_pro2:
          print(f"Nombre:{p.nombre}") #pro.nombre
          print(f"Tiempo Máximo Estimado:{p.TME}")

        self.ejecutar_proceso(proceso_a_ejecutar)

        #self.ejecutar_proceso(proceso_a_ejecutar) # pro


  def empezar(self):
    for lote in self.lotes:
      self.listar_procesos(lote)
    """"
    for lote in self.lotes:
      for lista_pro in lote.listas_procesos:
        for pro in lista_pro:
          print(pro.nombre)
    """

    
