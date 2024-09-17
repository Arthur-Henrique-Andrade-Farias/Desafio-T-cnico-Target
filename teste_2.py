def pertence_fibonacci(numero):
    a = 0
    b = 1 
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b  
    return False

numero = 3
print(pertence_fibonacci(numero))
