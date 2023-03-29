
result_list = [[1,2,3],[4,5,6],[7,8,0]]

pai = [[1,2,3],[4,6,0],[7,5,8]]

given_list = [[1,2,3],[4,0,6],[7,5,8]]

total_list = [[[1,2,3],[4,0,6],[7,5,8]], [[[1,2,3],[4,6,0],[7,5,8]],[[1,2,3],[0,4,6],[7,5,8]]]]

"""Implementação do calculo do custo para o jogo dos 8"""

def h_value(result, given):
    s = 0
    for j in range(len(result)):
        k = 0
        for h in result[j]:
            if h != given[j][k]:
                s += 1
            k += 1
    return s

def g_value(total):
    h = len(total) - 1
    return h
    
def manhattan_distance(h, g):
   sum  = h + g
   return sum

print(manhattan_distance(h_value(pai, given_list), g_value(total_list)))

    

