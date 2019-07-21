import random

#===========================================================================================================================================
#                                                     OBJETOS Y MÉTODOS
#===========================================================================================================================================

class Fila(object):
    """Clase base de fila"""

    def __init__(self):
        """constructor de la clase Fila """
        self.enfila= 0
        self.fila = []

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""   
    
    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.enfila+=1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente prederencial"""

        if self.enfila>0:

            self.enfila-=1
            self.fila.pop(0)
    
    def abrircajanueva(self, filanueva,maxenfila=10):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        
        if self.enfila>maxenfila:
		
		
		#x=self.fila.pop(0)        ESTOY SACANDO EL PRIMER ELEMENTO DE LA FILA pref Y LO ESTOY GUARDANDO EN X
		#filanueva.insertar(x)
		
		#Algo mas elegante
	               
                self.enfila-=1
		
                filanueva.fila.append(self.fila.pop(0))  #ESTOY METENIENDO EL QUE SAQUÉ DENTRO DE LA FILA NUEVA
                                                      # Y LLAMANDO AL METODO !! lo del método no funcionó ... asi  que puse append
                filanueva.enfila+=1
        	
#mensaje para mi, yo estoy metiendo un objeto en abrircajanueva, puedo usar cualquier mètodo de ka fila preferencial #para hacerle cosas !! usas pop y todo esoooo.  FALTA ACOMODAR LO DE ENFILA !!!    
    
    
    
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

    for t in range (0,4000):                           #Pasos temporales en los que el Banco trabaja

        gentenueva=random.randint(0,3)                  #Para que por cada paso temporal o no ntre nadie, entre 1 persona o entren 2
    
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

    
        if t%3 == 0: 
        
            fg1.atender()
        
        if t%2 == 0: 

            fp1.atender()
            fp2.atender() 
            
           
    print(fg1.enfila)
    
    print(fp1.enfila)

    print(fp2.enfila)

























