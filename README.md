# Simulador de Algoritmos de Planificación de Procesos (FIFO, LIFO y Round Robin)

Este proyecto implementa y compara tres algoritmos clásicos de planificación de procesos del área de Sistemas Operativos: FIFO, LIFO y Round Robin.
El usuario ingresa un conjunto de tareas con su tiempo inicial (ti) y tiempo de ejecución (t), y el programa simula la ejecución de cada algoritmo, genera sus tablas finales y calcula métricas de eficiencia.

---

## 📌 Caracteristicas Principales

* Entrada dinámica del número de tareas.
* Cada tarea contiene:
    * *ti* → tiempo inicial
    * *t* → tiempo de ejecución
    * *tf* → tiempo final calculado
    * *T, E, I* → métricas por tarea
    * *Completed* → estado de ejecución
* Implementación completa de:
    * **FIFO** (First In, First Out)
    * **LIFO** (Last In, First Out)
    * **Round Robin** (con quantum definido por el usuario)
* Comparación automática entre algoritmos usando la métrica *I* (Índice de rendimiento).
* Medición del tiempo de ejecución real (perf_counter()).
* Tablas formateadas para visualización clara.

---
## 🧠 Descripción de los algoritmos
###  FIFO (First In, First Out)

Las tareas se ejecutan en el orden en que llegan.
El algoritmo avanza el reloj (*clk*) hasta el tiempo inicial mínimo (*x*), luego busca siempre la primera tarea disponible cuya condición *ti ≤ clk* sea verdadera y que no esté completada. Una vez seleccionada, calcula su tiempo final *tf = t + clk*, actualiza *clk* y marca la tarea como completada. Si no hay tareas disponibles en un instante dado, incrementa *clk* simulando tiempo ocioso.

###  LIFO (Last In, First Out)

Las tareas se ejecutan en orden inverso al de llegada.
La lógica es equivalente a FIFO, pero la búsqueda de tareas comienza desde la parte inferior de la tabla (las tareas más recientes). Al finalizar, se reintegran los valores de *tf* en el orden original.

###  Round Robin

Utiliza ejecución por rebanadas de tiempo (quantum).
Cada tarea recibe un intervalo fijo q para ejecutarse.
Si *t ≤ q*, la tarea finaliza inmediatamente.
Si *t > q*, se descuenta q de su tiempo de ejecución y la tarea queda pendiente para una ronda posterior.
El algoritmo mantiene un seguimiento del reloj y del estado de cada tarea hasta completarlas todas.

---

## 📊 Métricas calculadas en cada algoritmo

Para cada tarea:

* ```T = tf – ti```
* ```E = T – t```
* ```I = t / T```

Y para el algoritmo completo se calcula el promedio de cada metrica por todas las tareas, y se utilizan los promedios I para comparar los algoritmos y determinar cuál fue más eficiente.

---

## 🖥️ Salida del programa

El programa imprime:

* Tabla completa del algoritmo con columnas:

    ```  Nombre | ti | t | tf | T | E | I | Completed ```

* Promedio de *T, E e I*
* Tiempo real de ejecución del algoritmo
* Algoritmo más eficiente según el valor de *I*
