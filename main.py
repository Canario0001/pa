#!/usr/bin/env python3
from fractions import Fraction
from numpy import arange

def header(num):
    print('┅'*num)

def muda_virgula(num):
    return num.replace(',', '.')

def a_um(a_n, n, r):
    return a_n - (n - 1) * r

def a_n(a_1, n, r):
    return a_1 + (n - 1) * r

def razao(a_n, a_1, n):
    return (a_n - a_1) / (n - 1)

def pos1(a_n, a_1, r):
    return ((a_n - a_1) / r) + 1

def pos2(sn, a_1, a_n):
    return (2 * sn) / (a_1 + a_n)

def soma_p1(a_1, a_n, n):
    return ((a_1 + a_n) * n) / 2

def soma_p2(a_1, r, n):
    return ((2 * a_1 + (n - 1) * r) * n ) / 2

def medio1(a_1, a_n):
    return (a_1 + a_n) / 2

def medio2(a_1, n, r):
    return (2 * a_1 + (n - 1) * r) / 2

def lista():
    print('\nA lista estará da seguinte maneira:\nabreviação: o que significa\nDigite no formato abreviação:valor\n')
    print('a1: Primeiro termo da PA')
    print('r: Razão da PA')
    print('an: n termo da PA')
    print('n: Posição do an na PA')
    print('sn: Soma dos n primeiros termos da PA')
    print('am: Termo médio da PA')

def contas(a1=None, r=None, an=None, n=None, sn=None, am=None):
    err = None
    
    for _ in range(2):
        if a1 is None:
            try:
                a1 = a_um(an, n, r)
            except (ValueError, TypeError):
                a1 = err
        
        if r is None:
            try:
                r = razao(an, a1, n)
            except (ValueError, TypeError):
                r = err

        if an is None:
            try:
                an = a_n(a1, n, r)
            except (ValueError, TypeError):
                an = err
        
        if n is None:
            try:
                n = pos1(an, a1, r)
            except (ValueError, TypeError):
                try:
                    n = pos2(sn, a1, an)
                except (ValueError, TypeError):
                    n = err

        if sn is None:
            try:
                sn = soma_p1(a1, an, n)
            except (ValueError, TypeError):
                try:
                    sn = soma_p2(a1, r, n)
                except (ValueError, TypeError):
                    sn = err

        if am is None:
            try:
                am = medio1(a1, an)
            except (ValueError, TypeError):
                try:
                    am = medio2(a1, n, r)
                except (ValueError, TypeError):
                    am = err

    try:
        if r != 0:
            pa = tuple(Fraction(i) for i in arange(a1, an+1 if an > 0 else an-1, r))
            pa = tuple(i.limit_denominator() for i in pa)
        else:
            pa = [a1] * n
    except TypeError:
        print('Você não informou informações o suficiente ou a1, an, ou r são números reais e não inteiros.')
        exit()

    if r == 0:
        classe = 'constante'
    elif r > 0:
        classe = 'crescente'
    else:
        classe = 'decrescente'

    result = {
        'a1': a1,
        'an': an,
        'am': am,
        'n': n,
        'r': r,
        'pa': pa,
        'tamanho': len(pa),
        'sn': sn if sn else sum(pa),
        'menor': min(pa),
        'maior': max(pa),
        'class': classe,
    }

    return result

def anotar(nome, resultado):
    with open(f'{nome}.txt', 'w', encoding='utf-8') as f:
        f.write(f'Resultados\n\na1: {resultado["a1"]}\n')
        f.write(f'an: {resultado["an"]}\nn: {resultado["n"]}\n')
        f.write(f'razão: {resultado["r"]}\n')
        f.write('PA: (', )
        for i in resultado["pa"]:
            f.write(f'{i}, ')
        f.write('\b\b)\n')
        f.write(f'tamanho da PA: {resultado["tamanho"]} termos\n')
        f.write(f'soma da PA: {resultado["sn"]}\n')
        f.write(f'menor termo da PA: {resultado["menor"]}\n')
        f.write(f'maior termo da PA: {resultado["maior"]}\n')
        f.write(f'classificação da PA: {resultado["class"]}\n')

def main():
    header(45)
    print('  Calculadora de Progressão Aritmética!')
    header(45)
    print('\nDeseja ver a lista de abreviações ou quer começar agora?\n')
    print('[0] - Ver a lista de abreviações\n[1] - Começar sem ver a lista\n')
    choice = int(input('>>> '))
    if choice == 0: lista()
    elif choice == 1: pass
    else:
        print('Insira um valor válido. Tente novamente.')
        exit()
    
    print('\nDigite as informações que você possui de acordo com a lista de abreviações. Digite "q" se tiver terminado.\n')
    
    info = {
        'a1': None,
        'r': None,
        'an': None,
        'am': None,
        'n': None,
        'sn': None
    }

    while True:
        comp = input('>>> ').strip().lower()

        if comp == 'q':
            break

        key, value = comp.split(':')

        if ',' in value:
            value = muda_virgula(value)

        if key in info:
            info[key] = Fraction(value)
            continue

        print('Digite uma informação válida!')

    info = contas(**info)
    print('\n')
    header(35)
    print('  Resultados')
    header(35)
    print()
    print(f'  a1: {info["a1"]}')
    print(f'  an: {info["an"]}')
    print(f'  am: {info["am"]}')
    print(f'  razão: {info["r"]}')
    print(f'  n: {info["n"]}')
    print('  PA: (', end='')
    print(*info["pa"], sep=', ', end='')
    print(')')
    print(f'  tamanho da PA: {info["tamanho"]} termos')
    print(f'  soma da PA: {info["sn"]}')
    print(f'  menor termo da PA: {info["menor"]}')
    print(f'  maior termo da PA: {info["maior"]}')
    print(f'  classificação da PA: {info["class"]}')
    print('\n\nVocê quer escrever os resultados num arquivo de texto?\n\n[0] - Sim\n[1] - Não\n')
    choice = int(input('>>> ').strip())
    if choice == 0:
        print('\nQual será o nome do arquivo?\n')
        nome = input('>>> ').strip()
        anotar(nome, info)
        print(f'\nResultados salvos no arquivo {nome}.txt!')
    elif choice == 1: pass
    else: print('Opção inválida. Operação cancelada.')

    print('\nObrigado por usar!\nFeito por: Cristian (aka Canário)')

if __name__ == '__main__':
    main()
