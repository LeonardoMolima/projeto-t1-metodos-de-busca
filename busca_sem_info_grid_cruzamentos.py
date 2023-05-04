class No(object):
    def __init__(self, pai=None, coordenada=None, nivel=None, anterior=None, proximo=None):
        self.pai           = pai
        self.coordenada    = coordenada
        self.nivel         = nivel
        self.anterior      = anterior
        self.proximo       = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, p):
        novo_no = No(p, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, p):

        novo_no = No(p, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.coordenada)
            temp.append(aux.nivel)
            str.append(temp)
            aux = aux.proximo
        
        return str
    
    def exibeCaminho(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.coordenada)
            atual = atual.pai
        caminho.append(atual.coordenada)
        caminho = caminho[::-1]
        return caminho
    
    def exibeCaminho1(self,valor):
                
        atual = self.head
        print(atual.coordenada,valor)
        
        while atual.coordenada[0] != valor[0] or atual.coordenada[1] != valor[1]:
            atual = atual.proximo
        print(atual.coordenada)
        
        #AQUI!!!!!!!!
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.coordenada)
            atual = atual.pai
        caminho.append(atual.coordenada)
        return caminho

    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

class busca(object):

    def amplitude(self, inicio, fim, dx, dy, obs):

        caminho = []
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            x = atual.coordenada[0]
            y = atual.coordenada[1]

            filhos = []
            filhos = self.sucessor(x,y,dx,dy,obs)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.nivel+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        print("Árvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"
    
    def profundidade(self, inicio, fim, dx, dy, obs):

        caminho = []
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            x = atual.coordenada[0]
            y = atual.coordenada[1]

            filhos = []
            filhos = self.sucessor(x,y,dx,dy,obs)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.nivel+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        print("Árvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"
    
    def prof_limitada(self, inicio, fim, dx, dy, obs, limite):

        caminho = []
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio()!=True:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            if atual.nivel < limite:
                x = atual.coordenada[0]
                y = atual.coordenada[1]
    
                filhos = []
                filhos = self.sucessor(x,y,dx,dy,obs)
    
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
    
                    flag = True  # pressuponho que não foi visitado
    
                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.nivel+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho += l2.exibeCaminho()
                            print("Árvore de busca:\n",l2.exibeLista())
                            return caminho
        
        return caminho
    
    def aprof_iterativo(self, inicio, fim, dx, dy, obs, lim_max):
        
        for limite in range(1,lim_max):

            caminho = []
            # manipular a FILA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
            while l1.vazio()!=True:
                # remove o primeiro da fila
                atual = l1.deletaUltimo()
                if atual.nivel < limite:
                    x = atual.coordenada[0]
                    y = atual.coordenada[1]
        
                    filhos = []
                    filhos = self.sucessor(x,y,dx,dy,obs)
        
                    # varre todos as conexões dentro do grafo a partir de atual
                    for novo in filhos:
        
                        flag = True  # pressuponho que não foi visitado
        
                        # para cada conexão verifica se já foi visitado
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.nivel+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.nivel+1
                                break
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.nivel + 1, atual)
                            l2.insereUltimo(novo, atual.nivel + 1, atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.nivel+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho += l2.exibeCaminho()
                                print("Árvore de busca:\n",l2.exibeLista())
                                return caminho
        
        return []
    
    # BUSCA BIDIRECIONAL
    def bidirecional(self, inicio, fim, dx, dy, obs):
    
        # manipular a FILA para a busca
        l1 = lista()
        l3 = lista()
    
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()
        l4 = lista()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)
    
    
        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        
        ni = 0
        while l1.vazio()==False or l3.vazio()==False:
            
            while l1.vazio() == False:
                
                if ni!=l1.primeiro().nivel:
                    break
                    
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
                x = atual.coordenada[0]
                y = atual.coordenada[1]
                #print("atual primeiro: ",x,y)

                filhos = []
                filhos = self.sucessor(x,y,dx,dy,obs)
                #print("filhos primeiro: ",filhos)
                
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # pressuponho que não foi visitado
                    flag = True
                    #print(novo)
        
                    # controle de nós repetidos
                    for j in range(len(visitado1)):
                        if visitado1[j][0]==novo:
                            if visitado1[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado1[j][1]=atual.nivel+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado1.append(linha)
        
                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado2)):
                            if visitado2[j][0]==novo:
                                flag = True
                                break
                        
                        if flag:
                            caminho = []
                            #print("Fila:\n",l1.exibeLista())
                            print("\nÁrvore de busca:\n",l2.exibeLista())
                            print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        
            while l3.vazio() == False:
                if ni!= l3.primeiro().nivel:
                    break
                # remove o primeiro da fila
                atual = l3.deletaPrimeiro()
                x = atual.coordenada[0]
                y = atual.coordenada[1]

                filhos = []
                filhos = self.sucessor(x,y,dx,dy,obs)
                #print("atual segundo: ",x,y)
                #print("filhos segundo: ",filhos)
                
                
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:

                    # pressuponho que não foi visitado
                    flag = True
        
                    # controle de nós repetidos
                    for j in range(len(visitado2)):
                        if visitado2[j][0]==novo:
                            if visitado2[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado2[j][1]=atual.nivel+1
                            break
                        
                    # se não foi visitado inclui na fila
                    if flag:
                        l3.insereUltimo(novo, atual.nivel + 1, atual)
                        l4.insereUltimo(novo, atual.nivel + 1, atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado2.append(linha)
        
                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado1)):
                            if visitado1[j][0]==novo:
                                flag = True
                                break
                            
                        if flag:
                            caminho = []
                            #print("Fila:\n",l3.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]
                            
            ni += 1
    
        return caminho
    
    
    def sucessor(self,x,y,dx,dy,obs):

        f = []
        
        # direita
        if x+1<dx:
            linha = []
            linha.append(x+1)
            linha.append(y)
            if linha not in obs:
                f.append(linha)
        
        # esquerda
        if x-1>=0:
            linha = []
            linha.append(x-1)
            linha.append(y)
            if linha not in obs:
                f.append(linha)

        # acima
        if y+1<dy:
            linha = []
            linha.append(x)
            linha.append(y+1)
            if linha not in obs:
                f.append(linha)

        # abaixo
        if y-1>=0:
            linha = []
            linha.append(x)
            linha.append(y-1)
            if linha not in obs:
                f.append(linha)
        
        return f
    
def gera_Ambiente(dx,dy):
        
    mapa = []
    
    # Gerando o ambiente
    for i in range(1,dx+1):
        linha = []
        for j in range(1,dy+1): 
            str1 = "C" + str((i-1)*dx + j)
            linha.append(str1)
        mapa.append(linha)
    
    # Gerando os obstáculos
    obs = []
    pos = []
    
    
    #obstáculos
    '''
    pos = []
    pos.append(0)
    pos.append(4)
    obs.append(pos)
    '''

    for i in mapa:
        for j in mapa:
            x = mapa.index(i)
            y = mapa.index(j)
            print(mapa[x][y])
    
    return mapa, obs       


sol = busca()
caminho = []

# PROBLEMA C
'''
dim_x = 6
dim_y = 6
origem  = [0,0]
destino = [5,5]
mapa, obs = gera_Ambiente(dim_x,dim_y)
limite = 12
#print(mapa)
'''
'''

caminho = sol.amplitude(origem,destino,dim_x,dim_y,obs)
print("\nAmplitude.......: ",caminho,'\n')

caminho1 = []
for no in caminho:
    print(mapa[no[0]][no[1]])
    caminho1.append(mapa[no[0]][no[1]])
print("\nAmplitude.......: ",caminho1)


caminho = sol.profundidade(origem,destino,dim_x,dim_y,obs)
print("\nProfundidade.......: ",caminho,'\n')

caminho1 = []
for no in caminho:
    caminho1.append(mapa[no[0]][no[1]])
print("\nProfundidade.......: ",caminho1)


caminho = sol.prof_limitada(origem,destino,dim_x,dim_y,obs,limite)
if len(caminho)>0:
    print("\nProf_limitada.......: ",caminho,'\n')

    caminho1 = []
    for no in caminho:
        caminho1.append(mapa[no[0]][no[1]])
    print("\nProf_limitada.......: ",caminho1)
else:
    print("\nProf_limitada.......: Caminho não encontrado")

caminho = sol.aprof_iterativo(origem,destino,dim_x,dim_y,obs,limite)
if len(caminho)>0:
    print("\nAprof_iterativo.......: ",caminho,'\n')

    caminho1 = []
    for no in caminho:
        caminho1.append(mapa[no[0]][no[1]])
    print("\nAprof_iterativo.......: ",caminho1)
else:
    print("\nAprof_iterativo.......: Caminho não encontrado")


caminho = sol.bidirecional(origem,destino, dim_x, dim_y, obs)
print("\nBIDIRECIONAL.......: ",caminho,'\n')

caminho1 = []
for no in caminho:
    caminho1.append(mapa[no[0]][no[1]])
print("\nBIDIRECIONAL.......: ",caminho1)
'''