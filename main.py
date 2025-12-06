import copy
from functions import print_matrix, datos_tareas, headers_matrix, fill_E, fill_I, fill_T, FIFO_result, LIFO_result, Round_Robin_result

m = int(input("Ingrese el numero de tareas que desea realizar: "))
q= int(input("Ingrese el quantum: "))

tabla = [[0 for col in range(8)] for row in range(m+1)]
tabla= headers_matrix(tabla)
tabla = datos_tareas(tabla)
copy1_tabla = copy.deepcopy(tabla)
copy2_tabla= copy.deepcopy(tabla)

fifo= FIFO_result(tabla, m)
lifo=LIFO_result(copy1_tabla, m)
round_robin = Round_Robin_result(copy2_tabla, m, q)

# Compara resultados
results = {"FIFO": fifo, "LIFO": lifo, "Round Robin": round_robin}
max_algorithm = max(results, key=results.get)
print()
print(f"El algoritmo con mayor eficiencia es: {max_algorithm} con un valor I de {results[max_algorithm]}")







