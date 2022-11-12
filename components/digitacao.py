def digitado(win):
    # Checka a coordenada pressionada e compara com os elementos graficos
    click = win.getMouse()
    # Retorna o numero 1
    if (515 < click.getX() < 552) and (162 < click.getY() < 188):
        return str(1)
    # Retorna o numero 4
    elif (515 < click.getX() < 552) and (202 < click.getY() < 228):
        return str(4)
    # Retorna o numero 7
    elif (515 < click.getX() < 552) and (242 < click.getY() < 268):
        return str(7)
    # Retorna o numero 2
    elif (565 < click.getX() < 602) and (162 < click.getY() < 188):
        return str(2)
    # Retorna o numero 5
    elif (565 < click.getX() < 602) and (202 < click.getY() < 228):
        return str(5)
    # Retorna o numero 8
    elif (565 < click.getX() < 602) and (242 < click.getY() < 268):
        return str(8)
    # Retorna o numero 3
    elif (615 < click.getX() < 652) and (162 < click.getY() < 188):
        return str(3)
    # Retorna o numero 6
    elif (615 < click.getX() < 652) and (202 < click.getY() < 228):
        return str(6)
    # Retorna o numero 9
    elif (615 < click.getX() < 652) and (242 < click.getY() < 268):
        return str(9)
    # Retorna o numero 0
    elif (565 < click.getX() < 602) and (282 < click.getY() < 308):
        return str(0)
    # Retorna string 'confirma'
    elif ((620 < click.getX() < 675) and (314 < click.getY() < 352)):
        return 'confirma'
    # Retorna string 'branco'
    elif ((490 < click.getX() < 545) and (324 < click.getY() < 352)):
        return 'branco'
    # Retorna string 'corrige'
    elif ((555 < click.getX() < 612) and (324 < click.getY() < 352)):
        return 'corrige'
    # Retorna string 'encerra'
    elif ((625 < click.getX() < 674) and (396 < click.getY() < 444)):
        return 'encerra'
    # Retorna None
    else:
        return 'None'
