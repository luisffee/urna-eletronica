from graphics import *

# Depreciado
'''def confEncerra(win):

    # Confere se o botão de encerrar foi apertado
    click = win.getMouse()
    if (625 < click.getX() < 674) and (396 < click.getY() < 444):
        # Confere se a senha bate
        with open('src/senha.txt', 'r+') as file:
            data = file.readlines()
            try:
                if data[0] == data[1]:
                    # contagem.votoCont(win)
                    print('A senha está correta!')
                    with open('src/senha.txt', 'w+') as file1:
                        file1.write('0000\n')
                    win.close()
                    return True
                else:
                    print(
                        f'A senha padrão é: {data[0]} e a senha digitada é: {data[1]}\n')
                    print(f'Conteúdo arquivo: {data}')
                    with open('src/senha.txt', 'w+') as file1:
                        file1.write('0000\n')
                    return None
            except:
                return False
    else:
        return False'''

# Depreciado
'''def confVoto(win):
    if ((confVotoGov(win) == 1) or (confVotoGov(win) == 2) or (confVotoGov(win) == 3)):
        return True
    elif ((confVotoPres(win) == 1) or (confVotoPres(win) == 2) or (confVotoPres(win) == 3)):
        return True
    else:
        return False'''

# Depreciado
'''def confVotoPres(win):
    with open('src/numvoto.txt', 'r+') as file:
        numvoto = file.readlines()
        try:
            if numvoto[0] == (dados.numero_precandidato1):
                # Contabilizar o voto
                desenho.candPres(win)
                with open('src/numvoto.txt', 'w+') as file1:
                    file1.write('')
                return 1
            elif numvoto[0] == (dados.numero_precandidato2):
                # Contabilizar o voto
                desenho.candPres(win)
                with open('src/numvoto.txt', 'w+') as file1:
                    file1.write('')
                return 2
            elif numvoto[0] == 'branco':
                # Contabilizar o voto como branco
                with open('src/numvoto.txt', 'w+') as file1:
                    file1.write('')
                return 3

        except:
            with open('src/numvoto.txt', 'w+') as file1:
                file1.write('')
            return False'''

# Depreciado
'''def confVotoGov(win):
    with open('src/numvoto.txt', 'r+') as file:
        numvoto = file.readlines()
        try:
            if numvoto[0] == (dados.numero_govcandidato1):
                # Contabilizar o voto
                desenho.candGov(win)
                with open('src/numvoto.txt', 'w+') as file1:
                    file1.write('')
                return 1
            elif numvoto[0] == (dados.numero_govcandidato2):
                # Contabilizar o voto
                desenho.candGov(win)
                with open('src/numvoto.txt', 'w+') as file1:
                    file1.write('')
                return 2
            elif numvoto[0] == 'branco':
                # Contabilizar o voto como branco
                with open('src/numvoto.txt', 'w+') as file1:
                    file1.write('')
                return 3

        except:
            with open('src/numvoto.txt', 'w+') as file1:
                file1.write('')
            return False'''
