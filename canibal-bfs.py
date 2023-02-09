class node:
    def __init__(self, data, parents=None):
        self.parents = parents
        self.data = data
        
    def printar_caminho(self):
        if self.parents != None:
            self.parents.printar_caminho()
        print(self.data)
        
initial = node([3,3,0,0,0]) # pos[0] = nº de padres do lado inicial // pos[1] = nº de canibais do lado inicial // pos[2] = nº de padres do lado final // pos[3] = nº de canibais do lado final // pos[4] = lado do barco (0 - lado inicial, 1 - lado final)
fronteira:node = [] # possibilidades atualmente na memória
visitados=[] # estados já visitados
operadores = [(1,0), (1,1), (2,0), (0,2)] #movimento possiveis

def testeMeta(estado_atual:node):
    if estado_atual.data[2]==3 and estado_atual.data[3]==3:
        return True
    else: return False

def mover(estado_atual, m=0, c=0):
    
    if m + c >2:
        return
    
    om = 0 #origem dos missionarios
    oc = 1 #origem dos canibais
    dm = 2 #destino dos missionarios
    dc = 3 #destino dos canibais
    
    if estado_atual[-1] == 1:
       om = 2 
       oc = 3 
       dm = 0 
       dc = 1 
    
    if estado_atual[om]== 0 and estado_atual[oc] == 0 :
        return
    
    estado_atual[-1] = 1 - estado_atual[-1]
    
    for i in range(min(m,estado_atual[om])):
        estado_atual[om]-=1
        estado_atual[dm]+=1
        
    for i in range(min(c,estado_atual[oc])):
        estado_atual[oc]-=1
        estado_atual[dc]+=1
        
    return estado_atual

def gerar_grafo(estado_atual:node):
    filhos:node = []
    for (i,j) in operadores:
        s = mover(estado_atual.data[:], i , j)
        if s == None : continue
        if (s[0]<s[1] and s[0]>0) or (s[2]<s[3] and s[2]>0): continue
        if s in visitados: continue
        filhos.append(node(s,estado_atual))
    return filhos

def bfs(estado):
    fronteira.append(estado)
    while len(fronteira) > 0:
        elemento = fronteira[0]
        if testeMeta(elemento):
            break
        else:
            v = gerar_grafo(elemento)
            if len(v) != 0:
                for i in range(len(v)):
                    visitados.append(v[i].data)
                    fronteira.append(v[i])
            else:
                fronteira.pop(0)
    else:
        print("Caminho não encontrado")
    return elemento

result=bfs(initial)
result.printar_caminho()