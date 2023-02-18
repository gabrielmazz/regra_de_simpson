import sympy as sp

def simpson(funcao_fx, intervalo_1, intervalo_2, iteracoes):
    
    #O primeiro bloco faz uma verificação se o número de iterações é par. A regra de Simpson requer que o 
    # número de iterações seja par, pois o método faz a aproximação por pares de intervalos. 
    if iteracoes % 2 == 1:
        print("Número de divisões deve ser par!")
        return None
    
    # Calculado o valor de h, que é a largura de cada subintervalo do intervalo de integração.
    h = (intervalo_2 - intervalo_1) / iteracoes
    soma = funcao_fx(intervalo_1) + funcao_fx(intervalo_2)
    
    # Utiliza um loop para percorrer os subintervalos de índices ímpares, e adiciona 4 vezes o valor da 
    # função no ponto médio de cada subintervalo à soma.
    for i in range(1, iteracoes, 2):
        soma += 4 * funcao_fx(intervalo_1 + i * h)
        
    # Utiliza um segundo loop para percorrer os subintervalos de índices pares, e adiciona 2 vezes o valor 
    # da função no ponto médio de cada subintervalo à soma    
    for i in range(2, iteracoes-1, 2):
        soma += 2 * funcao_fx(intervalo_1 + i * h)
    integral = h * soma / 3
    
    return integral

expr_str = input("Digite a expressão matemática da função: ")
expr = sp.sympify(expr_str)

intervalo_1 = float(input("Digite o limite inferior do intervalo: "))
intervalo_2 = float(input("Digite o limite superior do intervalo: "))
iteracoes = int(input("Digite o número de divisões: "))

# Define a função a ser integrada a partir da expressão lida, assim o 'x' não será mais uma string
funcao_fx = lambda x: expr.subs('x', x)

# Calcula a aproximação da integral usando a regra de Simpson
integral = simpson(funcao_fx, intervalo_1, intervalo_2, iteracoes)

# Imprime o resultado
print("\n\nO polinômio lido é:", sp.simplify(expr_str))
print(f"Com intervalos de [{intervalo_1}, {intervalo_2}] com {iteracoes} iterações")
print("Sua aproximação foi de:", sp.simplify(integral))

# Calcula o valor da integral sem usar nenhum método de aproximação
x = sp.Symbol('x')
integral_real = sp.integrate(funcao_fx(x), (x, intervalo_1, intervalo_2))

print("Sua integral real tem valor de:", sp.simplify(integral_real))

erro = integral - integral_real
print("O erro da aproximação foi de:", format(erro, '9f'))