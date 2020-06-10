def solicitando_nome():
    while True:
        usuario = input('\033[1;30mDigite seu nome: ')
        if usuario.isnumeric():
            print('\033[1;31mSeu nome não pode ser números')
            print('\033[1;31mTente novamente')
        elif len(usuario) <= 1:
            print('\033[1;31mSeu nome não pode ser apenas um caracter!')
            print('\033[1;31mTente novamente')
        else:
            usuario = usuario.upper()
            return usuario

def solicitando_quantidade_players():
    while True:
        quem_vai_jogar = input()
        if not quem_vai_jogar.isnumeric():
            print('\033[1;31mAceitamos somente 1 ou 2')
            print('\033[1;31mTente novamente')
        else:
            quem_vai_jogar =int(quem_vai_jogar)
            if quem_vai_jogar == 1:
                print('\033[1;30mOk, será VOCÊ contra EU!')
                print('\033[1;30mSe prepare!')
                return quem_vai_jogar
            elif quem_vai_jogar == 2:
                print('\033[1;30mOk, será VOCÊ seu AMIGO!')
                print('\033[1;30mSe prepare!')
                return quem_vai_jogar
            else:
                print('\033[1;31mOpção Invalida!')
                print('\033[1;31mTente novamente')

def solicitando_tema():
    while True:
        numero_escolhido = input('\033[1;30mDigite 1 ou 2 ou 3: ')
        if not numero_escolhido.isnumeric():
            print('\033[1;31mOpção Invalida!')
            print('\033[1;31mDigite apenas número!')
        else:
            numero_escolhido = int(numero_escolhido)
            if numero_escolhido >= 4:
                print('\033[1;31mOpção Invalida')
                print('\033[1;31mTemos apenas 3 opções!')
            if numero_escolhido == 1:
                print('\033[1;30mOK, estou escolhendo uma palavra com o tema ANIMAL....' )
                return numero_escolhido
            if numero_escolhido == 2:
                print('\033[1;30mOK, estou escolhendo uma palavra com o tema OBJETO....' )
                return numero_escolhido
            if numero_escolhido == 3:
                print('\033[1;30mOK, estou escolhendo uma palavra com o tema CARRO....' )
                return numero_escolhido

def pedindo_letra():
    while True:
        letra_escolhida = input('\033[1;30mDigite uma letra: ')
        letra_escolhida = letra_escolhida.upper()
        if letra_escolhida.isnumeric():
            print('\033[1;31mNão aceitamos números, apenas letras ou palavras completas!')
            print('\033[1;31mTente novamente!')
        elif len(letra_escolhida) == 2:
            print('\033[1;31mNão exite palavra de 2 letras, ou você digita 1 letra ou a palavra completa!')
            print('\033[1;31mTente Novamente')
        elif len(letra_escolhida) == 1:
            print('\033[1;30mVocê acabou de chutar uma letra!')
            print('\033[1;30mEstou vendo se você acertou.....')
            return letra_escolhida
        elif len(letra_escolhida) >= 3:
            print('\033[1;30mVocê acabou de chutar uma palavra!')
            print('\033[1;30mEstou vendo se você acertou.....')
            return letra_escolhida

        else:
            print('\033[1;30mERRO!')

def escolhendo_papeis():
    print('\033[1;30mPrimeiramente preciso saber, quem vai ser o DESAFIANTE e o DESAFIADO.')
    print('\033[1;30mPara o PLAYER1 ser o DESAFIANTE e o PLAYER2 ser o DESAFIADO digite 1')
    print('\033[1;30mPara o PLAYER2 ser o DESAFIANTE e o PLAYER1 ser o DESAFIADO digite 2')
    while True:
        escolhendo_papeis = input('Digite 1 ou 2: ')
        if escolhendo_papeis == '1' or escolhendo_papeis == '2':
            escolhendo_papeis = int(escolhendo_papeis)
            print('Processando')
            return escolhendo_papeis
        else:
            print('ERRO')


def pedindo_palavra():
    while True:
        palavra_escolhida = input()
        if len(palavra_escolhida) <= 2:
            print('\033[1;31mVocê precisa digitar uma palavra completa')
            print('\033[1;31mTente novamente')
        elif palavra_escolhida.isnumeric():
            print('\033[1;31mVocê precisa digitar uma palavra!')
            print('\033[1;31mTente novamente!')
        else:
            palavra_escolhida = palavra_escolhida.upper()
            return palavra_escolhida

def pedindo_dica():
    while True:
        dica = input()
        if dica.isnumeric():
            print('\033[1;31mVocê precisa digitar uma palavra!')
            print('\033[1;31mTente novamente!')
        else:
            dica = dica.upper()
            return dica


def outra_partida():
    while True:
        outro_jogo=input('\033[1;30mDigite S ou N! ')
        if (outro_jogo == 'N') or (outro_jogo == 'n') or (outro_jogo == 'S') or (outro_jogo == 's'):
            return outro_jogo
        else:
            print('\033[1;31mOpção Invalida!')
            print('\033[1;31mTente novamente!')

