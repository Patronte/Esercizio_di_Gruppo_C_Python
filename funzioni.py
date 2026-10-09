# """ """ #Es riassuntivo
# Prt 1
# Hai 60 min per creare un esercizio che rappresenti tutto quello che hai imparato nella settimana precedente

# #necessità modulo main, decidere cosa fare in ogni case, modulo con


# Creare un menu 
# match case per il menu degli argomenti confermato
# ogni case è un macro argomento


# case "Variabili" 
#     all'interno spiegare e mostrare come funziona l'argomento con esempi pratici 
# case"Liste"
# case"Controllo del flusso"
#     if selezione "if/while/for"
    
# case "Funzioni"
# case "Moduli"


 

def somma(a,b):
    return a+b

def sottrazione (a,b):
    return a-b

def moltiplicazione (a,b):
    return a*b

def divisione (a,b):
    return a/b

nome = str(input("Inserisci il tuo nome: "))
def saluto (nome):
    print("Ciao ,", nome)
    print("Benvenuto nelle funzioni")
    
saluto(nome)

def spiega (a):
    a = input("Seleziona un topic: ")
    if a.lower()== "variabili":
        a = b
        print(a)

b = "Spiegazione variabili"




            
def creaLista(numero):

    lista = []
    for i in range(numero):
        number= int(input('dammi un numero '))
        lista.append(number)
    return lista

