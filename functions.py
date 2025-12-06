import copy
import time
import math

def print_matrix(matrix): 
    """    
    Prints a matrix with items aligned
    -> param matrix: list
    """
    for row in matrix:
        for item in row:
            print (f"{item:<9}", end="")
        print()

def datos_tareas(matrix):
    """
    Asks input for cells in rows 1 and 2 in columns 0->Name ; 1-> Tiempo Inicial; 2-> Tiempo de ejecucion
    -> param matrix: list
    """
    counter=0
    for row in matrix[1:]:
        counter+=1
        print(f"Tarea {counter} :")
        print("---------------")
        row[0]= input("Nombre: ")
        row[1]= int(input("Tiempo inicial: "))
        row[2]= int(input("Tiempo de ejecucion: "))
        row[7]=False
        print()

    return matrix

def headers_matrix(matrix):
    """
    Names headers of columns for given matrix
    : 0-> "" ; 1-> ti ; 2-> t ; 3-> tf ; 4-> T ; 5-> E ; 6-> I ; 7 -> Completed
    ->param matrix: list
    """
    matrix[0][0]=""
    matrix[0][1]="ti"
    matrix[0][2]="t"
    matrix[0][3]="tf"
    matrix[0][4]="T"
    matrix[0][5]="E"
    matrix[0][6]="I"
    matrix[0][7]="Completed"

    return matrix

def fill_T(matrix):
    for row in matrix[1:]:
        row[4]=row[3]-row[1]

def fill_E(matrix):
    for row in matrix[1:]:
        row[5]=row[4]-row[2]

def fill_I(matrix):
    for row in matrix[1:]:
        row[6]=round(row[2]/row[4], 4)

def get_T(matrix, m):
    T=0
    for row in matrix[1:]:
        T=T+row[4]
    return round(T/m, 4)

def get_E(matrix, m):
    E=0
    for row in matrix[1:]:
        E=E+row[5]
    return round(E/m, 4)
    
def get_I(matrix, m):
    I=0
    for row in matrix[1:]:
        I=I+row[6]
    return round(I/m, 4)

def get_stats(matrix, m):
    #get averages
    T= get_T(matrix, m)
    E= get_E(matrix, m)
    I= get_I(matrix, m)
    #print them
    print(f"{"Los valores promedios son: ":^65}")
    print(f"T = {T} , E = {E} , I = {I}".center(65))
    return I

def copyColumns(matrixA, matrixB, n):
    """Copy the column n from A to B"""
    rows=0
    for row in matrixA:
        matrixB[rows][n]= row[n]
        rows=rows+1



def FIFO_result(matrix, m):
    """
    FIFO_result
    -> gets and prints table (matrix) for the FIFO process management
    :param matrix: list
    :param m: number of tasks to be done
    """
    clk=0
    k=0
    x= min(row[1] for row in matrix[1:]) #min ti

    while (clk<x):
        clk=clk+1

    #starts process
    start = time.perf_counter()
    print(f"Start time: {start}")
    ###########################

    while (k<m):
        for row in matrix[1:]:
            tin= row[1]
            completed= row[7]
            if (tin<=clk and not(completed)):
                row[3]= row[2]+clk  #tfn = tn +clk
                clk=row[3]          #clk = tfn
                k=k+1               #update nbr of tasks
                row[7]=True         #update task status
                break  # Exit the for loop and restart the while loop (start searching for tasks again)
        else:
            clk = clk + 1  # Increment clk only if no break occurred - (did not find any task that can be executed)

    #ends process
    end = time.perf_counter()
    print(f"End time: {end}")
    ###########################
    
    #print(clk)
    #get_stats
    fill_T(matrix)
    fill_E(matrix)
    fill_I(matrix)
    
    print("----------------------------------------------------------------")
    print(f"{"FIFO - Process":^65}")
    print("----------------------------------------------------------------")
    print_matrix(matrix)
    I= get_stats(matrix, m)
    print(f"Tiempo para FIFO: {end - start:.10f} seconds".center(64))
    return I


def LIFO_result(matrix, m):
    """
    FIFO_result
    -> gets and prints table (matrix) for the FIFO process management
    :param matrix: list
    :param m: number of tasks to be done
    """
    clk=0
    k=0
    x= min(row[1] for row in matrix[1:]) #min ti

    while (clk<x):
        clk=clk+1

    reverse_matrix= list(reversed(matrix))
    #starts process
    start = time.perf_counter()
    print(f"Start time: {start}")
    ###########################
    while (k<m):
        for row in reverse_matrix[:-1]:
            tin= row[1]
            completed= row[7]
            if (tin<=clk and not(completed)):
                row[3]= row[2]+clk  #tfn = tn +clk
                clk=row[3]          #clk = tfn
                k=k+1               #update nbr of tasks
                row[7]=True         #update task status
                break  # Exit the for loop and restart the while loop (start searching for tasks again)
        else:
            clk = clk + 1  # Increment clk only if no break occurred - (did not find any task that can be executed)

    #ends process
    end = time.perf_counter()
    print(f"End time: {end}")
    ###########################

    reverse_matrix= list(reversed(reverse_matrix))
    #Copy the column n from A to B without the header
    copyColumns(reverse_matrix, matrix, 3)

    #print(clk)
    #get_stats
    fill_T(matrix)
    fill_E(matrix)
    fill_I(matrix)
    
    print("----------------------------------------------------------------")
    print(f"{"LIFO - Process":^65}")
    print("----------------------------------------------------------------")
    print_matrix(matrix)
    I = get_stats(matrix, m)
    print(f"Tiempo para LIFO: {end - start:.10f} seconds".center(64))
    return I

def Round_Robin_result(matrix, m, q):
    """
    RR_result
    -> gets and prints table (matrix) for the RR- process management
    :param matrix: list
    :param m: number of tasks to be done
    :param q: quantum
    """

    matrix_copy= copy.deepcopy(matrix)
    clk=0
    k=0
    x= min(row[1] for row in matrix_copy[1:]) #min ti

    #starts process
    start = time.perf_counter()
    print(f"Start time: {start}")
    ###########################
    while (clk<x):
        clk=clk+1


    while (k<m):
        found = False
        for row in matrix_copy[1:]:
            tin= row[1]
            completed= row[7]
            tn= row[2]
            if (tin<=clk and not(completed)):
                #si la encontro

                #La puede ejecutar totalmente
                if(tn<=q):
                    row[3]= row[2]+clk  #tfn = tn +clk
                    row[2]=0 #OPCIONAL --> tn=0
                    clk=row[3]          #clk = tfn
                    row[7]=True         #update task status
                    k=k+1               #update nbr of tasks 
                    found = True  

                #la puede ejecutar parcialmente
                else:
                    row[2]= row[2]-q  # tn= tn - q
                    clk= clk + q # clk = clk +q
                    
        if not found: #no la encontro
            clk = clk + 1  # Increment clk only if no break occurred - (did not find any task that can be executed)

    #ends process
    end = time.perf_counter()
    print(f"End time: {end}")
    ###########################
    copyColumns(matrix_copy, matrix, 3)
    #print(clk)
    #get_stats
    fill_T(matrix)
    fill_E(matrix)
    fill_I(matrix)
    
    print("----------------------------------------------------------------")
    print(f"{"Round Robin - Process":^65}")
    print("----------------------------------------------------------------")
    print_matrix(matrix)
    I=get_stats(matrix, m)
    print(f"Tiempo para Round Robin: {end - start:.10f} seconds".center(64))
    return I


