def read_file_to_dict(filename):
    dict_ = {}
    try:
        with open(filename, "r") as file:
            for linea in file:
                valores = linea.strip().split(";")
                for i in valores:
                    if i:  
                        producto, valor = i.split(':')
                        valor = float(valor)  

                        if producto not in dict_:
                            dict_[producto] = []

                        dict_[producto].append(valor)
    except FileNotFoundError as e:
        print(f"Error: el archivo '{filename}' no fue encontrado.")
        raise
    return dict_


def process_dict(data):
    for producto, precio in data.items():
        suma = sum(precio)
        promedio = suma / len(precio)
        print(f"{producto}: ventas totales ${suma:.2f}, promedio ${promedio:.2f}")
    pass
