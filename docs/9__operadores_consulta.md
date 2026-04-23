
Los métodos de consulta permiten recuperar la información almacenada en una colección de MongoDB. Mediante estos métodos podemos obtener documentos completos o parciales, aplicar filtros, ordenar los resultados y limitar la cantidad de documentos devueltos. 

El método principal de consulta en MongoDB es find(). Además, existen otros métodos que complementan y amplían su funcionamiento, como **sort(), limit(), skip() y pretty().

Estos métodos pueden utilizarse conjuntamente con find(), encadenándolos al final de la consulta y separados por un punto (.).

De forma resumida:  
- **sort()** controla el orden de los resultados.  
- **limit()** controla cuántos documentos se devuelven.  
- **skip()** controla cuántos documentos se ignoran.  
- **pretty()** mejora la presentación del resultado por pantalla, sin modificar los datos.  

Estos métodos **no cambia el contenido de los documentos, ni afecta al rendimiento de la consulta**. Se pueden combinar libremente y son fundamentales para implementar paginación y listados ordenados.

Sintaxis general:

        db.coleccion.find(filtro, proyeccion)
                    .sort(criterio)
                    .limit(numero)
                    .skip(numero)
                    .pretty()
        ``

#### sort()
  
El método sort() se utiliza para ordenar los documentos devueltos por una consulta según el valor de uno o varios campos.
Como parámetro recibe un documento JSON, donde:

- 1 indica orden ascendente
- -1 indica orden descendente

Si se indican varios campos, MongoDB ordenará: primero por el primer campo, en caso de empate, por el segundo, y así sucesivamente.

Ejemplo: ordenar por precio (ascendente)

    > db.libro.find({} , {titulo:1 , precio:1 , editorial:1}).sort({precio:1})  

    { "_id" : "9788499088075", "titulo" : "El ladrón de libros", "editorial" : "Debolsillo", "precio" : 9.45 }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1", "editorial" : "Gigamesh", "precio" : 9.5 }  
    { "_id" : "9788415140054", "titulo" : "La princesa de hielo", "editorial" : "Embolsillo", "precio" : 11 }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "precio" : 15.9 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "editorial" : "Planeta", "precio" : 17.23 }  
    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "editorial" : "Planeta", "precio" : 21.75 }  
    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "editorial" : "Plaza & Janes", "precio" : 21.75 }

Devuelve una lista con todos los campos y sus valores de la clave. La secuencia es: campo1 valor1 campo2 valor2 ... 
Pero no podemos fiarnos de que el orden sea el mismo orden que cuando lo definimos.

Ejemplo: Ordenación por varios campos, editorial  (ascendente) y precio  (descendente)

    > db.libro.find({} , {titulo:1 , precio:1 , editorial:1}).sort({editorial:1 , precio:-1})  

    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "precio" : 15.9 }  
    { "_id" : "9788499088075", "titulo" : "El ladrón de libros", "editorial" : "Debolsillo", "precio" : 9.45 }  
    { "_id" : "9788415140054", "titulo" : "La princesa de hielo", "editorial" : "Embolsillo", "precio" : 11 }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1", "editorial" : "Gigamesh", "precio" : 9.5 }  
    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "editorial" : "Planeta", "precio" : 21.75 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "editorial" : "Planeta", "precio" : 17.23 }  
    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "editorial" : "Plaza & Janes", "precio" : 21.75 }

Observe cómo el primero es el que no tiene editorial (equivalente a null). Y cómo que hay dos de la editorial Planeta, aparece primero el más caro, y después el más barato (ya que el precio está en orden descendente).

#### limit()

El método limit() limita el número de documentos devueltos por la consulta a n documentos.

Ejemplo: 

    > db.libro.find(
          {},
          { titulo: 1, precio: 1, editorial: 1 }
        ).limit(3)


    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "editorial" : "Planeta", "precio" : 21.75 }  
    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "editorial" : "Plaza & Janes", "precio" : 21.75 }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1", "editorial" : "Gigamesh", "precio" : 9.5 }

Si el número de documentos que cumple la consulta es menor que n, se devolverán todos los disponibles. 

En el siguiente ejemplo:

    > db.libro.find({editorial:"Planeta"} , {titulo:1 , precio:1 , > editorial:1}).limit(3)  

    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "editorial" : "Planeta", "precio" : 21.75 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "editorial": "Planeta", "precio" : 17.23 }

Vemos que el resultado de la consulta es de dos documentos, aunque ponemos límite(3), se devolverá 2 documentos, ya que de la editorial Planeta sólo hay dos libros.
    

#### skip()

El método skip() permite omitir los primeros n documentos del resultado. Si hubiera menos documentos de los que se salten, pues no se mostraría ninguna.

    > db.libro.find({} , {titulo:1 , precio:1 , editorial:1}).skip(2)  

    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1", "editorial" : "Gigamesh", "precio" : 9.5 }  
    { "_id" : "9788499088075", "titulo" : "El ladrón de libros", "editorial" : "Debolsillo", "precio" : 9.45 }  
    { "_id" : "9788415140054", "titulo" : "La princesa de hielo", "editorial" : "Embolsillo", "precio" : 11 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "editorial" : "Planeta", "precio" : 17.23 }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "precio" : 15.9 }

MongoDB ignorará los dos primeros documentos y mostrará el resto.


#### pretty()

El método pretty() se utiliza para mejorar la presentación del resultado de una consulta en MongoDB. Hace que los documentos devueltos por un find() se muestren de forma más legible y ordenada, con saltos de línea e indentación.

Es no modifica los datos ni la consulta, únicamente afecta a cómo se muestran los resultados por pantalla.

Lo aplicaremos a los libros, donde tenemos más documentos. Y no mostramos todos los campos, para una mejor lectura:

        >  db.libro.find(      { editorial: "Planeta" },      { titulo: 1, precio: 1, editorial: 1 }    ).pretty()


Este sería el resultado utilizando el método pretty():

        {
          "_id" : "9788408117117",
          "titulo" : "Circo Máximo",
          "editorial" : "Planeta",
          "precio" : 21.75
        }
        {
          "_id" : "9788408113331",
          "titulo" : "Las carreras de Escorpio",
          "editorial" : "Planeta",
          "precio" : 17.23
        }
 
#### **Encadenamiento de métodos**

Los métodos de consulta en MongoDB pueden encadenarse para construir consultas más completas y precisas. El encadenamiento consiste en aplicar varios métodos consecutivamente sobre el resultado de un find().

Por ejemplo: 

        db.libro.find({ enstock: true }, { titulo: 1, precio: 1 })
                .sort({ precio: -1 })
                .limit(3)
                .pretty()

Esta consulta realiza las siguientes operaciones, en orden:

1. Filtra los libros que están en stock.
2. Muestra únicamente los campos titulo y precio.
3. Ordena los resultados por precio de forma descendente.
4. Limita el resultado a 3 documentos.
5. Mejora la presentación del resultado mediante pretty().

**Combinación de sort(), skip() y limit()**

Los métodos sort(), skip() y limit() pueden combinarse para obtener subconjuntos concretos de resultados, lo que resulta especialmente útil para paginación o para seleccionar posiciones concretas dentro de un listado ordenado.

Nota importante: Aunque estos métodos pueden combinarse libremente, el orden lógico es relevante. En la práctica, primero se debe ordenar (sort()), y después saltar (skip()) y limitar (limit()) resultados.

Ejemplo: Obtener el segundo y tercer libro más caro.

    > db.libro.find({} , {titulo:1 , precio:1 , > editorial:1}).sort({precio:-1}).skip(1).limit(2)  

    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "editorial" : "Plaza & Janes", "precio" : 21.75 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "editorial" : "Planeta", "precio" : 17.23 }

En este caso: 
- Se ordenan los libros por precio de mayor a menor.
- Se descarta el primero (el más caro).
- Se recuperan los dos siguientes.

### **Búsquedas en documentos embebidos**

Para realizar búsquedas en campos que a su vez son objetos (o documentos
dentro de documentos, en la terminología de Mongo), sólo debemos poner la ruta de
las llaves separando por medio de puntos, y cuidar de ponerla entre comillas.

Así, por ejemplo, vamos a hacer una consulta sobre la colección de alumnos, que
eran unos documentos en los que existía algún campo de tipo objeto.

    > db.alumnos.find().pretty()  

    {  
        "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
        "nombre" : "Abel",  
        "apellidos" : "Bernat Cantera",  
        "edad" : 22,  
        "dirección" : {  
        "calle" : "Mayor",  
        "numero" : 7,  
        "cp" : "12502"  
        },  
        "nota" : [  
            9.5,  
            9  
        ]  
    }  
    {  
    "_id" : ObjectId("56dfdbd136d8b095cb6bd57a"),  
    "nombre" : "Berta",  
    "apellidos" : "Bernat Cantero"  
    }

Se podrían mostrar los documentos (los alumnos) que viven en el código postal
12502. Nos debe salir el único alumno del que tenemos la dirección, que justamente tiene
este código postal. Recuerde que en la clave (realmente clave.subclave), debe ir
entre comillas. Hemos puesto al final **pretty()** para una mejor lectura, pero
evidentemente no es necesario.

    > db.alumnos.find({"dirección.cp": "12502"}).pretty()  

    {  
        "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
        "nombre" : "Abel",  
        "apellidos" : "Bernat Cantera",  
        "edad" : 22,  
        "dirección" : {  
            "calle" : "Mayor",  
            "numero" : 7,  
            "cp" : "12502"  
        },  
        "nota" : [  
            9.5,  
            9  
        ]  
    }

Y funcionaría igual con cualquier número de subniveles, es decir, documentos
que tienen objetos, los cuales tienen objetos, ... Y también con otros tipos
de operadores, o expresiones regulares, ...

Por ejemplo, todos los alumnos de Castellón (el código postal debe empezar por
12 y contener 3 cifras más, es decir, carácter del 0 al 9 y 3 veces.

    > db.alumnos.find({"dirección.cp": /^12[0-9]{3}/}).pretty()  

    {  
        "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
        "nombre" : "Abel",  
        "apellidos" : "Bernat Cantera",  
        "edad" : 22,  
        "dirección" : {  
            "calle" : "Mayor",  
            "numero" : 7,  
            "cp" : "12502"  
        },  
        "nota" : [  
            9.5,  
            9  
        ]  
    }

  
