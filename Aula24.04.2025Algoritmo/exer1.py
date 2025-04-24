# intervalo de tempo leio variavel

intervaloTempo = int(input("Qual o intevalo de Tempo"))


# realizo as divisoes para saber as horas minuto e segundos
# divisão no python que so usa inteiros 
horas = intervaloTempo // 60
# operador modulo para achar os minutos resto da divisão
minutos = intervaloTempo % 60
segundos = 0

#printo na tela os valores em horas minutos e segundos 
print("Horas", horas)
print("minutos", minutos)
print("segundos", segundos)


