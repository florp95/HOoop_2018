import random
import matplotlib.pyplot as pp 

#===========================================================================================================================================
#                                                     OBJETOS Y MÉTODOS
#===========================================================================================================================================

#--------------------------------------------------------------------------------------------------

class Fila(object):
    """Clase base de fila"""

    def __init__(self):
        """constructor de la clase Fila """
        self.enfila= 0
        self.fila = []

#---------------------------------------------------------------------------------------------------

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""   
    
    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.enfila+=1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente prederencial"""

        if self.enfila>0:               #Para que atiendan solamente si e que hay alguien en la fila

            self.enfila-=1
            self.fila.pop(0)           #Saco primer elemento de la fila (Atienden al primer cliente)
    
    def abrircajanueva(self, filanueva,maxenfila=20):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        
        if self.enfila>maxenfila:
		
		
		    #x=self.fila.pop(0)                     ESTOY SACANDO EL PRIMER ELEMENTO DE LA FILA pref Y LO ESTOY GUARDANDO EN X
		    #filanueva.insertar(x)
		
		    #Algo mas elegante
	               
            self.enfila-=1
		
            filanueva.fila.append(self.fila.pop(0))  #ESTOY METENIENDO EL QUE SAQUÉ DENTRO DE LA FILA NUEVA
                                                      # Y LLAMANDO AL METODO !! lo del método no funcionó ... asi  que puse append
            filanueva.enfila+=1
        	
            #mensaje para mi, yo estoy metiendo un objeto en abrircajanueva, puedo usar cualquier mètodo de ka fila preferencial
            #para hacerle cosas !! usas pop y todo esoooo.  FALTA ACOMODAR LO DE ENFILA !!!    
    
#----------------------------------------------------------------------------------------------------------------------    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila+=1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente prederencial"""

        if self.enfila>0:
            
            self.enfila-=1
            self.fila.pop(0)     
#----------------------------------------------------------------------------------------------------------------------
    
class cliente(object):
    """clase cliente """
    def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria=categoria


#============================================================================================================================================
#                                                      MAIN  
#============================================================================================================================================    

if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
  
    fg1=FilaGeneral()
    fp1=FilaPreferencial()
    fp2=FilaPreferencial()

    total_personas_atendidas=0                   #  Para tener un contador de a cuánta gente se atendió en el día
    
    var_enfilaGeneral=[]                         # Voy a ir armando listas con la cantidad de gente que hay en cada tipo de 
    var_enfilaPref1=[]                           # fila y los tiempos correspondientes (Para despues hacer un gŕafico)
    var_enfilaPref2=[]
    var_tiempo=[]
                 

    for t in range (0,480):                      #  El banco atiende 8 hs, o sea 480 minutos 

        gentenueva=random.randint(0,3)           #  Para que por cada minuto no ntre nadie, entre 1 persona o entren 2
        
        total_personas_atendidas+= gentenueva    
        
        for i in range (0,gentenueva):

        
            fulane=cliente(i)
        
            a=random.randint(0,2)

       
            if a==0:
        
                fulane.modificarcategoria("General")
                fg1.insertar(fulane)
        
                       
            else:
            
                fulane.modificarcategoria("Preferencial")
                fp1.insertar(fulane)
                        
                fp1.abrircajanueva(fp2)
        
            #print(fg1.enfila)
            #print(fp1.enfila)

    
        if t%3 == 0:          #Cada tres minutos atienden a una persona nueva en la fila General 
        
            fg1.atender()
        
        if t%2 == 0:          #Cada dos minutos atienden a una persona de la fila pref 1 y de la 2 (Si es que tienen gente)

            fp1.atender()
            fp2.atender() 
            
        var_enfilaGeneral.append(fg1.enfila)   #Relevo la cantidad de gente que hay en el tiempo dado
        var_enfilaPref1.append(fp1.enfila)
        var_enfilaPref2.append(fp2.enfila)
        var_tiempo.append(t)                  #Pienso que en t=0 ya hay gente que llegó temprano, antes de que comenzaran a atender
                                              #Por eso ya hay gente para tiempo 0. 
   

#------------------------------------------------------------------------------------------------------------   
    
    print(fg1.enfila)
    
    print(fp1.enfila)

    print(fp2.enfila)

    print(total_personas_atendidas)


    pp.plot(var_tiempo,var_enfilaGeneral,'r', label='Fila General')   
    pp.plot(var_tiempo,var_enfilaPref1,'g', label='Fila Preferencial 1')
    pp.plot(var_tiempo,var_enfilaPref2,'b', label='Fila Preferencial 2')

    pp.ylabel("Cantidad de Clientes")
    pp.xlabel("Tiempo [minutos]")

    pp.title("Cantidad de clientes por fila en función del tiempo")
    
    pp.grid()

    pp.legend()

    pp.savefig("FilasBanco.jpg",dpi=200)

    pp.show()
       
    
#------------------------------------------------------------------------------------------------------------
























