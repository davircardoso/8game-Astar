class Busca: 
       
    def __init__(self):
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]   
                
    def largura(self, father):
        linhas = len(father)
        colunas = len(father[0])
        linha_zero = 0
        col_zero = 0
        abertos = [(father, [])]
        explorados = set()
        
        while abertos:
            estado_atual, movimentos = abertos.pop(0)
            explorados.add(str(estado_atual))
            
            if estado_atual == self.goal:
                qtd_jogadas = 'Quantidade de jogadas: ' + str(len(movimentos))
                jogadas = 'Jogadas: ' + str(movimentos)
                busca = 'Número de nodos consultados: ' + str(len(explorados))
                return qtd_jogadas, jogadas, busca
            
            for i in range(linhas):
                for j in range(colunas):
                    if estado_atual[i][j] == 0:
                        linha_zero = i
                        col_zero = j
                        break  
                    
            # Move para cima
            if linha_zero > 0:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero-1][col_zero] = novo_estado[linha_zero-1][col_zero], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                     abertos.append((novo_estado, movimentos + [('Pra cima', novo_estado)]))
                
            # Move para baixo
            if linha_zero < 2:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero+1][col_zero] = novo_estado[linha_zero+1][col_zero], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    abertos.append((novo_estado, movimentos + [('Pra baixo', novo_estado)]))
                
            # Move pra esquerda
            if col_zero > 0:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero][col_zero-1] = novo_estado[linha_zero][col_zero-1], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    abertos.append((novo_estado, movimentos + [('Pra esquerda', novo_estado)]))
                
            # Move pra direita
            if col_zero < 2:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero][col_zero+1] = novo_estado[linha_zero][col_zero+1], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    abertos.append((novo_estado, movimentos + [('Pra direita', novo_estado)]))
            
            
        return 'Não foi possível encontrar uma solução'
                
                
    def distancia_manhattan(self, father):
        distancia = 0
        for i in range(len(father)):
            for j in range(len(father[0])):
                preco = father[i][j]
                if preco != 0:
                    linha_zero = (preco - 1) // len(father[0])
                    col_zero = (preco - 1) % len(father[0])
                    distancia += abs(linha_zero - i) + abs(col_zero - j)
        return distancia
    
    def distancia_manhattan_melhorada(self, father):
        dist = 0
        posicoes = {}
        for i in range(len(father)):
            for j in range(len(father[0])):
                if father[i][j] != 0:
                    posicoes[father[i][j]] = (i, j)
        for i in range(len(father)):
            for j in range(len(father[0])):
                if father[i][j] != 0:
                    final_i, final_j = posicoes[father[i][j]]
                    dist += abs(final_i - i) + abs(final_j - j)
        return dist

    def a_estrela_manhattan(self, father):
        linhas = len(father)
        colunas = len(father[0])
        linha_zero = 0
        col_zero = 0
        explorados = set()
        abertos = [(father, [])]        
        while abertos:
            abertos.sort(key=lambda estado: self.distancia_manhattan(estado[0]) + len(estado[1]) + 1)
            estado_atual, movimentos = abertos.pop(0)
            explorados.add(str(estado_atual))
            
            if estado_atual == self.goal:
                qtd_jogadas = 'Quantidade de jogadas: ' + str(len(movimentos))
                jogadas = 'Jogadas: ' + str(movimentos)
                busca = 'Número de nodos consultados: ' + str(len(explorados))
                return qtd_jogadas, jogadas, busca
            
            for i in range(linhas):
                for j in range(colunas):
                    if estado_atual[i][j] == 0:
                        linha_zero = i
                        col_zero = j
                        break
                              
            # Move para cima
            if linha_zero > 0:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero-1][col_zero] = novo_estado[linha_zero-1][col_zero], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    custo = self.distancia_manhattan(novo_estado) + len(movimentos) + 1
                    abertos.append((novo_estado, movimentos + [('Pra cima', novo_estado, custo) ]))
                
                
            # Move para baixo
            if linha_zero < 2:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero+1][col_zero] = novo_estado[linha_zero+1][col_zero], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    custo = self.distancia_manhattan(novo_estado) + len(movimentos) + 1
                    abertos.append((novo_estado, movimentos + [('Pra cima', novo_estado, custo)]))
                  
                
            # Move pra esquerda
            if col_zero > 0:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero][col_zero-1] = novo_estado[linha_zero][col_zero-1], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    custo = self.distancia_manhattan(novo_estado) + len(movimentos) + 1
                    abertos.append((novo_estado, movimentos + [('Pra cima', novo_estado, custo)]))
                
            # Move pra direita
            if col_zero < 2:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero][col_zero+1] = novo_estado[linha_zero][col_zero+1], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    custo = self.distancia_manhattan(novo_estado) + len(movimentos) + 1
                    abertos.append((novo_estado, movimentos + [('Pra cima', novo_estado, custo)]))
            
        return None
    
    def a_estrela_heuristica_complexa(self, father):
        linhas = len(father)
        colunas = len(father[0])
        linha_zero = 0
        col_zero = 0
        explorados = set()
        abertos = [(father, [])]        
        while abertos:
            abertos.sort(key=lambda estado: self.distancia_manhattan_melhorada(estado[0]) + len(estado[1]) + 1)
            estado_atual, movimentos = abertos.pop(0)
            explorados.add(str(estado_atual))
            
            if estado_atual == self.goal:
                qtd_jogadas = 'Quantidade de jogadas: ' + str(len(movimentos))
                jogadas = 'Jogadas: ' + str(movimentos)
                busca = 'Número de nodos consultados: ' + str(len(explorados))
                return qtd_jogadas, jogadas, busca
            
            for i in range(linhas):
                for j in range(colunas):
                    if estado_atual[i][j] == 0:
                        linha_zero = i
                        col_zero = j
                        break
                              
            # Move para cima
            if linha_zero > 0:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero-1][col_zero] = novo_estado[linha_zero-1][col_zero], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    custo = self.distancia_manhattan_melhorada(novo_estado) + len(movimentos) + 1
                    abertos.append((novo_estado, movimentos + [('Pra cima', novo_estado, custo) ]))
                
                
            # Move para baixo
            if linha_zero < 2:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero+1][col_zero] = novo_estado[linha_zero+1][col_zero], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    custo = self.distancia_manhattan_melhorada(novo_estado) + len(movimentos) + 1
                    abertos.append((novo_estado, movimentos + [('Pra cima', novo_estado, custo)]))
                  
                
            # Move pra esquerda
            if col_zero > 0:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero][col_zero-1] = novo_estado[linha_zero][col_zero-1], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    custo = self.distancia_manhattan_melhorada(novo_estado) + len(movimentos) + 1
                    abertos.append((novo_estado, movimentos + [('Pra cima', novo_estado, custo)]))
                
            # Move pra direita
            if col_zero < 2:
                novo_estado = [linha[:] for linha in estado_atual]
                novo_estado[linha_zero][col_zero], novo_estado[linha_zero][col_zero+1] = novo_estado[linha_zero][col_zero+1], novo_estado[linha_zero][col_zero]
                if str(novo_estado) not in explorados:
                    custo = self.distancia_manhattan_melhorada(novo_estado) + len(movimentos) + 1
                    abertos.append((novo_estado, movimentos + [('Pra cima', novo_estado, custo)]))
            
        return None