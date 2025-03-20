A, B, C = map( float, input().split())

delta = (B*B) - (4*(A * C))

if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    X1 = ((-1*B) + (delta ** (1/2))) / (2 * A)
    X2 = ((-1*B) - (delta ** (1/2))) / (2 * A)
    print(f"R1 = {X1:.5f}")
    print(f"R2 = {X2:.5f}")
    
