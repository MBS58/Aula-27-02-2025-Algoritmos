codigoPeca1, numeroPeca1, valorUnitario1 = map(float, input().split())
codigoPeca2, numeroPeca2, valorUnitario2 = map(float, input().split())

valorFinal = (numeroPeca1 * valorUnitario1) + (numeroPeca2 * valorUnitario2)
print(f"VALOR A PAGAR: R$ {valorFinal:.2f}")