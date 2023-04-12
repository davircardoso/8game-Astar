class EightGame():    
    def __init__(self, goal):
        self.goal = goal     
                
    def move(self, father, goal):

        linhas = len(father)
        colunas = len(father[0])
        linha_zero = 0
        col_zero = 0
        abertos = [father]
        explorados = []
        jogadas = 0
        
        while abertos:
            move_list = ['U', 'D', 'L', 'R']
            estado_atual = abertos.pop(0)
            explorados.append(estado_atual)
            
            if estado_atual == goal:
                break
            
            for i in range(linhas):
                for j in range(colunas):
                    if estado_atual[i][j] == 0:
                        linha_zero = i
                        col_zero = j
                        break  

            if linha_zero == 0 and col_zero == 0:
                move_list.remove('U')
                move_list.remove('L')
            elif linha_zero == 0 and col_zero == 1:
                move_list.remove('U')
            elif linha_zero == 0 and col_zero == 2:
                move_list.remove('U')
                move_list.remove('R')
            elif linha_zero == 1 and col_zero == 0:
                move_list.remove('L')
            elif linha_zero == 1 and col_zero == 1:
                pass
            elif linha_zero == 1 and col_zero == 2:
                move_list.remove('R')
            elif linha_zero == 2 and col_zero == 0:
                move_list.remove('D')
                move_list.remove('L')
            elif linha_zero == 2 and col_zero == 1:
                move_list.remove('D')
            elif linha_zero == 2 and col_zero == 2:
                move_list.remove('D')
                move_list.remove('R')

            for move in move_list:
                if move == 'U':
                    temp0 = [row[:] for row in estado_atual]
                    temp0[linha_zero][col_zero], temp0[linha_zero-1][col_zero] = temp0[linha_zero-1][col_zero], temp0[linha_zero][col_zero]
                    if temp0 not in explorados and temp0 not in abertos:
                        abertos.append(temp0)
                elif move == 'D':
                    temp1 = [row[:] for row in estado_atual]
                    temp1[linha_zero][col_zero], temp1[linha_zero+1][col_zero] = temp1[linha_zero+1][col_zero], temp1[linha_zero][col_zero]
                    if temp1 not in explorados and temp1 not in abertos:
                        abertos.append(temp1)
                elif move == 'L':
                    temp2 = [row[:] for row in estado_atual]
                    temp2[linha_zero][col_zero], temp2[linha_zero][col_zero-1] = temp2[linha_zero][col_zero-1], temp2[linha_zero][col_zero]
                    if temp2 not in explorados and temp2 not in abertos:
                        abertos.append(temp2)
                else:
                    temp3 = [row[:] for row in estado_atual]
                    temp3[linha_zero][col_zero], temp3[linha_zero][col_zero+1] = temp3[linha_zero][col_zero+1], temp3[linha_zero][col_zero]
                    if temp3 not in explorados and temp3 not in abertos:
                        abertos.append(temp3)
            jogadas += 1
        
        qtd_jogadas = 'Quantidade de jogadas: ' + str(jogadas)
            
        return explorados, qtd_jogadas
  
                
eight_game = EightGame([[1,2,3],[4,5,6],[7,8,0]])

move = eight_game.move([[1,2,3],[4,0,6],[7,5,8]], [[1,2,3],[4,5,6],[7,8,0]])

print(move)

