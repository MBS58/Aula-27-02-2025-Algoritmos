import csv

with open ("amazon.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    contador = 0
    
    for i in reader:
        ano = i[0]
        estado = i[1]
        if ano == "2010" and estado == "Santa Catarina":
            quantidade = int(i[3])
            contador += quantidade
print(f"Contador de incendios em Santa Catarina em 2010: {contador}")
    
csv_file.close() 