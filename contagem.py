from components import dados


def addVotoPres(tipo):
    with open('src/votos.txt', 'r+') as file1:
        data1 = file1.read()
        data2 = data1.split(';')
        data2 = data2[0]
        data2 = data2.split('\n')

        if tipo == 'cand1':
            b = data2[0]
            c = b.split('-')
            b1 = str(b[:-1])
            v = int(c[1])
            v += 1
            b1 += str(v)

            new = str(data1).replace(b, b1)
            with open('src/votos.txt', 'w+') as file2:
                file2.write(new)

        if tipo == 'cand2':
            b = data2[1]
            c = b.split('-')
            b1 = str(b[:-1])
            v = int(c[1])
            v += 1
            b1 += str(v)

            new = str(data1).replace(b, b1)
            with open('src/votos.txt', 'w+') as file2:
                file2.write(new)

        if tipo == 'branco':
            b = data2[2]
            c = b.split('-')
            b1 = str(b[:-1])
            v = int(c[1])
            v += 1
            b1 += str(v)

            new = str(data1).replace(b, b1)
            with open('src/votos.txt', 'w+') as file2:
                file2.write(new)
        if tipo == 'nulo':
            b = data2[3]
            c = b.split('-')
            b1 = str(b[:-1])
            v = int(c[1])
            v += 1
            b1 += str(v)

            new = str(data1).replace(b, b1)
            with open('src/votos.txt', 'w+') as file2:
                file2.write(new)


def addVotoGov(tipo):
    with open('src/votos.txt', 'r+') as file1:
        data1 = file1.read()
        data2 = data1.split(';')

        data2 = data2[1]
        data2 = data2.split('\n')
        data2.remove('')

        if tipo == 'cand1':
            b = data2[0]
            c = b.split('-')
            b1 = str(b[:-1])
            v = int(c[1])
            v += 1
            b1 += str(v)

            new = str(data1).replace(b, b1)
            with open('src/votos.txt', 'w+') as file2:
                file2.write(new)

        if tipo == 'cand2':
            b = data2[1]
            c = b.split('-')
            b1 = str(b[:-1])
            v = int(c[1])
            v += 1
            b1 += str(v)

            new = str(data1).replace(b, b1)
            with open('src/votos.txt', 'w+') as file2:
                file2.write(new)

        if tipo == 'branco':
            b = data2[2]
            c = b.split('-')
            b1 = str(b[:-1])
            v = int(c[1])
            v += 1
            b1 += str(v)

            new = str(data1).replace(b, b1)
            with open('src/votos.txt', 'w+') as file2:
                file2.write(new)
        if tipo == 'nulo':
            b = data2[3]
            c = b.split('-')
            b1 = str(b[:-1])
            v = int(c[1])
            v += 1
            b1 += str(v)

            new = str(data1).replace(b, b1)
            with open('src/votos.txt', 'w+') as file2:
                file2.write(new)


def ContVotos():
    with open('src/resultado.txt', 'w+') as file:
        TotalPres = (int(dados.votosPresCand1) + int(dados.votosPresCand2) +
                     int(dados.votosPresBranco) + int(dados.votosPresNulo))
        lista_de_votos = [int(dados.votosPresCand1), int(dados.votosPresCand2), int(
            dados.votosPresBranco), int(dados.votosPresNulo)]
        i = 0
        listafinal = ''
        listafinal = 'Total de votos-' + str(TotalPres) + '\n'
        while i < len(lista_de_votos):
            try:
                Porcen = (lista_de_votos[i]*100)/TotalPres
            except:
                Porcen = 0
            listanPres = ''
            Porcen = round(Porcen, 2)
            listanPres = dados.listaPres[i] + '-' + str(Porcen) + '%'
            listafinal += listanPres + '\n'
            i += 1

        TotalGov = (int(dados.votosGovCand1) + int(dados.votosGovCand2) +
                    int(dados.votosGovBranco) + int(dados.votosGovNulo))
        lista_de_votos2 = [int(dados.votosGovCand1), int(dados.votosGovCand2), int(
            dados.votosGovBranco), int(dados.votosGovNulo)]
        i = 0
        listafinal += ';' + '\n' + 'Total de votos-' + str(TotalGov) + '\n'
        while i < len(lista_de_votos2):
            try:
                Porcen = (lista_de_votos2[i] * 100) / TotalGov
            except:
                Porcen = 0
            listanGov = ''
            Porcen = round(Porcen, 2)
            listanGov = dados.listaGov[i] + '-' + str(Porcen) + '%'
            listafinal += listanGov + '\n'
            i += 1
        file.write(listafinal)
