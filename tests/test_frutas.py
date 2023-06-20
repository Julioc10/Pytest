from frutas import fruta

def test():
    if fruta() == 'banana':
        assert fruta() == 'banana'

    elif fruta() == 'goiaba':
        assert fruta() == 'goiaba' 

    else:
        assert fruta() == 'manga'

