# largura
larguraTerreno = int(input("Qual a largura do Terreno"))
# altura
alturaTerreno = int(input("Qual a Altura do Terreno"))
# dimensoẽs do terreno retangular
dimensaoTerreno = larguraTerreno * alturaTerreno


# largura
larguraCasa = int(input("Qual a largura do Casa"))
# altura
alturaCasa = int(input("Qual a Altura do Casa"))
# dimensoes da casa retangular 
dimensaoCasa = larguraCasa * alturaCasa

# calculo para saber os metros quadrados livres e a porcentagem em relação ao total do terreno
espaçoLivreMetrosQuadrados = dimensaoTerreno - dimensaoCasa
espaçoLivrePorcentagem = (espaçoLivreMetrosQuadrados / dimensaoTerreno ) * 100

# printo no terminal os valores 
print("Valor em Metros Quadrados", espaçoLivreMetrosQuadrados)
print("Valor em Porcentagem", espaçoLivrePorcentagem,"%")