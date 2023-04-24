import time
from search import Busca

jogo8 = Busca()

start_time = time.time()
move_cinco_largura = jogo8.largura([[4, 1, 2],[0, 5, 3],[7, 8, 6]])
#move_dezoito_largura = jogo8.largura([[6, 7, 5],[1, 2, 3],[0, 4, 8]])
#move_vintequatro_largura = jogo8.largura([[3, 1, 8],[5, 6, 2],[7, 4, 0]])
move_cinco_manhattan = jogo8.a_estrela_manhattan([[4, 1, 2],[0, 5, 3],[7, 8, 6]])
move_cinco_euclidiana = jogo8.a_estrela_euclidiana([[4, 1, 2],[0, 5, 3],[7, 8, 6]])
#move_dezoito_manhattan = jogo8.a_estrela_manhattan([[6, 7, 5],[1, 2, 3],[0, 4, 8]])
#move_vintequatro_manhattan = jogo8.a_estrela_manhattan([[3, 1, 8],[5, 6, 2],[7, 4, 0]])
#move_dezoito_euclidiana = jogo8.a_estrela_euclidiana([[6, 7, 5],[1, 2, 3],[0, 4, 8]])
#move_vintequatro_euclidiana = jogo8.a_estrela_euclidiana([[3, 1, 8],[5, 6, 2],[7, 4, 0]])

end_time = time.time()

print('Utilizando Largura para 5 Jogadas', move_cinco_largura)
print('Utilizando Heurística Simples para 5 Jogadas', move_cinco_euclidiana)
print('Utilizando Heurística Complexa para 5 Jogadas', move_cinco_manhattan)
#print('Utilizando Largura para 18 Jogadas', move_dezoito_largura)
#print('Utilizando Largura para 24 Jogadas', move_vintequatro_largura)
#print( 'Utilizando Heurística Simples para 18 Jogadas', move_dezoito_euclidiana)
#print( 'Utilizando Heurística Simples para 24 Jogadas', move_vintequatro_euclidiana)
#print('Utilizando Heurística Complexa para 18 Jogadas', move_dezoito_manhattan)
#print('Utilizando Heurística Complexa para 24 Jogadas', move_vintequatro_manhattan)

print('Tempo de execução: ', end_time - start_time)