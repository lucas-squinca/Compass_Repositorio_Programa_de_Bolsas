def calcular_valor_maximo(operadores,operandos) -> float:
    def conta(operador, operando):
        if operador == '+':
            return operando[0] + operando[1]
        elif operador == '-':
            return operando[0] + operando[1]
        elif operador == '*':
            return operando[0] * operando[1]
        elif operador == '/':
            return operando[0] / operando[1]
        elif operador == '%':
            return operando[0] % operando[1]
    
    results = list(map(lambda x: conta(x[0], x[1]), zip(operadores, operandos)))

    maior = max(results)

    return maior
