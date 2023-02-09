def movimentos(estado):
    possibilidades = []
    miss = estado[0]
    cani = estado[1]
    barco = estado[2]

    if barco == 1:
        for i in range(0,3):
            for j in range(0,3):
                miss2 = miss - i
                cani2 = cani - j
                if i+j<=2 and i+j>=1 and miss2>=0 and cani2>=0 and miss2<=3 and cani2<=3:
                    if miss2 != 0:
                        if miss2>=cani2:
                            if (3-miss2) != 0:
                                if (3-cani+j)<=(3-miss+i):
                                    possibilidades.append([miss2,cani2,0])
                            else:
                                possibilidades.append([miss2,cani2,0])
                    else:
                        possibilidades.append([miss2,cani2,0])
    else:
        for i in range(0,3):
            for j in range(0,3):
                miss2 = miss + i
                cani2 = cani + j
                if i+j<=2 and i+j>=1 and miss2>=0 and cani2>=0 and miss2<=3 and cani2<=3:
                    if miss != 0:
                        if (3-miss2) != 0:
                            if (3-cani-j)<=(3-miss-i) and miss2>=cani2:
                                possibilidades.append([miss2,cani2,1])
                        else:
                            possibilidades.append([miss2,cani2,1])
                    else:
                        possibilidades.append([miss2,cani2,1])
    return possibilidades

def bfs(inicio,final):
    fronteira = [[inicio]]
    visitados = []
    while fronteira:
        path = fronteira[0]
        fronteira = fronteira[1:]
        end = path[-1]
        if end in visitados:
            continue
        for move in movimentos(end):
            if move in visitados:
                continue
            fronteira.append(path + [move])
        visitados.append(end)
        if end == final: break
    
    return path

inicio = [3,3,1]
final = [0,0,0]

resposta = bfs(inicio,final)
contador = 0
for estado in resposta:
    print('Movimento',contador)
    print('Missionários:',estado[0])
    print('Canibais:', estado[1])
    print('Barco na margem:', estado[2])
    print('------------')
    contador+=1
