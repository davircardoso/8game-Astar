import time
from search import Search

eight_game = Search()

start_time = time.time()
move_dezoito = eight_game.largura([[6, 7, 5],[1, 2, 3],[0, 4, 8]])
move_vintequatro = eight_game.largura([[3, 1, 8],[5, 6, 2],[7, 4, 0]])
end_time = time.time()
print(move_vintequatro)
print('Tempo de execução: ', end_time - start_time)