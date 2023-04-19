import time

class EightGame: 
       
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
                
eight_game = EightGame()

start_time = time.time()
move_dezoito = eight_game.largura([[6, 7, 5],[1, 2, 3],[0, 4, 8]])
move_vintequatro = eight_game.largura([[3, 1, 8],[5, 6, 2],[7, 4, 0]])
end_time = time.time()
print(move_vintequatro)
print('Tempo de execução: ', end_time - start_time)
