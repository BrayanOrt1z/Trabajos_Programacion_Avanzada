#!/usr/bin/env python
# coding: utf-8

# # NOMBRE: BRAYAN ANDRÉS ORTIZ GONZÁLEZ
# # ID: 360727

# # Taller 2: Regresión Robotnik
# 
# Ejercicio inspirado en Reggie's Linear Regression de Codecademy (2022) y referencias a películas y videojuegos.
# 
# El Dr. Robotnik ha sido contratado para capturar a un erizo azúl que está provocando fluctuaciones eléctricas en un pueblo lejano de Norteamérica. Se sospecha que su origen sea de naturaleza extraterrestre. Al verse frente a frente, Robotnik se mostró fascinado por la criatura y decidió capturarla para sus experimentos. Desafortunadamente, el erizo demostró poseer una velocidad nunca antes registrada por un organismo vivo, además de la capacidad de liberar energía a medida que incrementaba su velocidad. 
# 
# Después de una aplastante derrota a todos sus drones, Robotnik regresa a su laboratorio para diseñar un dispositivo que pueda soportar la fuerza de choque del erizo. Para ello, necesitará modelar la relación entre la velocidad y la cantidad de energía liberada por el erizo a través de una regresión lineal a partir de los datos recolectados por sus destruidos drones. 
# 
# Una _regresión lineal_ se basa en un grupo de puntos sobre una gráfica sobre la cual se encuentra una línea que se aproxime a estos puntos minimizando el _error_ o la distancia de cada punto hacia la línea. 
# 
# El objetivo de este taller es utilizar ciclos, listas y operaciones aritméticas para crear una función que encuentre la línea de mejor ajuste para una serie de datos dados (en este caso, la velocidad y energía liberada por el erizo). 

# ## Parte 1: Cálculo del Error

# La línea que deseamos encontrar es de la forma:
# 
# $$y = mx + b$$
# 
# donde $m$ es la pendiente de la línea y $b$ el intercepto donde la línea se cruza con el eje $y$.
# 
# Crea una función llamada `get_y()` que reciba como parámetros `m`, `b` y `x` y retorne el valor de `y` para esa `x`. 

# In[35]:


# Función get_y().
def get_y(m, b, x): #Se define la función que representará la ecuación de la recta.
    y = m*x + b
    return y


# Robotnik quiere probar muchos valores de `m` y `b` para determinar cuál produce la línea con el menor error. 
# 
# Para calcular el error entre un punto y una línea, requiere una función llamada `calculate_error()`, que toma `m`, `b` y un punto llamado `point` que es una pareja de valores `(x, y)` (la velocidad y la energía medidas por los drones). La función debe retornar la distancia entre la línea y el punto.  
# 
# Para encontrar esta distancia, considere lo siguiente:
# 1. Obtenga el valor de $x$ del punto y almacénelo en una variable llamada `x_point`.
# 2. Obtenga el valor de $y$ del punto y almacénelo en una variable llamada `y_point`.
# 3. Utilice la función `get_y()` para obtener el valor de $y$ calculado con el valor de `x_point`.
# 4. Calcule la diferencia entre la $y$ calculada con la función `get_y()` y `y_point`
# 5. Retorne el valor absoluto de la distancia (puede usar la función `abs()` para hacer esto).

# In[36]:


# Función calculate_error(m, b, point)
def calculate_error(m, b, point): # Se define la función que calculará el error entre un punto y una línea.
    x_point = point[0]            # Se guarda en la variable x_point, la abcisa de la coordenada "point".
    y_point = point[1]            # Se guarda en la variable y_point, la ordenada de la coordena "point".
    y = get_y(m, b, x_point)      # Se obtiene el nuevo valor de "y" al evaluar "x_point" en la función "get_y". 
    subtract = (y_point)-y        # Se calcula la diferencia entre el valor de "y" actual y el valor de "y" anterior.
    distance = abs(subtract)      # Se calcula el valor absoluto a la diferencia para obtener la distancia en valores positivos.
    return distance               # Aquí se retorna a la variable "distance".


# Probemos la función:

# In[37]:


#En esta línea, y = x, así que el punto (3, 3) debería estar sobre la línea. El error debe ser cero (0):
print(calculate_error(1, 0, (3, 3)))

#El punto (3, 4) debería estar a 1 unidad de distancia de la línea y = x:
print(calculate_error(1, 0, (3, 4)))

#El punto (3, 3) debería estar a 1 unidad de distancia de la línea y = x - 1:
print(calculate_error(1, -1, (3, 3)))

#El punto (3, 3) debería estar a 5 unidades de distancia de la línea y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))


# Los datos de velocidad y energía recolectados por los drones de Robotnik han sido almacenados en una lista llamada `datapoints`:

# In[38]:


datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]


# El primer registro, `(1, 2)`, significa que el erizo produjo una cantidad de energía de $2 GJ$ ($1 GJ = 277.8 kWh$) a una velocidad de $1 m/s$. A una velocidad de $4 m/s$ produjo $4 GJ$. 
# 
# A medida que buscamos una línea que se ajuste a estos datos, necesitaremos una función llamada `calculate_all_error`, que toma la `m` y la `b` que describe una línea, y un conjunto de datos `datapoints`. 
# 
# La función `calculate_all_error` debería iterar a través de cada `point`en `points` y calcular el error de ese punto hacia la línea (usando `calculate_error`). La función debe mantener un acumulador del error total, y luego retornar este valor al terminar de evaluar todos los puntos. 

# In[39]:


# Función calculate_all_error(m, b, datapoints):
def calculate_all_error(m, b, datapoints):       # Se define la función que calculará el error total de un conjunto de puntos. 
    error_acumulador = 0                         # Se inicializá la variable con el valor de cero (0).
    for point in range(len(datapoints)):         # Con este ciclo se recorren todos los elementos de "datapoints"
        variable= datapoints[point]              # Con estas variables se calcula el error de cada punto que se va recorriendo y se van sumando para así obtener el error total.
        error_acumulador += calculate_error(m, b, variable) 
    return error_acumulador


# Probemos la función:

# In[40]:


#Cada punto en este conjunto se encuentra sobre la línea y=x, por lo que el error total debería ser cero (0):
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#Cada punto en este conjunto está a 1 unidad de distancia de y = x + 1, por lo que el error total debería ser de cuatro (4):
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#Cada punto en este conjunto está a 1 unidad de distancia de y = x - 1, por lo que el error total debería ser de cuatro (4):
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))

#Los puntos en este conjunto están a 1, 5, 9, y 3 unidades de distancia de y = -x + 1, respectivamente, 
#por lo que el error total debería ser de 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))


# Robotnik parece satisfecho. Parece que ya tenemos una función que toma una línea y los datos de los drones, y retornar qué tanto error se produce cuando tratamos de encajar la línea con los datos. 
# 
# El siguiente paso es encontrar la `m` y la `b` que minimiza este error, y así, la que mejor se ajusta a los datos.

# ## Parte 2: Probando pendientes e interceptos

# Robotnik considera que la mejor forma de encontrar la línea que mejor se ajusta a los datos es a punta de ensayo y error. Para esto, se debe probar muchas pendientes diferentes (valores de `m`) y muchos interceptos diferentes (valores de `b`), y ver cuál de ellos produce el error más pequeño para los registros de los drones. 
# 
# Usando list comprehension, crea una lista de los posibles `m` a probar. Haz que la lisa `possible_ms` vaya de -10 a 10 (inclusiva) en incrementos de 0.1.
# 
# Pista: (para ver la pista, haz doble clic en la celda para ver el texto oculto) 
# <span style="visibility: hidden;">
#   puedes atravesar los valores en range(-100, 101) y multiplicar cada uno por 0.1
# </span>

# In[41]:


# possible_ms = []
possible_ms = [i*0.1 for i in range(-100, 101)] # Se crea una lista con los posibles valores de "m" en un rango comprendido entre -10 y 10 en pasos de 0.1.


# Ahora, crea una lista de los posibles `b` (`possible_bs`) entre -20 y 20 (inclusivo), en pasos de 0.1:

# In[42]:


# possible_bs = []
possible_bs = [i*0.1 for i in range(-200,201)] # Se crea una lista con los posibles valores de "b" en un rango comprendido entre -20 y 20 en pasos de 0.1.


# Para encontrar el error más pequeño, primero tenemos que crear todas las líneas posibles (`y = mx + b`) a partir de todas las `m` y las `b` posibles (`possible_ms` y `possible_bs`). Después, tenemos que evaluar qué línea produce el menor error total con el conjunto de datos de los registros de los drones (`datapoints`)
# 
# Para esto:
# 1. Crea las variables que estaremos optimizando:
#     * `smallest_error` - debería comenzar en el infinito (`float("inf")`) tal que cualquier error que obtengamos inicialmente sea más pequeño que `smallest_error`.
#     * `best_m` - puede comenzar en cero (0).
#     * `best_b` - puede comenzar en cero (0).
# 2. Itera a través de cada elemento `m` en `possible_ms`.
# 3. Para cada valor de `m`, toma cada valor de `b` en `possible_bs`.
# 4. Si el valor retornado de la función `calculate_all_error` para un valor de `m`, `b` y los `datapoints` es menor que el `smallest_error` actual, cambia los valores de `best_m`, `best_b` y `smallest_error`.
# 
# Al finalizar los ciclos anidados, la variable `smallest_error` debería tener el menor error encontrado, y `best_m` y `best_b` deberían ser los valores que producen el menor error. 

# In[43]:


# Calcular smallest_error, best_m y best_b
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]             # Es la lista de los datos recolectados por el Dr. Robotnik.   
smallest_error = (float("inf"))                                   # Se inicializa la variable en el infinito.
best_m = 0                                                        # Se inicializa la variable con un valor de cero (0).
best_b = 0                                                        # Se inicializa la variable con un valor de cero (0).
for i in range(len(possible_ms)):                                 # Con estos ciclos anidados se recorren todos los posibles  
    ms = possible_ms[i]                                           # valores de la pendiente y de los interceptos.
    for j in range(len(possible_bs)):                             # Luego haciendo uso de la función "calculate_all_error"
        bs = possible_bs[j]                                       # se obtiene el error para luego comparar el error actual con
        current_error = calculate_all_error(ms, bs, datapoints)   # el error anteriormente guardado.
        if current_error < smallest_error:                        # Si se cumple la condición dada entonces se cambian los
            best_m = ms                                           # valores de "best_m" y "best_b" y con esto, se obtiene los
            best_b = bs                                           # valores que producen el menor error.
            smallest_error = current_error
print(f"La pendiente que genera el menor error es: m = {best_m}")
print(f"El intercepto que genera el menor error es: b = {best_b}")
print(f"El menor error encontrado es: {smallest_error}")


# ## Parte 3: Predicciones del Modelo

# Utilizando los valores de `m` y `b` arrojados por nuestro algoritmo para encontrar la línea de mejor ajuste a los datos recopilados por los drones, grafica la línea energía-velocidad utilizando los siguientes comandos:
# ```python
# from matplotlib import pyplot as plt
# x = [i*0.5 for i in range(0,101)]
# y = [m*i + b for i in x]
# plt.plot(x, y)
# plt.show()
# 
# ```
# No olvide cambiar los valores de `m` y `b`.

# In[44]:


# Gráfica de la línea de mejor ajuste
from matplotlib import pyplot as plt                          # En esta sección se encuentra la graficación de "x" y "y".  
x = [i*0.5 for i in range(0, 101)]                            # En la list comprenhension de "y" se ven números con muchos
y = [0.30000000000000004*i + 1.7000000000000002 for i in x]   # decimales ya que no se le dió formato a las variables de
plt.plot(x, y)                                                # donde proceden dichos valores.
plt.show()


# In[ ]:




