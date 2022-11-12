with open('src/candidatos.txt', 'r+') as arquivo_candidatos:
    lista_candidatos = arquivo_candidatos.read()

    lista_candidatos = lista_candidatos.split(';')

    # presidente
    lista_presidentes = lista_candidatos[0]
    lista_presidentes = lista_presidentes.split('\n')
    lista_presidentes.remove('')

    info_precandidato1 = lista_presidentes[0]
    info_precandidato1 = info_precandidato1 .split('-')
    nome_precandidato1 = info_precandidato1[0]
    numero_precandidato1 = info_precandidato1[1]
    foto_precandidato1 = info_precandidato1[2]

    info_precandidato2 = lista_presidentes[1]
    info_precandidato2 = info_precandidato2.split('-')
    nome_precandidato2 = info_precandidato2[0]
    numero_precandidato2 = info_precandidato2[1]
    foto_precandidato2 = info_precandidato2[2]

    # __

    # governador
    lista_governadores = lista_candidatos[1]
    lista_governadores = lista_governadores.split('\n')
    lista_governadores.remove('')

    info_govcandidato1 = lista_governadores[0]
    info_govcandidato1 = info_govcandidato1.split('-')
    nome_govcandidato1 = info_govcandidato1[0]
    numero_govcandidato1 = info_govcandidato1[1]
    foto_govcandidato1 = info_govcandidato1[2]

    info_govcandidato2 = lista_governadores[1]
    info_govcandidato2 = info_govcandidato2.split('-')
    nome_govcandidato2 = info_govcandidato2[0]
    numero_govcandidato2 = info_govcandidato2[1]
    foto_govcandidato2 = info_govcandidato2[2]

# __

with open('src/votos.txt', 'r+') as file2:
    info = file2.read()
    candinfo = info.split(';')

    # presidente
    listaPres = candinfo[0]
    listaPres = listaPres.split('\n')
    listaPres.remove('')

    presCand1 = listaPres[0].split('-')
    nomePresCand1 = presCand1[0]
    votosPresCand1 = presCand1[1]

    presCand2 = listaPres[1].split('-')
    nomePresCand2 = presCand2[0]
    votosPresCand2 = presCand2[1]

    presBranco = listaPres[2].split('-')
    nomePresBranco = presBranco[0]
    votosPresBranco = presBranco[1]

    presNulo = listaPres[3].split('-')
    nomePresNulo = presNulo[0]
    votosPresNulo = presNulo[1]

    # governador
    listaGov = candinfo[1]
    listaGov = listaGov.split('\n')
    listaGov.remove('')

    govCand1 = listaGov[0].split('-')
    nomeGovCand1 = govCand1[0]
    votosGovCand1 = govCand1[1]

    govCand2 = listaGov[1].split('-')
    nomeGovCand2 = govCand2[0]
    votosGovCand2 = govCand2[1]

    govBranco = listaGov[2].split('-')
    nomeGovBranco = govBranco[0]
    votosGovBranco = govBranco[1]

    govNulo = listaPres[3].split('-')
    nomeGovNulo = govNulo[0]
    votosGovNulo = govNulo[1]
