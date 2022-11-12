from graphics import *
from time import sleep


def bemVindo(win):
    # A tela de inicio é desenhada
    urna = Image(Point(385, 277), 'src/urna.png')
    urna.draw(win)
    encerra = Text(Point(560, 425), 'ENCERRAR')
    encerra.setSize(14)
    encerra.draw(win)
    encerra1 = Image(Point(650, 420), 'src/bt.gif')
    encerra1.draw(win)
    tbc = telaBranca(win)
    bemvindo = Text(tbc, 'Bem Vindo à votação!')
    bemvindo.setSize(24)
    bemvindo.draw(win)

    time.sleep(2.5)

    bemvindo.undraw()

    bemvindo2 = Text(tbc, 'Você poderá votar em \nGovernador e Presidente')
    bemvindo2.setSize(20)
    bemvindo2.draw(win)

    time.sleep(2.5)

    bemvindo2.undraw()


def telaBranca(win):
    telab = Rectangle(Point(95, 106), Point(425, 355))
    telab.draw(win)
    telab.setFill('white')
    center = telab.getCenter()
    return center


# Depreciado
'''def init(win):

    votPres = Text(Point(185, 190), 'Presidente')
    votPres.draw(win)
    votPres.setSize(20)
    global votGov
    if ((verificacao.confVotoGov(win) == 1) or (verificacao.confVotoGov(win) == 2) or (verificacao.confVotoGov(win) == 3)):
        votPres.undraw()
        votGov = Text(Point(185, 190), 'Governador')
        votGov.draw(win)
        votGov.setSize(20)

    votNum1 = Rectangle(Point(140, 220), Point(180, 262))
    votNum1.draw(win)
    votNum2 = Rectangle(Point(190, 220), Point(230, 262))
    votNum2.draw(win)

    votodig = ''
    dicvot = {}
    c = 1
    for item in [votNum1, votNum2]:
        num = digitacao.digitado(win)
        if (num != 'None') and (num != 'confirma') and (num != 'branco') and (num != 'corrige'):
            votodig += num
            x = item.getCenter()
            dicvot['votnum' + str(c)] = Text(x, str(num))
            dicvot['votnum' + str(c)].setSize(20)
            dicvot['votnum' + str(c)].setTextColor('Red')
            dicvot['votnum' + str(c)].draw(win)
            c += 1
        else:
            break

    if digitacao.digitado(win) == 'confirma':
        try:
            votPres.undraw()
            dicvot['votnum1'].undraw()
            dicvot['votnum2'].undraw()
        except:
            pass
        try:
            votGov.undraw()
            dicvot['votnum1'].undraw()
            dicvot['votnum2'].undraw()
        except:
            pass
    with open('src/numvoto.txt', 'w+') as file1:
        file1.write(str(votodig))'''

# Depreciado
'''def senha(win):
    telaBranca(win)
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

    while verificacao.confEncerra(win) != True:
        senhadig = ''
        d = {}
        c = 1
        for item in [recNum1, recNum2, recNum3, recNum4]:
            num = digitacao.digitado(win)
            if (num != 'None') and (num != 'confirma') and (num != 'branco') and (num != 'corrige'):
                senhadig += num
                print(num)
                x = item.getCenter()
                d['num' + str(c)] = Text(x, str(num))
                d['num' + str(c)].setSize(20)
                d['num' + str(c)].setTextColor('Red')
                d['num' + str(c)].draw(win)
                c += 1
            else:
                break
        senhadig += '\n'
        print(senhadig)
        with open('src/senha.txt', 'a+') as file1:
            file1.write(str(senhadig))
        if verificacao.confEncerra(win) == None:
            d['num1'].undraw()
            d['num2'].undraw()
            d['num3'].undraw()
            d['num4'].undraw()'''

# Depreciado
'''def candPres(win):
    with open('src/numvoto.txt', 'r+') as file:
        numvoto = file.readlines()
    if numvoto[0] == (dados.numero_precandidato1):
        pres1 = Image(Point(345, 175), 'src/lula.gif')
        pres1.draw(win)
        pres1nome = Text(Point(345, 260), 'Luis Inacio Lula')
        pres1nome.setSize(14)
        pres1nome.draw(win)
        pres1num = Text(Point(345, 285), '13')
        pres1num.setSize(14)
        pres1num.draw(win)
        time.sleep(2)
        pres1.undraw()
        pres1nome.undraw()
        pres1num.undraw()
    elif numvoto[0] == (dados.numero_precandidato2):
        pres2 = Image(Point(345, 175), 'src/bolsonaro.gif')
        pres2.draw(win)
        pres2nome = Text(Point(345, 250), 'Jair Bolsonaro')
        pres2nome.setSize(14)
        pres2nome.draw(win)
        pres2num = Text(Point(345, 275), '17')
        pres2num.setSize(14)
        pres2num.draw(win)
        time.sleep(2)
        pres2.undraw()
        pres2nome.undraw()
        pres2num.undraw()

    else:
        print('deu errado')'''

# Depreciado
'''def candGov(win):
    with open('src/numvoto.txt', 'r+') as file:
        numvoto = file.readlines()
    if numvoto[0] == (dados.numero_govcandidato2):
        gov2 = Image(Point(345, 175), 'src/leite.gif')
        gov2.draw(win)
        gov2nome = Text(Point(345, 250), 'Eduardo Leite')
        gov2nome.setSize(14)
        gov2nome.draw(win)
        gov2num = Text(Point(345, 275), '45')
        gov2num.setSize(14)
        gov2num.draw(win)
        time.sleep(2)
        gov2.undraw()
        gov2nome.undraw()
        gov2num.undraw()
    elif numvoto[0] == (dados.numero_govcandidato1):
        gov1 = Image(Point(345, 195), 'src/onyx.gif')
        gov1.draw(win)
        gov1nome = Text(Point(345, 285), 'Onyx Lorenzoni')
        gov1nome.setSize(14)
        gov1nome.draw(win)
        gov1num = Text(Point(345, 310), '22')
        gov1num.setSize(14)
        gov1num.draw(win)
        time.sleep(2)
        gov1.undraw()
        gov1nome.undraw()
        gov1num.undraw()
    else:
        print('deu errado')'''
