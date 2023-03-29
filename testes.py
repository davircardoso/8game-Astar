"""for length in range(len(self.given_list)):
            for i in range(len(self.given_list[length])):
                for j in range(len(self.given_list[length][i])):
                    if self.given_list[length][i][j] == 0:
                        if i == 0:
                            move_list.remove('U')
                        if i == 2:
                            move_list.remove('D')
                        if j == 0:
                            move_list.remove('L')
                        if j == 2:
                            move_list.remove('R')
                        
                        for move in move_list:
                            if move == 'U':
                                temp = self.given_list[length][i][j]
                                self.given_list[length][i][j] = self.given_list[length][i-1][j]
                                self.given_list[length][i-1][j] = temp
                            if move == 'D':
                                temp = self.given_list[length][i][j]
                                self.given_list[length][i][j] = self.given_list[length][i+1][j]
                                self.given_list[length][i+1][j] = temp
                            if move == 'L':
                                temp = self.given_list[length][i][j]
                                self.given_list[length][i][j] = self.given_list[length][i][j-1]
                                self.given_list[length][i][j-1] = temp
                            if move == 'R':
                                temp = self.given_list[length][i][j]
                                self.given_list[length][i][j] = self.given_list[length][i][j+1]
                                self.given_list[length][i][j+1] = temp
                                
                        move_list = ['U', 'D', 'L', 'R']"""
                        
lista = [[3,2,1,0],[1,2,3,4]]

for i in range(len(lista)):
    for k in lista[i]:
        print(k)
        print(lista[i].index(k))