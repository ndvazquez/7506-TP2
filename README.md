# 7506-Competencia

[Link a la competencia](https://www.kaggle.com/c/trocafone)

### Como funcionan las cosas: 

+ Todos los datasets y archivos deben estar en la carpeta 'data' local de cada uno.

+ El dataset con eventos se debe llamar 'events.csv' (unico dataset que se va a renombrar, por comodidad).

+ Feature Gathering:
 1. levantar todos los datasets necesarios en una celda del notebook.
 2. hacer todo lo que se deba hacer.
 3. guardar los features encontrados en un .csv en la carpeta 'data' local para futuro uso.

+ Modelos de ML:
 1. leer todos los .csv necesarios de la carpeta 'data'.
 2. armar el dataframe (**que se va a usar durante todo el notebook**) en una celda.
 3. hacer todo lo que hay que hacer

+ Algunas cosas importantes:
 + Siempre hay que usar el mismo dataframe durante todo el modelado, para que sea facil cambiar las features y volver a correr todo.
 + Cuando se hace el feature gathering la idea es dejar todo armado para que venga otro, corra todo y tenga el .csv en 'data'.
 + Es muy importante hacer el join de todos los .csv a un mismo dataframe en un solo bloque del notebook. Para facilitar el cambio del mismo. No hay que agregar features luego de ese bloque, ya que si otra persona quiere correr el notebook con sus features va a tener que ir a buscar donde fueron agregadas otras features para sacarlas.