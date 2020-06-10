def instrucoes_iniciais():
    print('\033[1;30m Olá Jogador!')
    print('\033[1;30mVocê está prestes a começar o incrivel Jogo da Forca no curso de ADS!')
    print('\033[1;30mPrimeiramente preciso saber, você quer jogar contra eu ou contra um amigo?')
    print('\033[1;30mDigite 1 para PLAYER vs PC')
    print('\033[1;30mDigite 2 para PLAYER vs PLAYER')

def palavras_animais():
    import random
    lista = ['BALEIAS', 'CACHORROS', 'CAVALOS', 'COBRA','CROCODILO', 'ELEFANTES',
             'GAMBA', 'GATOS','GOLFINHO', 'LEOES', 'GIRAFA', 'LOBOS', 'MACACOS',
             'OVELHA', 'PAPAGAIO', 'POLVO', 'POMBOS','RINOCERONTES', 'TARTARUGAS']
    palavra_escolhida= random.choice(lista)
    return palavra_escolhida




def palavras_objetos():
    import random
    lista = ['DESPERTADOR', 'CAMA', 'ESTANTE', 'XICARA','GARFO', 'COPO',
             'ESFREGAO', 'CANECA','PRATO', 'VASO', 'CADEIRA' ,'COMPUTADOR', 'SOFA' ,
             'TAPETE', 'MESA', 'TELEFONE', 'DESODORANTE','ESPELHO','CHUVEIRO']
    palavra_escolhida= random.choice(lista)
    return palavra_escolhida



def palavras_carros():
    import random
    lista = ['CHEVROLET', 'VOLKSWAGEN', 'FIAT', 'RENAULT','FORD', 'TOYOTA',
             'HYUNDAI', 'JEEP','HONDA', 'NISSAN', 'CITROEN','MITSUBISHI','PEUGEOT',
             'CHERY', 'BMW', 'MERCEDES', 'KIA','AUDI', 'VOLVO']
    palavra_escolhida= random.choice(lista)
    return palavra_escolhida
