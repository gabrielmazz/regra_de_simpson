# Implementação da Regra do Trapézio

## Introdução

A regra de Simpson é um método numérico de integração que utiliza parábolas para aproximar a função a ser integrada. A ideia é aproximar a função a cada dois pontos do intervalo de integração por uma parábola. Dessa forma, a área sob a curva é aproximada por áreas sob essas parábolas.

A fórmula da regra de Simpson é dada por:

$\int_{a}^{b}f(x)dx \approx \frac{b-a}{6}\left[f(a) + 4f\left(\frac{a+b}{2}\right) + f(b)\right]$

onde $f(x)$ é a função a ser integrada, $a$ e $b$ são os limites de integração e o número de divisões do intervalo deve ser par. A implementação da regra de Simpson envolve o cálculo do valor de $h$, que é a largura de cada subintervalo do intervalo de integração sendo $h = \frac{b-a}{n}$

## Função principal

A função principal do programa é `simpson`. Ela recebe como parâmetros a função a ser integrada (`funcao_fx`), os limites de integração (`intervalo_1` e `intervalo_2`) e o número de iterações (`iteracoes`). A função `simpson` retorna a aproximação da integral da função.

A implementação da regra de Simpson envolve a soma de valores da função nos pontos médios de cada subintervalo do intervalo de integração. A quantidade de subintervalos é determinada pelo número de iterações (`iteracoes`).

```python
def simpson(funcao_fx, intervalo_1, intervalo_2, iteracoes)
```

## Entrada de dados

O programa inicia solicitando ao usuário a expressão matemática da função que deseja integrar, que deve ser digitada em uma única linha e ser compatível com a biblioteca sympy. A expressão é lida como uma string e, em seguida, convertida em uma expressão matemática manipulável pela biblioteca `sympy`. Em seguida, o programa solicita ao usuário os limites do intervalo de integração, onde o primeiro intervalo deve ser digitado antes do segundo intervalo, e o número de subintervalos desejado para calcular a integral aproximada usando a regra de Simpson.

## Saída de dados

O programa imprime o valor aproximado da integral definida da função utilizando a regra do trapézio. Além disso, o programa também calcula o valor real da integral e o erro cometido na aproximação.

## Execução

Para rodar o aplicativo em Python, basta executar o código em qualquer ambiente que suporte a linguagem Python 3. 

```bash
python3 regra_do_trapezio.py
```

O código utiliza as bibliotecas `sympy` e `numpy`, portanto, é necessário ter essas bibliotecas instaladas no ambiente em que o código será executado.