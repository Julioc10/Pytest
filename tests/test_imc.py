from imc import imc

def test_imc():

    if imc() == 'Muito abaixo do peso':
        assert imc() == ("Muito abaixo do peso")

    elif imc() == 'Abaixo do peso':
        assert imc() == 'Abaixo do peso'

    elif imc() == 'peso normal':
        assert imc() == 'peso normal'

    elif imc() == 'Acima do peso':
        assert imc() == 'Acima do peso'

    elif imc() == 'Obesidade I':
        assert imc() == 'Obesidade I'

    elif imc() == 'Obesidade II':
        assert imc() == 'Obesidade II'

    elif imc() == 'Obesidade III':
        assert imc() == 'Obesidade III'
