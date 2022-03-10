import operacoes


def cabecalho(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)

cabecalho ('VOCÊ ESTÁ USANDO A CALCULADORA BÁSICA')
cabecalho ('Guia de usuário:')

print('''FUNCõES:
  --> ADIÇÃO [ + ] = Soma o primeiro número digitado com o segundo número digitado.    
  --> SUBTRAÇÃO [ - ] = Subtrai o primeiro número digitado pelo segundo número digitado.
  --> MULTIPLICAÇÃO [ * ]= Multiplica os dois números digitados.
  --> DIVISÃO [ / ] = Divide o primeiro número digitado pelo segundo número digitado.
  ''')

cabecalho('INICIANDO...')

while True:

    while True:
        try:
            print('-> Primeiro número: ', end=' ')
            n1 = float(input())
        except ValueError:
            print('ERRO: APENAS NÚMEROS.')
        else:
            break
    while True:
        print('-> Operação: ', end=' ')
        op = input()
        if op not in '/*-+':
            print('ERRO: OPERAÇÃO INVÁLIDA.')
        else:
            break
    while True:
        try:
            print('-> Segundo número: ', end=' ')
            n2 = float(input())
        except ValueError:
            print('ERRO: APENAS NÚMEROS.')
        else:
            break

    if op == '+':
        print(n1, op, n2, sep=' ', end=' ')
        print(f'= {operacoes.soma(n1, n2)}')
    if op == '-':
        print(n1, op, n2, sep=' ', end=' ')
        print(f'= {operacoes.subtracao(n1, n2)}')
    if op == '/':
        print(n1, op, n2, sep=' ', end=' ')
        print(f'= {operacoes.divisao(n1, n2)}')
    if op == '*':
        print(n1, op, n2, sep=' ', end=' ')
        print(f'= {operacoes.multiplicacao(n1, n2)}')
