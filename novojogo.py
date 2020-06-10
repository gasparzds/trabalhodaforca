from modulos.textos import textoinicial
from modulos.entrada_de_informacao import input_usuario
from modulos.tabuleiro import tabuleiro
Errou_letra = True
Ganhou_jogo = False
n_de_errou = 0
base = []
dica = None
palavra_escolhida = None
escolhendo_papeis = 0
desafiante = None
desafiado = None



#BLOCO INICIAL, PEDIDO DE PALAVRA
textoinicial.instrucoes_iniciais()
quem_vai_joga = input_usuario.solicitando_quantidade_players()
if quem_vai_joga == 1:
    nome = input_usuario.solicitando_nome()
    while True:
        print(f'\033[1;30m{nome} você escolheu jogar contra eu, então vou escolher uma palavra pra você adivinhar')
        print('\033[1;30mEntão vou lhe dar uma colher de chá, irei deixar você escolher o tema da palavra')
        print('\033[1;30mPara o tema ANIMAIS digite 1')
        print('\033[1;30mPara o tema OBJETOS digite 2')
        print('\033[1;30mPara o tema CARROS digite 3')
        numero_escolhido = input_usuario.solicitando_tema()
        if numero_escolhido == 1:
            dica = (f'\033[1;30mA dica é: ANIMAL')
            palavra_escolhida = textoinicial.palavras_animais()
        if numero_escolhido == 2:
            dica = (f'\033[1;30mA dica é: OBJETOS')
            palavra_escolhida = textoinicial.palavras_objetos()
        if numero_escolhido == 3:
            dica = (f'\033[1;30mA dica é: CARROS')
            palavra_escolhida = textoinicial.palavras_carros()
        print('\033[1;30mAgora sim já escolhi a palavra!')
        for letra in palavra_escolhida:
            base.append(' - ')
        print('\033[1;30mSua vez agora, tente adivinhar a palavra!')
        print('\033[1;30mVocê pode tentar letra por letra, ou chutar a palavra!')
        print('\033[1;30mMas CUIDADO, se você chutar a palavra e errar, você será enforcado!')

    #BLOCO VERIFICAÇÃO DE ACERTO
        while Ganhou_jogo == False:
            Errou_letra = True
            Ganhou_jogo = False
            tabuleiro.mostrar_tabuleiro(n_de_errou)
            print(base)
            print(dica)
            if n_de_errou == 4:
                print('\033[1;31m FIM DE JOGO')
                print(f'\033[1;31m A palavra escolhida era {palavra_escolhida}')
                break
            letra_palavra_usuario=input_usuario.pedindo_letra()
            if letra_palavra_usuario.isnumeric():
                print('\033[1;31mOpção Invalida!')
                print('\033[1;31mNão aceitamos números!')
            elif len(letra_palavra_usuario) == 2:
                print('\033[1;31mOpção Invalida!')
                print('\033[1;31mDigite uma letra ou uma palavra completa!')
            elif len(letra_palavra_usuario) >= 3:
                    if letra_palavra_usuario == palavra_escolhida:
                        print('\033[1;32mFim de Jogo')
                        print('\033[1;32mVocê acertou a palavra')
                        print('\033[1;32mParabéns')
                        break
                    else:
                        break
            elif len(letra_palavra_usuario) == 1:
                for letradig in palavra_escolhida:
                    if letra_palavra_usuario == letradig:
                        print('\033[1;32mVocê acertou uma letra!')
                        for i, let in enumerate(palavra_escolhida):
                            if palavra_escolhida[i] == letra_palavra_usuario:
                                base[i] = letra_palavra_usuario
                                Errou_letra = False
                if Errou_letra == True:
                    n_de_errou +=1
            for let in base:
                if let == ' - ':
                    Ganhou_jogo = False
            if Ganhou_jogo:
                tabuleiro.mostrar_tabuleiro()
                print(base)
                print('\033[1;31m PARABÉNS VENCEDOR!!!')
                break


        outra_partida = input_usuario.outra_partida()
        if outra_partida == 'n' or outra_partida == 'N':
            print('\033[1;30mAté a proxima!')
            print('\033[1;30mFim da Sessão!')
            break
        else:
            base.clear()
            n_de_errou = 0
            print('\033[1;30mBora outra!')
if quem_vai_joga == 2:
#BLOCO INICIAL PEDINDO NOME DOS JOGADORES

    print('\033[1;30mOlá Jogadores!')
    print('\033[1;30mVocês estão prestes a começar o incrivel Jogo da Forca no curso de ADS!')
    while True:
        jogador1 = input_usuario.solicitando_nome()
        jogador2 = input_usuario.solicitando_nome()
        papeis = input_usuario.escolhendo_papeis()
        papeis_escolhidos = int(papeis)
        if papeis_escolhidos == 1:
            desafiante = jogador1
            desafiado = jogador2
        if papeis_escolhidos == 2:
            desafiante = jogador2
            desafiado = jogador1
        print(f'\033[1;30m{desafiante} em segredo digite uma palavra para seu adversário adivinhar!')
        palavra_escolhida = input_usuario.pedindo_palavra()
        print('\033[1;30mAgora digite uma dica para seu adversário ')
        print('\033[1;30mExemplo: ANIMAL, OBJETO....')
        dica = input_usuario.pedindo_dica()
        for letra in palavra_escolhida:
            base.append(' - ')


    #BLOCO DE VERIFICAÇÃO DE ACERTO
        print(f'\033[1;30mOK, agora é sua vez {desafiado}, você precisa adivinhar a palavra!')
        while Ganhou_jogo == False:
            Errou_letra = True
            Ganhou_jogo = False
            tabuleiro.mostrar_tabuleiro(n_de_errou)
            print(base)
            print(f'A dica é {dica}')

            if n_de_errou == 4:
                print('Acabou o jogo')
                print(f'A palavra era {palavra_escolhida}')
                break
            letra_palavra_usuario = input_usuario.pedindo_letra()
            if letra_palavra_usuario.isnumeric():
                print('\033[1;31mOpção Invalida!')
                print('\033[1;31mNão aceitamos números!')
            elif len(letra_palavra_usuario) == 2:
                print('\033[1;31mOpção Invalida!')
                print('\033[1;31mDigite uma letra ou uma palavra completa!')
            elif len(letra_palavra_usuario) >= 3:
                if letra_palavra_usuario == palavra_escolhida:
                    print('\033[1;32mVocê acertou a palavra')
                    print('\033[1;32mPARABÉNS')
                    break
                else:
                    print('\033[1;33mVocê errou')
                    n_de_errou =4
                    break

            elif len(letra_palavra_usuario) == 1:
                for letradig in palavra_escolhida:
                    if letra_palavra_usuario == letradig:
                        print('\033[1;32mVocê acertou uma letra!')
                        for i, let in enumerate(palavra_escolhida):
                            if palavra_escolhida[i] == letra_palavra_usuario:
                                base[i] = letra_palavra_usuario
                                Errou_letra = False
                if Errou_letra == True:
                    n_de_errou = n_de_errou + 1
                for let in base:
                    if let == ' - ':
                        Ganhou_jogo = False

        print('\033[1;30mQuer revanche? S para SIM e N para NÃO')
        outra_partida = input_usuario.outra_partida()
        if outra_partida == 'n' or outra_partida == 'N':
            print('\033[1;30mAté a proxima!')
            print('\033[1;30mFim da Sessão!')
            break
        else:
            base.clear()
            print('\033[1;30mBora outra!')
