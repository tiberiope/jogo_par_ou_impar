def calcular_par_impar(num1, num2):
    num1 = num1
    num2 = num2
    soma = num1 + num2
    resultado = soma % 2
    par_impar = ''

    if resultado == 0:
        par_impar = 'par'
    else:
        par_impar = 'par_impar'

    return par_impar