class node:
    def __init__(self, estacao, distancias, vizinhos=[]):
        self.estacao: int = estacao
        self.distancias: list = distancias
        self.vizinhos: list = vizinhos
        self.acumulado = 0
        self.ultima_linha = ""


e1 = node(0, [0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32])
e2 = node(1, [11, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24])
e3 = node(2, [20, 9, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18])
e4 = node(3, [27, 16, 7, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17])
e5 = node(4, [40, 29, 20, 13, 0, 3, 2, 21, 25, 31, 38, 27, 16, 20])
e6 = node(5, [43, 32, 22, 16, 3, 0, 4, 23, 28, 33, 41, 30, 17, 20])
e7 = node(6, [39, 28, 19, 12, 2, 4, 0, 22, 25, 29, 38, 28, 13, 17])
e8 = node(7, [28, 19, 15, 13, 21, 23, 22, 0, 9, 22, 18, 7, 25, 30])
e9 = node(8, [18, 11, 10, 13, 25, 28, 25, 9, 0, 13, 12, 12, 23, 28])
e10 = node(9, [10, 4, 11, 18, 31, 33, 29, 22, 13, 0, 20, 27, 20, 23])
e11 = node(10, [18, 17, 21, 26, 38, 41, 38, 18, 12, 20, 0, 15, 35, 39])
e12 = node(11, [30, 23, 21, 21, 27, 30, 28, 7, 12, 27, 15, 0, 31, 37])
e13 = node(12, [30, 21, 13, 11, 16, 17, 13, 25, 23, 20, 35, 31, 0, 5])
e14 = node(13, [32, 24, 18, 17, 20, 20, 17, 30, 28, 23, 39, 37, 5, 0])

e1.vizinhos = [(e2, "Az")]
e2.vizinhos = [(e1, "Az"), (e3, "Az"), (e9, "Am"), (e10, "Am")]
e3.vizinhos = [(e2, "Az"), (e4, "Az"), (e9, "Vm"), (e13, "Vm")]
e4.vizinhos = [(e3, "Az"), (e5, "Az"), (e8, "Vd"), (e13, "Vd")]
e5.vizinhos = [(e4, "Az"), (e8, "Am"), (e6, "Az"), (e7, "Am")]
e6.vizinhos = [(e5, "Az")]
e7.vizinhos = [(e5, "Am")]
e8.vizinhos = [(e9, "Am"), (e5, "Am"), (e12, "Vd"), (e4, "Vd")]
e9.vizinhos = [(e2, "Am"), (e11, "Vm"), (e3, "Vm"), (e8, "Am")]
e10.vizinhos = [(e2, "Am")]
e11.vizinhos = [(e9, "Vm")]
e12.vizinhos = [(e8, "Vd")]
e13.vizinhos = [(e3, "Vm"), (e4, "Vd"), (e14, "Vd")]
e14.vizinhos = [(e13, "Vd")]

visitados = []


def buscar(origem: node, destino: node):
    no_pai: node = origem
    caminho = [origem]
    visitados.append(no_pai)
    while True:
        if no_pai.estacao == destino.estacao:
            for i in range(0, len(caminho)):
                print("Estacao: ", caminho[i].estacao+1,
                      "custo acumulado: ", caminho[i].acumulado)
            print("Fim")
            break
        else:
            melhor: node = node(99, [])
            melhor.acumulado = 99999
            for i in no_pai.vizinhos:
                if i[0] in visitados:
                    continue
                else:
                    visitados.append(i[0])
                    i[0].acumulado = no_pai.acumulado + i[0].distancias[no_pai.estacao] + i[0].distancias[destino.estacao]
                    if i[1] != no_pai.ultima_linha and no_pai.ultima_linha != '':
                        i[0].acumulado += 4
                    if i[0].acumulado < melhor.acumulado:
                        melhor = i[0]
                        melhor.ultima_linha = i[1]
            caminho.append(melhor)
            no_pai = melhor

buscar(e1, e6)
