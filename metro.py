distancias = [
    [0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32],
    [11, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24],
    [20, 9, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18],
    [27, 16, 7, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17],
    [40, 29, 20, 13, 0, 3, 2, 21, 25, 31, 38, 27, 16, 20],
    [43, 32, 22, 16, 3, 0, 4, 23, 28, 33, 41, 30, 17, 20],
    [39, 28, 19, 12, 2, 4, 0, 22, 25, 29, 38, 28, 13, 17],
    [28, 19, 15, 13, 21, 23, 22, 0, 9, 22, 18, 7, 25, 30],
    [18, 11, 10, 13, 25, 28, 25, 9, 0, 13, 12, 12, 23, 28],
    [10, 4, 11, 18, 31, 33, 29, 22, 13, 0, 20, 27, 20, 23],
    [18, 17, 21, 26, 38, 41, 38, 18, 12, 20, 0, 15, 35, 39],
    [30, 23, 21, 21, 27, 30, 28, 7, 12, 27, 15, 0, 31, 37],
    [30, 21, 13, 11, 16, 17, 13, 25, 23, 20, 35, 31, 0, 5],
    [32, 24, 18, 17, 20, 20, 17, 30, 28, 23, 39, 37, 5, 0],
]
matrixAdj = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

matrix_Enc = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 1, 0, 0, 4, 0, 0, 0, 0, 4, 0],
            [0, 0, 0, 1, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 2, 0, 0, 0, 2, 0, 0, 4, 0, 0],
            [0, 2, 3, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0]]


def custo_de_tempo(origem:int, destino:int):
    return (distancias[origem][destino] * 2)

def busca(origem:int, destino:int):
    posicao = 1
    tempo_total=0
    no_pai = origem
    visitados = [0]*len(distancias)
    tempos = [0]*len(distancias)
    ordem_estacoes= [0]*len(distancias)
    linha_estacao= [0]*len(distancias)
    
    #soma da estimativa + custo acumulado
    f=0
    g=0
    h=0
    
    f_node_melhor = 9999
    melhor_node=0
    linha_melhor_node=0
    visitados[origem]=1
    ordem_estacoes[posicao]=origem
    tempos[posicao]=0
    linha_estacao[posicao]=0
    
    while(ordem_estacoes[posicao]!=destino):
        for no_atual in range(0,len(distancias)):
            if no_atual!=destino:
                counter = 0
                for i in range(0,len(distancias)):
                    if matrixAdj[no_atual][i]==1:
                        counter += 1
            if counter==1:
                no_atual+=1
            if matrixAdj[no_pai][no_atual-1]==1 and visitados[no_atual-1]==0:
                g = custo_de_tempo(no_pai, no_atual-1)
                if matrix_Enc[no_pai][no_atual-1] != linha_estacao[posicao] and (linha_estacao[posicao]!=0 and matrix_Enc[no_pai][no_atual-1]!=0):
                    g+=4
                h=custo_de_tempo(no_atual-1,destino)
                f = g+h
                if f_node_melhor >= f:
                    f_node_melhor=f
                    melhor_node=no_atual
                    linha_melhor_node= matrix_Enc[no_pai][no_atual-1]
                    visitados[melhor_node-1] = 1

        tempos[posicao-1]= custo_de_tempo(no_pai, melhor_node-1)
        tempo_total += tempos[posicao-1]
        linha_estacao[posicao]= linha_melhor_node
        
        if (linha_estacao[posicao] != linha_estacao[posicao]) and (linha_estacao[posicao] != 0 and linha_estacao[posicao-1] !=0):
                tempo_total +=4
        print("Estacao",no_pai,"->Estacao",melhor_node," Tempo:",tempos[posicao-1])
        no_pai= melhor_node
        posicao+=1
        ordem_estacoes[posicao]= no_pai
    print("Tempo total: ",tempo_total)
  
busca(0,4)
    
    
