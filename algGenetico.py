import random

#Nint = input("Ingrese el número que desea factorizar: ")
Nint = 3127
N = bin(Nint)[2:]

def cromosoma(individuo: str) -> bool:
    
    esIndividuo = True
    
    if(individuo[0] != "1"):
        esIndividuo = False
    
    if(len(individuo) > len(N)/2 and int(N, 2)%2 == 0):
        esIndividuo = False
        
    if(len(individuo) > (len(N)+1)/2 and int(N, 2)%2 != 0):
        esIndividuo = False
        
    return esIndividuo

def crearPoblacion(tam: int) -> list:
    
    poblacion = []
    Nint = int(N, 2)
    
    for i in range(0, tam):
        strIndividuo = "1"
        
        if(Nint % 2 == 0):
        
            for j in range(1, round(len(N)/2)):
                
                r = random.randint(1, 1000)
                rBit = r%2
                strIndividuo += str(rBit)
        
        else:
            
            for j in range(1, round((len(N) + 1)/2)):
                
                r = random.randint(1, 1000)
                rBit = r%2
                strIndividuo += str(rBit)
            
        if(cromosoma(strIndividuo)):   
            poblacion.append(strIndividuo)
    
    return poblacion

def cruce(poblacion: list, p: int) -> list:
    
    poblacionCruzada = []
    mitad = round(len(poblacion)/2)
    
    for i in range(0, mitad):
        j = i + mitad
        
        ind1 = poblacion[i]
        ind2 = poblacion[j]
        
        primeraMitad = ind1[0:round(len(ind1)/2)]
        
        segundaMitad = ind2[round(len(ind2)/2):round(len(ind2) - 1)]
        
        indNuevo = primeraMitad + segundaMitad
        
        r = random.randint(1, 100)
        
        if(cromosoma(indNuevo) and r <= p):
            poblacionCruzada.append(indNuevo)
    
    return poblacionCruzada

def mutacion(poblacion: list, p: int) -> list:
    poblacionMutada = []
    
    for i in range(0, len(poblacion)):
        ind = poblacion[i]
        change = random.randint(1, len(ind) - 1)
        
        parteIzq = ind[:change]
        mutacion = str((int(ind[change]) + 1) % 2)
        parteDer = ind[change + 1:]
        
        indMutado = parteIzq + mutacion + parteDer
        
        r = random.randint(1, 100)
        
        if(r <= p and cromosoma(indMutado)):
            poblacionMutada.append(indMutado)
            
def aptitud(individuo: str):
    
    p = int(individuo, 2)
    Nint = int(N, 2)

    resultado = Nint % p
    
    return resultado


def algoritmo():
    
    tamPoblacion = 10
    
    print("== Creando la población ==")
    
    poblacionInicial = crearPoblacion(tamPoblacion)

    
    print("La población inicial es:")
    for ind in poblacionInicial:
        print(ind + " -- " + str(int(ind, 2)) + " -- " + str(aptitud(ind)))
        
    G = 10
    poblacion = poblacionInicial
    
    for g in range(0, G):        

        poblacion.sort(key=aptitud)
        
        
            
        pobSeleccionada = poblacion[0: round(len(poblacion)/2)]
        
        pobCruzada = cruce(pobSeleccionada, 80)
        
        pobSeleccionada.extend(pobCruzada)
        
        pobMutada = mutacion(pobSeleccionada, 10)
        
        pobSeleccionada.extend(pobMutada)
        
        pobSeleccionada.sort(key=aptitud)
        
        pobSeleccionadaSigGen = pobSeleccionada[0: tamPoblacion]
        
        poblacion = pobSeleccionadaSigGen
        
        
    
    
    
algoritmo()      