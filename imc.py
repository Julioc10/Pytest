def imc(): 

    massa = int(input('Qual sua massa corporal: '))
    altura = float(input('Qual sua altura: '))
    
    imc_calc = massa / (altura * altura)
    imc_calc_format = "{:.2f}".format(imc_calc)

    print(f'seu imc é {imc_calc_format}')

    if imc_calc < 17:
        print("Muito abaixo do peso")
        return "Muito abaixo do peso"

    elif 17 < imc_calc < 18.49:
        print('Abaixo do peso')
        return 'Abaixo do peso'

    elif 18.5 < imc_calc < 24.99:
        print('peso normal')
        return 'peso normal'

    elif 25 < imc_calc < 29.99:
        print('Acima do peso')
        return 'Acima do peso'

    elif  30 < imc_calc < 34.99:
        print('Obesidade I')
        return 'Obesidade I'

    elif 35 < imc_calc < 34.99:
        print('Obesidade II')
        return 'Obesidade II'

    elif imc_calc > 35:
        print('Obesidade III')
        return 'Obesidade III'
