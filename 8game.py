class EightGame():    
    def __init__(self, given_list, result_list):
        self.result_list = result_list
        self.given_list = given_list
        self.sons_list = []
                
        
    def move(self, father):
        move_list = ['U', 'D', 'L', 'R']
        
        for lenght in range(len(father)):
            for i in father[lenght]:
                if lenght == 0:
                    if i == 0:
                        print(father.index(i))
                        if  father[lenght].index(i) == 0:
                            move_list.remove('U','L')
                        if  father[lenght].index(i) == 1:
                            move_list.remove('U')
                        if  father[lenght].index(i) == 2:
                            move_list.remove('R','U')
                if lenght == 1:
                    if i == 0:
                        if  father[lenght].index(i) == 0:
                            move_list.remove('L')
                        if  father[lenght].index(i) == 2:
                            move_list.remove('R')
                if lenght == 2:
                    if i == 0:
                        if father[lenght].index(i) == 0:
                            move_list.remove('D','L')
                        elif  father[lenght].index(i) == 1:
                            move_list.remove('D')
                        elif  father[lenght].index(i) == 2:
                            move_list.remove('R','D')
                    
        return move_list, father
                    
    def realize_move(self, move_list, father):
        for i in range(len(move_list)):
            j = 0
            for move in move_list:
                if move == 'U' and i != 0:
                    temp = father[i][j]
                    father[i][j] = father[i-1][j]
                    father[i-1][j] = temp
                    self.sons_list.append(temp)
                if move == 'D' and i != 2:
                    temp = father[i][j]
                    father[i][j] = father[i+1][j]
                    father[i+1][j] = temp
                    self.sons_list.append(temp)
                if move == 'L' and j != 0:
                    temp = father[i][j]
                    father[i][j] = father[i][j-1]
                    father[i][j-1] = temp
                    self.sons_list.append(temp)
                if move == 'R' and j != 2:
                    temp = father[i][j]
                    father[i][j] = father[i][j+1]
                    father[i][j+1] = temp
                    self.sons_list.append(temp)
                else:
                    pass
            j += 1       
        return self.sons_list
                    
                
                
eight_game = EightGame([[1,2,3],[4,0,6],[7,5,8]], [[1,2,3],[4,5,6],[7,8,0]])

move = eight_game.move([[1,2,3],[4,0,6],[7,5,8]])
print(move)

print(eight_game.realize_move(move[0],move[1]))