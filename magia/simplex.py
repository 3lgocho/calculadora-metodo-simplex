tabla=[[]]
arregloFilas=[]
arregloCol=[]
from magia.escribir import *

class MetodoSimplex:
    '''
    Clase en la cual se implementa el metodo simplex
    esto quiere decir que se lleva a cabo un gauss jordan
    verificacion si se encuentra en la solucion optima
    '''
    def __init__(self, tablaAux,arregloFilasAux,arregloColumnasAux,esMin,file):
        global tabla,arregloFilas,arregloCol
        tabla = tablaAux  # tabla donde se almacena la forma estandar
        arregloFilas=arregloFilasAux # nombre de filas o variable basicas
        arregloCol=arregloColumnasAux # nombre de columnas
        self.esMin=esMin # booleano para saber si es minimizar o maximizar
        self.flagDg=False # bandera de funcion degenerada
        self.archivo=file # archivo donde se escribe
    '''
    Funcion que verifica si ya los valores de la fila Z
    son negativos o 0 en caso de que se trate de maximizar
    para saber si ya se llego a la condicion de parada
    '''
    def optimoMax(self):
        global tabla
        for x in range(0,len(tabla[0])-2):
            valor = tabla[0][x].NUM 
            if(valor>0): return False
        return True
    '''
    Funcion que verifica si ya los valores de la fila Z
    son positivos o 0 en caso de que se trate de minimizar
    para saber si ya se llego a la condicion de parada
    '''    
    def optimoMin(self):
        global tabla
        for x in range(len(tabla[0])-2):
            valor = tabla[0][x].NUM
            if(valor<0):return False
        return True
    '''
    Funcion encargada de encontrar el mas positivo
    para saber cual sera la columna Pivote 
    '''
    def encontrarColPivotMax(self):
        global tabla
        indica=(tabla[0][0].NUM)
        col=0
        for x in range(len(tabla[0])-2):
            if indica<(tabla[0][x].NUM) :
                indica = (tabla[0][x].NUM)
                col=x
        return col
    '''
    Funcion encargada de encontrar el mas negativo
    para asi saber cual es la columna pivote
    '''
    def encontrarColPivotMin(self):
        global tabla
        indica=tabla[0][0].NUM
        col=0
        
        for x in range(len(tabla[0])-2):
            if indica>tabla[0][x].NUM:
                indica = tabla[0][x].NUM
                col=x
        return col
    '''
    Funcion encargada de realizar la division entre la columna pivote 
    y la columna solucion 
    '''
    def realizarDivision(self,columna):
        global tabla
        for x in range(1,len(tabla)):
            if tabla[x][columna] == 0:
                tabla[x][len(tabla[x]) - 1] = 0
            elif tabla[x][columna] < 0:
                tabla[x][len(tabla[x]) - 1] = -1
            else:
                i = round(tabla[x][len(tabla[x]) - 2] / tabla[x][columna], 2)
                tabla[x][len(tabla[x]) - 1] = i
    '''
    Funcion encargada de encontrar cual es el cociente minimo
    para escoger la variable que sale
    '''
    def hallarFilaPivot(self): 
        global tabla 
        indica=1000
        fila=-1
        for x in range(1,len(tabla)):
            if(tabla[x][len(tabla[x])-1]>=0 and tabla[x][len(tabla[x])-1] < indica):
                indica =tabla[x][len(tabla[x])-1]
                fila=x
        return fila
    '''
    Funcion encargada de validar si corresponde a 
    minimizar o maximizar para luego poder encontrar la columna Pivot
    '''
    def elegirCol(self):
        if(self.esMin is True):return self.encontrarColPivotMax()
        else: return self.encontrarColPivotMax()
    '''
    Funcion encargada de verificar si existen dos o mas coeficientes
    minimos con el mismo valor
    De esta forma verificamos si se trata de una solucion degenerada o no
    '''
    def degeneradaSolucion(self,fila):
        cont=0

        for i in range(1,len(tabla)):
            if tabla[i][len(tabla[i])-1] == tabla[fila][len(tabla[i])-1]:
                cont+=1
                fila=i
        lista=[cont,fila]
        return lista
    '''
    Funcion que imprime datos de la solucion degenerada 
    '''
    def verificarDegenerada(self,degenerada):
        if self.flagDg is True:
            print("\n\n-> Solucion Degenerada hubo empate en coef minimo en coef minimo en el estado:"+str(degenerada)+"\n")
            self.archivo.write("\n\n-> Solucion Degenerada hubo empate en coef minimo en el estado:"+str(degenerada)+"\n")
    '''
    Funcion invocada cuando existe una solucion multiple
    '''
    def solucionExtra(self, col):
        global tabla,arregloFilas,arregloCol
        impresion=Imprime(self.archivo)
        columnaPivot= col
        self.realizarDivision(columnaPivot)
        filaPivot=self.hallarFilaPivot()
        print("- Numero Pivot: "+ str(round(tabla[filaPivot][columnaPivot],2))+ ",VB entrante: "+ arregloCol[columnaPivot]+ ",VB saliente: "+ arregloFilas[filaPivot])
        self.archivo.write("- Numero Pivot: "+ str(round(tabla[filaPivot][columnaPivot],2))+ ",VB entrante: "+ arregloCol[columnaPivot]+ ",VB saliente: "+ arregloFilas[filaPivot]+"\n")
        self.convertir_Fila_Pivot(filaPivot,columnaPivot)
        self.modificar_Filas(filaPivot,columnaPivot)
        self.modificar_FilaZ(filaPivot,columnaPivot)
        auxFila=arregloFilas[filaPivot]
        arregloFilas[filaPivot]=arregloCol[columnaPivot]
        impresion.imprime_Matriz()
        self.archivo.write("\n\n** Solucion EXTRA debido a que la variable no basica: "+ auxFila +" tenia un valor de 0 en el estado Final **\n")
        print("\n\n** Solucion EXTRA debido a que la variable no basica: "+  auxFila+" tenia un valor de 0 en el estado Final**")
    '''
    Funcion que inicia el metodo simplex
    '''
    def start_MetodoSimplex_Max(self):

        impresion=Imprime(self.archivo)
        estados=1
        global tabla,arregloFilas,arregloCol
        print_Aux= Print()
        multiplesSol=Multiples_Solucion()
        s=Solucion()
        degenerada=0
        s_Extra=Solucion()
        cont=0
        print_Aux.imprime_Matriz(tabla,arregloFilas,arregloCol,self.archivo) 
        while True:
            #Condicion de parada
            if self.optimoMax() is True and self.esMin is False or self.optimoMax() is True and self.esMin is True :
                self.verificarDegenerada(degenerada)#DEGENERADA
                print("\n- Estado Final")
                self.archivo.write("\n- Estado Final\n")
                s.mostrarSolucion(tabla,arregloFilas,arregloCol,self.archivo, self.esMin)

                if multiplesSol.localizar_VB(tabla,arregloFilas,arregloCol)!= -1: # se verifican si existe una solucion multiple
                    #existen multiples soluciones
                    print("\n->Existen multiples soluciones\n")
                    self.archivo.write("\n->Existen multiples soluciones\n")
                    self.solucionExtra(multiplesSol.localizar_VB(tabla,arregloFilas,arregloCol))
                    
                    s_Extra.mostrarSolucion(tabla,arregloFilas,arregloCol,self.archivo, self.esMin) # muestra solucin extra
                
                return tabla
            
            columnaPivot= self.elegirCol() #Elige cual es el valor en Z mas negativo o mas positivo
            
        
            self.realizarDivision(columnaPivot) #division de la columna pivote
            
            filaPivot=self.hallarFilaPivot()
            

            if(filaPivot == -1):#VERIFICA SOLUCION ACOTADA  # verificacion solucion acotada
                print("\n- Estado: "+ str(estados))
                self.archivo.write("\n- Estado: "+ str(estados)+"\n")
                print("** Solucion NO acotada  debido a que en la columna Pivote:"+ str(columnaPivot)+ " cada uno de los valores es negativo o 0 **")
                self.archivo.write("** Solucion NO acotada  debido a que en la columna Pivote:"+ str(columnaPivot)+ " cada uno de los valores es negativo o 0 **\n")
                s.mostrarSolucion(tabla,arregloFilas,arregloCol,self.archivo,self.esMin)
                return tabla
            
            if self.degeneradaSolucion(filaPivot)[0] >= 2: 
                self.flagDg=True
                filaPivot=self.degeneradaSolucion(filaPivot)[1]
               
                degenerada=estados+1

            self.archivo.write("\n- Estado: "+ str(estados)+"\n") # se escribe en el archivo de salida

            print("\n- Estado: "+ str(estados))
            estados+=1
            self.archivo.write("- Numero Pivot: "+ str(round(tabla[filaPivot][columnaPivot],2))+ ",VB entrante: "+ arregloCol[columnaPivot]+ ",VB saliente: "+ arregloFilas[filaPivot]+"\n")
            print("- Numero Pivot: "+ str(round(tabla[filaPivot][columnaPivot],2))+ ",VB entrante: "+ arregloCol[columnaPivot]+ ",VB saliente: "+ arregloFilas[filaPivot])
            arregloFilas[filaPivot]=arregloCol[columnaPivot]
            
            self.convertir_Fila_Pivot(filaPivot,columnaPivot) # Metodo gauss jordan
            self.modificar_Filas(filaPivot,columnaPivot)
            self.modificar_FilaZ(filaPivot,columnaPivot)

            impresion.imprime_Matriz()
 
    def modificar_Filas(self,filaPivot,columnaPivot):
        global tabla
        for i in range(1,len(tabla)):
            if i != filaPivot:
                arg1=tabla[i][columnaPivot]
                for j in range(0,len(tabla[i])-1):
                    x=tabla[i][j]-arg1*tabla[filaPivot][j]
                    tabla[i][j]=x

    def modificar_FilaZ(self,filaPivot,columnaPivot):
        global tabla
        lista=[]
        lista2=[]
        for i in range(len(tabla[0])-2):
            arg2=tabla[0][columnaPivot].NUM
            y=tabla[0][i].NUM-arg2*tabla[filaPivot][i]
            lista2.append(y)
        arg2=tabla[0][columnaPivot].NUM
        if self.esMin is True:
            y=tabla[0][len(tabla[0])-2].NUM-arg2*tabla[filaPivot][len(tabla[0])-2] 
        else:
            y=tabla[0][len(tabla[0])-2].NUM+arg2*tabla[filaPivot][len(tabla[0])-2]
        lista2.append(y)
        x=0
        while x < len(lista2):
            tabla[0][x].NUM=lista2[x]
            x+=1
    '''
    Funcion encargada de hacer el valor pivote en uno
    '''
    def convertir_Fila_Pivot(self,filaPivot,columnaPivot):
        if(tabla[filaPivot][columnaPivot] != 0):
            denominador=(1/tabla[filaPivot][columnaPivot])
        else:
            denominador = 1
        y=0
        while y < len(tabla[filaPivot])-1:
            numerador=(tabla[filaPivot][y])
            x= numerador*denominador
            tabla[filaPivot][y]=x
            y+=1

#Impresion de la parte grafica
class Imprime:
    #Constructor
    def __init__(self,file):
        self.archivo=file
    '''
    Funcion en la cual se imprimen el nombre
    correspondiente a cada una de las filas ya sea
    var de holgura artificial o basica
    '''
    def imprime_Columnas(self):
        global arregloCol
        aux="\n\n\n\t"
        aux2="\t"
        for i in arregloCol:
            aux+=i+"\t\t"
            aux2+=""
        aux2+=""
        print (aux+"\n"+aux2)
        self.archivo.write("\n"+aux+"\n"+aux2+"\n")


    def imprimeFilaZ(self):
        global arregloFilas
        aux=arregloFilas[0]+"\t"
        for x in range (len(tabla[0])):
            var2=round(tabla[0][x].NUM,2)
            aux+=str(var2)+"\t\t"
        print (aux)
        self.archivo.write(aux+"\n")

    '''
    Funcion encargada de imprimir la primer matriz
    una vez se encuentre estandarizada
    '''
    def imprime_Matriz(self):
       global tabla,arregloFilas
       if(len(tabla) is not 0):
          aux=""
          self.imprime_Columnas()
          self.imprimeFilaZ()
          for i in range (1,len(tabla)):
              aux=arregloFilas[i]+"\t"
              for j in range (len(tabla[i])):
                  var=round(tabla[i][j],2)
                  aux+=str(var)+"\t\t"
              self.archivo.write(aux+"\n")
              
              print(aux)
