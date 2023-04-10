numeros = list(range(1, 11))

# Iterable (percorriveis)
for numero in numeros:
    print ("Tabuada do: ", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("---------")    
