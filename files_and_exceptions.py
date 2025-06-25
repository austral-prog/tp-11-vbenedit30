def read_file_to_dict(filename):
    diccionario = {}
    try:
        with (open(filename, "r")) as file:
            line = file.readline().strip() #lee la linea del archivo
            prod_y_valor = line.split(";") #separa a los productos y valores
            for element in prod_y_valor:
                if ":" in element: #sólo avanza si el elemento existe, para evitar el errror provocado por el último ";"
                    producto, valor = element.split(":") #separa a cada elemento en producto y valor
                    valor = float(valor) #convierte el valor en un float
                    if producto not in diccionario:
                        diccionario[producto] = [valor] #crea el item en el diccionario
                    else:
                        diccionario[producto].append(valor) #agrega el valor a la lista de valor del item
    except FileNotFoundError: #por si el archivo no existe
        print ("Archivo no encontrado")
        raise
    return diccionario #lo devuelve vacío si no existe y si no, la respuesta correcta

def process_dict(data):
    for key, value in data.items():
        ventas_totales = 0 #actualiza el valor de ventas totales
        for element in value:
            ventas_totales += element #suma los valores de value, también se puede hacer con la función sum()
        promedio = ventas_totales/len(value) #saca el promedio de cada value
        print (f"{key}: ventas totales ${ventas_totales:.2f}, promedio ${promedio:.2f}") #imprime lo que tiene que imprimir según lo pedido, el .2f es para que se agreguen dos decimales al string
    return None #no retorna nada, porque el ejercicio no lo pide
