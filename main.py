from contagem import *
from components import digitacao, desenho, dados
from graphics import *


def main():
    # A janela é iniciada
    win = GraphWin("Votação", 770, 555)

    desenho.bemVindo(win)

    desenho.telaBranca(win)

    # Enquanto o botão encerra não for digitado
    encerra = 0
    while encerra != 1:
        votNum1 = Rectangle(Point(140, 220), Point(180, 262))
        votNum1.draw(win)
        votNum2 = Rectangle(Point(190, 220), Point(230, 262))
        votNum2.draw(win)
        prescheck = 0
        govcheck = 0
        # Enquanto a tela do presidente não acabar
        while prescheck != 1:
            prescheck = 0
            votpres = Text(Point(185, 190), 'Presidente')
            votpres.draw(win)
            votpres.setSize(20)
            # Os numeros são desenhados dentro dos retangulos
            votodig = ''
            dicvot = {}
            c = 1
            for item in [votNum1, votNum2]:
                num = digitacao.digitado(win)
                if (num != 'None') and (num != 'confirma') and (num != 'branco') and (num != 'corrige') and (num != 'encerra'):
                    votodig += num
                    x = item.getCenter()
                    dicvot['votnum' + str(c)] = Text(x, str(num))
                    dicvot['votnum' + str(c)].setSize(20)
                    dicvot['votnum' + str(c)].setTextColor('Red')
                    dicvot['votnum' + str(c)].draw(win)
                    c += 1
            # Verificação se o numero digitado corresponde ao Lula
            if votodig == dados.numero_precandidato1:
                # Se sim, os dados são desenhados
                pres1 = Image(Point(345, 175),
                              f'src/{dados.foto_precandidato1}')
                pres1.draw(win)
                pres1nome = Text(
                    Point(345, 255), f'{dados.nome_precandidato1}')
                pres1nome.setSize(14)
                pres1nome.draw(win)
                pres1num = Text(Point(345, 275),
                                f'{dados.numero_precandidato1}')
                pres1num.setSize(14)
                pres1num.draw(win)
            # Verificação se o numero digitado corresponde ao Bolsonaro
            if votodig == dados.numero_precandidato2:
                # Se sim, os dados são desenhados
                pres2 = Image(Point(345, 195),
                              f'src/{dados.foto_precandidato2}')
                pres2.draw(win)
                pres2nome = Text(
                    Point(345, 285), f'{dados.nome_precandidato2}')
                pres2nome.setSize(14)
                pres2nome.draw(win)
                pres2num = Text(Point(345, 310),
                                f'{dados.numero_precandidato2}')
                pres2num.setSize(14)
                pres2num.draw(win)
            # Verificação se o botão Branco é clickado
            if digitacao.digitado(win) == 'branco':
                # Add cont voto presBranco
                addVotoPres('branco')
                texBranco = Text(Point(345, 215), 'Voto em Branco')
                texBranco.setSize(14)
                texBranco.draw(win)

                prescheck += 1
            # Verificação se o botão Confirma é clickado
            if digitacao.digitado(win) == 'confirma':
                if votodig == dados.numero_precandidato1:
                    # Add cont voto pres1
                    addVotoPres('cand1')
                    try:
                        pres1.undraw()
                        pres1nome.undraw()
                        pres1num.undraw()
                    except:
                        pass
                elif votodig == dados.numero_precandidato2:
                    # Add cont voto pres2
                    addVotoPres('cand2')
                    try:
                        pres2.undraw()
                        pres2nome.undraw()
                        pres2num.undraw()
                    except:
                        pass
                else:
                    # Add cont voto presNulo
                    addVotoPres('nulo')
                    pass
                # Os numeros desenhados no retangulo são apagados
                dicvot['votnum1'].undraw()
                dicvot['votnum2'].undraw()
                prescheck += 1
            # Verificação se o botão Corrige é clickado
            if digitacao.digitado(win) == 'corrige':
                # Os numeros desenhados no retangulo e os possiveis dados do candidato são apagados
                try:
                    pres1.undraw()
                    pres1nome.undraw()
                    pres1num.undraw()
                except:
                    pass
                try:
                    pres2.undraw()
                    pres2nome.undraw()
                    pres2num.undraw()
                except:
                    pass
                dicvot['votnum1'].undraw()
                dicvot['votnum2'].undraw()
                pass
            votpres.undraw()
            try:
                texBranco.undraw()
            except:
                pass
        # Enquanto a tela do presidente não acabar
        while govcheck != 1:
            govcheck = 0
            votgov = Text(Point(185, 190), 'Governador')
            votgov.draw(win)
            votgov.setSize(20)
            # Os numeros são desenhados dentro dos retangulos
            votodig = ''
            dicvot = {}
            c = 1
            for item in [votNum1, votNum2]:
                num = digitacao.digitado(win)
                if (num != 'None') and (num != 'confirma') and (num != 'branco') and (num != 'corrige') and (num != 'encerra'):
                    votodig += num
                    x = item.getCenter()
                    dicvot['votnum' + str(c)] = Text(x, str(num))
                    dicvot['votnum' + str(c)].setSize(20)
                    dicvot['votnum' + str(c)].setTextColor('Red')
                    dicvot['votnum' + str(c)].draw(win)
                    c += 1
            # Verificação se o numero digitado corresponde ao Onyx
            if votodig == dados.numero_govcandidato1:
                # Se sim, os dados são desenhados
                gov1 = Image(Point(345, 175),
                             f'src/{dados.foto_govcandidato1}')
                gov1.draw(win)
                gov1nome = Text(Point(345, 250),
                                f'{dados.nome_govcandidato1}')
                gov1nome.setSize(14)
                gov1nome.draw(win)
                gov1num = Text(Point(345, 275),
                               f'{dados.numero_govcandidato1}')
                gov1num.setSize(14)
                gov1num.draw(win)
            # Verificação se o numero digitado corresponde ao Leite
            if votodig == dados.numero_govcandidato2:
                # Se sim, os dados são desenhados
                gov2 = Image(Point(345, 195),
                             f'src/{dados.foto_govcandidato2}')
                gov2.draw(win)
                gov2nome = Text(Point(345, 285),
                                f'{dados.nome_govcandidato2}')
                gov2nome.setSize(14)
                gov2nome.draw(win)
                gov2num = Text(Point(345, 310),
                               f'{dados.numero_govcandidato2}')
                gov2num.setSize(14)
                gov2num.draw(win)
            # Verificação se o botão Branco é clickado
            if digitacao.digitado(win) == 'branco':
                # Add cont voto govBranco
                addVotoGov('branco')
                texBranco = Text(Point(345, 215), 'Voto em Branco')
                texBranco.setSize(14)
                texBranco.draw(win)

                govcheck += 1
            # Verificação se o botão Confirma é clickado
            if digitacao.digitado(win) == 'confirma':
                if votodig == dados.numero_govcandidato1:
                    # Add cont voto gov1
                    addVotoGov('cand1')
                    try:
                        gov1.undraw()
                        gov1nome.undraw()
                        gov1num.undraw()
                    except:
                        pass
                elif votodig == dados.numero_govcandidato2:
                    # Add cont voto gov2
                    addVotoGov('cand2')
                    try:
                        gov2.undraw()
                        gov2nome.undraw()
                        gov2num.undraw()
                    except:
                        pass
                else:
                    # Add cont voto govNulo
                    addVotoGov('nulo')
                    pass
                # Os numeros desenhados no retangulo são apagados
                dicvot['votnum1'].undraw()
                dicvot['votnum2'].undraw()
                govcheck += 1
            # Verificação se o botão Corrige é clickado
            if digitacao.digitado(win) == 'corrige':
                # Os numeros desenhados no retangulo e os possiveis dados do candidato são apagados
                try:
                    gov1.undraw()
                    gov1nome.undraw()
                    gov1num.undraw()
                except:
                    pass
                try:
                    gov2.undraw()
                    gov2nome.undraw()
                    gov2num.undraw()
                except:
                    pass
                dicvot['votnum1'].undraw()
                dicvot['votnum2'].undraw()
                pass
            votgov.undraw()
            try:
                texBranco.undraw()
            except:
                pass
        try:
            votNum1.undraw()
            votNum2.undraw()
        except:
            pass
        # Verificação se o botão Encerra é clickado
        if digitacao.digitado(win) == 'encerra':
            encerra = 1
    # A tela da senha é desenhado
    recNum1 = Rectangle(Point(160, 220), Point(200, 262))
    recNum1.draw(win)
    recNum2 = Rectangle(Point(210, 220), Point(250, 262))
    recNum2.draw(win)
    recNum3 = Rectangle(Point(260, 220), Point(300, 262))
    recNum3.draw(win)
    recNum4 = Rectangle(Point(310, 220), Point(350, 262))
    recNum4.draw(win)
    senhaTexto = Text(Point(255, 190), 'SENHA')
    senhaTexto.setSize(24)
    senhaTexto.draw(win)

    senhaConf = 0
    # Enquanto a senha for incorreta
    while senhaConf != 1:
        # Reseta o conteudo com a senha padrão
        with open('src/senha.txt', 'w+') as file:
            file.write('0000\n')
        try:
            d['num1'].undraw()
            d['num2'].undraw()
            d['num3'].undraw()
            d['num4'].undraw()
        except:
            pass
        # Os numeros digitados são desenhados nos retangulos
        senhadig = ''
        d = {}
        c = 1
        for item in [recNum1, recNum2, recNum3, recNum4]:
            num = digitacao.digitado(win)
            if (num != 'None') and (num != 'confirma') and (num != 'branco') and (num != 'corrige') and (num != 'encerra'):
                senhadig += num
                x = item.getCenter()
                d['num' + str(c)] = Text(x, str(num))
                d['num' + str(c)].setSize(20)
                d['num' + str(c)].setTextColor('Red')
                d['num' + str(c)].draw(win)
                c += 1
            else:
                break
        senhadig += '\n'
        # A senha digitada é adicionada ao arquivo junto com a senha padrão
        with open('src/senha.txt', 'a+') as file1:
            file1.write(str(senhadig))
        # A senhas são comparadas
        with open('src/senha.txt', 'r+') as file2:
            data = file2.readlines()
        # Se forem iguais, acaba o while
        if data[0] == data[1]:
            senhaConf = 1
            with open('src/senha.txt', 'w+') as file3:
                file3.write('0000\n')

        # Os votos digitados até agora serão contabilizados

        ContVotos()


main()
