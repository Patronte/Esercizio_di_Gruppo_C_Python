import funzioni 
menu = True

nome = str(input("Inserisci il tuo nome: "))

while menu:
    scelta= int(input('scegli un esercizio tra 1, 2, 3,4,5: '))


    match scelta:
        case 1:
            print('hai scelto uno')
            print(funzioni.somma(1,5))
            
        case 2:
            numero = int(input('scegli  quanti valori vuoi inserire '))
            print(funzioni.creaLista(numero))
            
        case 3:
            pass
        case 4:
            pass
        case _:
            print('Sei un pippo')
            
            
            
            
            
            
