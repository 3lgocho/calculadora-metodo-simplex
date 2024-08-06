from magia.Main import main

class matrizDatos:

    def __init__(self):
        self.opcion = None
        self.variables = []
        self.restricciones = []
        self.operadores = []
        self.limites = []
        self.resultado = []

    def procesar_datos(self, modo, funcion_objetivo, restricciones, limites, operadores):
        self.opcion = modo
        self.variables = funcion_objetivo
        self.restricciones = restricciones
        self.operadores = operadores
        self.limites = limites
        self.funcionObjetivo()
        self.restriccionesLlenar()
        self.printear()

    def funcionObjetivo(self):
        self.resultado.append(self.opcion)
        self.resultado.append(f"{len(self.variables)},{len(self.restricciones)}")
        self.resultado.append(",".join(map(str, self.variables)))

    def restriccionesLlenar(self):
        for i in range(len(self.restricciones)):
            restriccion_completa = self.restricciones[i] + [self.limites[i], self.operadores[i]]
            restriccion_como_cadena = ",".join(map(str, restriccion_completa))
            self.resultado.append(restriccion_como_cadena)

    def printear(self):
        main(self.resultado)
        with open("solucionDosFases", "r") as archivo:
            lineas = archivo.readlines()
            lineaUltima = lineas[-1]
        print(lineaUltima)

# Ejemplo de uso
# if __name__ == "__main__":
#     matriz = matrizDatos()
#     modo = "max"
#     funcion_objetivo = [32, 26, 20]
#     restricciones = [[90, 20, 40], [30, 80, 60],[10,20,60]]
#     limites = [200, 180, 150]
#     operadores = ['<=', '<=','<=']
#     matriz.procesar_datos(modo, funcion_objetivo, restricciones, limites, operadores)
