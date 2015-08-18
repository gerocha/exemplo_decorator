def altera(f):
    def decorador(a, b):
        return a - b
    return decorador

# estou chamanando altera(soma(a, b))
@altera
def soma(a, b):
    return a+b

print(soma(1, 2))
