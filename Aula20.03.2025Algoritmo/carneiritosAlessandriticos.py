qtdEstrela = int(input())
carneiros = list(map(int, input().split(" ")))
count = 0
while True:
    if(carneiros[count] != 0):
        carneiros[count] -= 1
    
    if(carneiros[count] % 2 == 0):
        if((count + 1) == len(carneiros)):
            break
        count += 1
        
    else:
        if(count - 1 < 0):
            break
        
        count -= 1

carneritosRestantes = 0

for i in range(0, qtdEstrela):
    carneritosRestantes += carneiros[i]
print(f"{qtdEstrela} {carneritosRestantes}")