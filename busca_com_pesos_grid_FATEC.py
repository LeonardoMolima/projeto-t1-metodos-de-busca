import numpy as np
import random as rd
import math as ma

class No(object):
    def __init__(self, pai=None, coordenada=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.coordenada= coordenada
        self.valor1    = valor1        
        self.valor2    = valor2        
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):
        
        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual


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
            linha = []
            linha.append(aux.estado)
            linha.append(aux.valor1)            
            str.append(linha)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    def exibeArvore1(self,s):

        
        atual = self.head
        while atual.estado != s:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def exibeArvore2(self, s, v1):
        
        atual = self.tail
        
        while atual.coordenada != s or atual.valor1 != v1:
            atual = atual.anterior
        
        caminho = []
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
    
    def custo_uniforme(self,inicio,fim,dx,dy,obs):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.coordenada == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.coordenada,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho[::-1], atual.valor2
        
            x = atual.coordenada[0]
            y = atual.coordenada[1]

            filhos = []
            filhos = self.sucessor(x,y,dx,dy,obs)

            for novo in filhos:
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[2]  
                # VALOR DA FUNÇÃO F(N)
                v1 = v2
                # suponho que não foi visitado
                # ou foi visitado com valor pior
                flag1 = True
                # suponho que não foi visitado
                flag2 = True
                aux = []
                aux.append(novo[0])
                aux.append(novo[1])
                for j in range(len(visitado)):
                    if visitado[j][0]==aux:
                        if visitado[j][1]<=v2:
                            # foi visitado e o valor
                            # é pior do que a visita
                            flag1 = False 
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(aux,v1,v2,atual)
                    l2.inserePos_X(aux,v1,v2,atual)
                    if flag2:
                        linha = []
                        linha.append(aux)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      
    
    def greedy(self,inicio,fim,dx,dy,obs):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.coordenada == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.coordenada,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho[::-1], atual.valor2
        
            x = atual.coordenada[0]
            y = atual.coordenada[1]

            filhos = []
            filhos = self.sucessor(x,y,dx,dy,obs)

            for novo in filhos:
                aux = []
                aux.append(novo[0])
                aux.append(novo[1])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[2]  
                # VALOR DA FUNÇÃO F(N)
                v1 = self.heuristica(aux,fim)
                # suponho que não foi visitado
                # ou foi visitado com valor pior
                flag1 = True
                # suponho que não foi visitado
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==aux:
                        if visitado[j][1]<=v2:
                            # foi visitado e o valor
                            # é pior do que a visita
                            flag1 = False 
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(aux,v1,v2,atual)
                    l2.inserePos_X(aux,v1,v2,atual)
                    if flag2:
                        linha = []
                        linha.append(aux)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      

    def a_estrela(self,inicio,fim,dx,dy,obs):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.coordenada == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.coordenada,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho[::-1], atual.valor2
        
            x = atual.coordenada[0]
            y = atual.coordenada[1]

            filhos = []
            filhos = self.sucessor(x,y,dx,dy,obs)

            for novo in filhos:
                aux = []
                aux.append(novo[0])
                aux.append(novo[1])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[2]  
                # VALOR DA FUNÇÃO F(N)
                v1 = v2 + self.heuristica(aux,fim)
                
                # suponho que não foi visitado
                # ou foi visitado com valor pior
                flag1 = True
                # suponho que não foi visitado
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==aux:
                        if visitado[j][1]<=v2:
                            # foi visitado e o valor
                            # é pior do que a visita
                            flag1 = False 
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(aux,v1,v2,atual)
                    l2.inserePos_X(aux,v1,v2,atual)
                    if flag2:
                        linha = []
                        linha.append(aux)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"

    def aia_estrela(self,inicio,fim,dx,dy,obs,limite):
        
        while True:
            lim_exc = []
            l1 = lista()
            l2 = lista()
            visitado = []
            
            l1.insereUltimo(inicio,0,0,None)
            l2.insereUltimo(inicio,0,0,None)
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
            
            while l1.vazio() == False:
                atual = l1.deletaPrimeiro()
                
                if atual.coordenada == fim:
                    caminho = []
                    caminho = l2.exibeArvore2(atual.coordenada,atual.valor1)
                    return caminho[::-1], atual.valor2
            
                x = atual.coordenada[0]
                y = atual.coordenada[1]
    
                filhos = []
                filhos = self.sucessor(x,y,dx,dy,obs)
    
                for novo in filhos:
                    aux = []
                    aux.append(novo[0])
                    aux.append(novo[1])
                    
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    v2 = atual.valor2 + novo[2]  
                    # VALOR DA FUNÇÃO F(N)
                    v1 = v2 + self.heuristica(aux,fim)
                    
                    if v1<=limite:
                        # suponho que não foi visitado
                        # ou foi visitado com valor pior
                        flag1 = True
                        # suponho que não foi visitado
                        flag2 = True
                        for j in range(len(visitado)):
                            if visitado[j][0]==aux:
                                if visitado[j][1]<=v2:
                                    # foi visitado e o valor
                                    # é pior do que a visita
                                    flag1 = False 
                                else:
                                    visitado[j][1]=v2
                                    flag2 = False
                                break
        
                        if flag1:
                            l1.inserePos_X(aux,v1,v2,atual)
                            l2.inserePos_X(aux,v1,v2,atual)
                            if flag2:
                                linha = []
                                linha.append(aux)
                                linha.append(v2)
                                visitado.append(linha)
                    else:
                        lim_exc.append(v1)
                limite = sum(lim_exc)/len(lim_exc)
        return "Caminho não encontrado"
            
    def heuristica(self,atual,objetivo):
        dif_x = ma.fabs(atual[0]-objetivo[0])
        dif_y = ma.fabs(atual[1]-objetivo[1])
        return dif_x+dif_y
        
    def sucessor(self,x,y,dx,dy,obs):

        f = []

        # ACIMA (custo = 0.5)
        if y+1<dy:
            linha = []
            linha.append(x)
            linha.append(y+1)
            linha.append(0.5)
            if linha not in obs:
                f.append(linha)
        
        # ESQUERDA (custo = 5)
        if x-1>=0:
            linha = []
            linha.append(x-1)
            linha.append(y)
            linha.append(5)
            if linha not in obs:
                f.append(linha)

        # DIREITA (custo = 2.5)
        if x+1<dx:
            linha = []
            linha.append(x+1)
            linha.append(y)
            linha.append(2.5)
            if linha not in obs:
                f.append(linha)

        # ABAIXO (custo = 20)
        if y-1>=0:
            linha = []
            linha.append(x)
            linha.append(y-1)
            linha.append(20)
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
    
    #primeiro obstáculo
    pos = []
    pos.append(2)
    pos.append(2)
    obs.append(pos)
    
    #segundo obstáculo
    pos = []
    pos.append(1)
    pos.append(0)
    obs.append(pos)
    
    
    return mapa, obs

# HEURISTICA SERVE SOMENTE PARA DESTINO BUCARESTE
sol = busca()
caminho = []
'''
dx = 6
dy = 6
inicio  = [0,0]
final = [5,5]
mapa, obs = gera_Ambiente(dx,dy)

caminho, custo = sol.aia_estrela(inicio,final,dx,dy,obs,sol.heuristica(inicio,final))
print("\nAIA estrela: ",caminho,"\ncusto do caminho: ",custo)
caminho1 = []
print(caminho);
for no in caminho:
    aux = f'{mapa[no[0]][no[1]]}'
    caminho1.append(aux)

print(caminho1);


caminho, custo = sol.custo_uniforme(inicio,final,dx,dy,obs)
print("Custo Uniforme: ",caminho[::-1],"\nCusto do Caminho: ",custo)
caminho1 = []
print(caminho);
for no in caminho:
    aux = f'{mapa[no[0]][no[1]]}'
    caminho1.append(aux)

print(caminho1);

caminho, custo = sol.greedy(inicio,final,dx,dy,obs)
print("\nGreedy: ",caminho[::-1],"\ncusto do caminho: ",custo)
caminho1 = []
print(caminho);
for no in caminho:
    aux = f'{mapa[no[0]][no[1]]}'
    caminho1.append(aux)

print(caminho1);


caminho, custo = sol.a_estrela(inicio,final,dx,dy,obs)
print("\nA estrela: ",caminho[::-1],"\ncusto do caminho: ",custo)
caminho1 = []
print(caminho);
for no in caminho:
    aux = f'{mapa[no[0]][no[1]]}'
    caminho1.append(aux)

print(caminho1);
'''