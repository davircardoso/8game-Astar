class EightGame():    
    def __init__(self, given_list, result_list):
        self.result_list = result_list
        self.given_list = given_list
        self.sons_list = []
                
        
    def move(self, father):
        move_list = ['U', 'D', 'L', 'R']
        
        for lenght in range(len(father)):
            for i in self.result_list[lenght]:
                if lenght == 0:
                    if i == 0:
                        print(father.index(i))
                        if  father[lenght].index(i) == 0:
                            move_list.remove('U','L')
                        if  father[lenght].index(i) == 1:
                            move_list.remove('U')
                        if  father[lenght].index(i) == 2:
                            move_list.remove('R','U')
                    else:
                        pass
                if lenght == 1:
                    if i == 0:
                        if  father[lenght].index(i) == 0:
                            move_list.remove('L')
                        if  father[lenght].index(i) == 1:
                            move_list.remove()
                        if  father[lenght].index(i) == 2:
                            move_list.remove('R')
                    else:
                        pass
                if lenght == 2:
                    if i == 0:
                        if father[lenght].index(i) == 0:
                            move_list.remove('D','L')
                        elif  father[lenght].index(i) == 1:
                            move_list.remove('D')
                        elif  father[lenght].index(i) == 2:
                            move_list.remove('R','D')
                        else:
                            pass
                    else:
                        pass
                    
        return move_list, father
                    
    def realize_move(self, move_list):
        for i in range(len(self.given_list)):
            j = 0
            for move in move_list:
                if move == 'U':
                    temp = self.given_list[i][j]
                    self.given_list[i][j] = self.given_list[i-1][j]
                    self.given_list[i-1][j] = temp
                    self.sons_list.append(temp)
                if move == 'D':
                    temp = self.given_list[i][j]
                    self.given_list[i][j] = self.given_list[i+1][j]
                    self.given_list[i+1][j] = temp
                    self.sons_list.append(temp)
                if move == 'L':
                    temp = self.given_list[i][j]
                    self.given_list[i][j] = self.given_list[i][j-1]
                    self.given_list[i][j-1] = temp
                    self.sons_list.append(temp)
                if move == 'R':
                    temp = self.given_list[i][j]
                    self.given_list[i][j] = self.given_list[i][j+1]
                    self.given_list[i][j+1] = temp
                    self.sons_list.append(temp)
                j += 1
        return self.sons_list
                    
                
                
eight_game = EightGame([[1,2,3],[4,0,6],[7,5,8]], [[1,2,3],[4,5,6],[7,8,0]])

print(eight_game.realize_move(eight_game.move([[1,2,3],[4,0,6],[7,5,8]])))