import time
from search import Busca

jogo8 = Busca()

start_time = time.time()
#move_dezoito_largura = jogo8.largura([[6, 7, 5],[1, 2, 3],[0, 4, 8]])
#move_vintequatro_largura = jogo8.largura([[3, 1, 8],[5, 6, 2],[7, 4, 0]])
move_vintequatro_manhattan = jogo8.a_estrela_manhattan([[3, 1, 8],[5, 6, 2],[7, 4, 0]])
move_dezoito_manhattan = jogo8.a_estrela_manhattan([[6, 7, 5],[1, 2, 3],[0, 4, 8]])
#move_trintaum_manhattan = jogo8.a_estrela_manhattan([[1, 2, 3],[4, 5, 6],[8, 7, 0]])
move_ss = jogo8.a_estrela_manhattan([[1, 2, 3],[4, 5, 6],[8, 7, 0]])
move_dezoito_complex = jogo8.a_estrela_heuristica_complexa([[1, 2, 3],[4, 5, 6],[8, 7, 0]])
end_time = time.time()
#print('Utilizando Largura para 18 Jogadas', move_dezoito_largura)
#print('Utilizando Largura para 24 Jogadas', move_vintequatro_largura)
print('Utilizando Heurística Simples para 18 Jogadas', move_ss)
#print('Utilizando Heurística Simples para 24 Jogadas', move_vintequatro_manhattan)
#print('Utilizando Heurística Simples para 31 Jogadas', move_trintaum_manhattan)
print( 'Utilizando Heurística Complexa para 18 Jogadas', move_dezoito_complex)
print('Tempo de execução: ', end_time - start_time)