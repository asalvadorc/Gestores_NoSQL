
Hasta ahora, en las sentencias find(), update() y delete() hemos utilizado filtros basados principalmente en comparaciones de igualdad, es decir, hemos comprobado si el valor de un campo coincide con un valor concreto. Como en el ejemplo de consulta que devuelve todos los documentos de la colección alumnos cuya clave nombre tenga el valor "Rebeca".

        db.alumnos.find( { nombre : "Rebeca" } )

Sin embargo, en muchos casos es necesario definir criterios de búsqueda más complejos, como comparar valores mayores o menores, trabajar con rangos o combinar varias condiciones en una misma consulta.

Para ello, MongoDB proporciona los **operadores de consulta (query operators)**, que se utilizan dentro de los filtros y permiten realizar _comparaciones, combinaciones lógicas y búsquedas más avanzadas_, ampliando así las posibilidades de consulta sobre las colecciones.


#### Operadores de comparación

Los operadores de comparación permiten comparar el valor de un campo con un valor concreto. Gracias a estos operadores, podemos ir más allá de la igualdad y realizar consultas que busquen valores mayores, menores, distintos o dentro de un rango.

Estos operadores se utilizan dentro de los filtros de las sentencias find(), update() y delete(), y se expresan mediante documentos JSON.

Operadores:

* **`$eq`** → comprueba si los valores son iguales
* **`$ne`** → comprueba si los valores son distintos
* **`$gt`**  → comprueba si el valor es mayor que otro
* **`$gte`** → comprueba si el valor es mayor o igual que otro
* **`$lt`**  → comprueba si el valor es menor que otro
* **`$lte`** → comprueba si el valor es menor o igual que otro

Sintaxis:

        clave: { $operador: valor }

Así por ejemplo, la siguiente consulta muestra los libros cuyo precio es superior a 10 €:

        db.libro.find(
          { precio: { $gt: 10 } },
          { titulo: 1, precio: 1 }
        )

  
    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "precio" : 21.75 }  
    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "precio" : 21.75 }  
    { "_id" : "9788415140054", "titulo" : "La princesa de hielo", "precio" : 11 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "precio" : 17.23 }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "precio" : 15.9 }

**Comparaciones por rango**

Es posible combinar varios operadores de comparación sobre un mismo campo.

Por ejemplo, para obtener los libros cuyo precio esté entre 10 y 20 €:

        > db.libro.find(
          { precio: { $gt: 10, $lt: 20 } },
          { titulo: 1, precio: 1 }
        )

    > db.libro.find( { precio : { $gt : 10 , $lt:20 } } , { titulo:1 , precio:1 })
  
    { "_id" : "9788415140054", "titulo" : "La princesa de hielo", "precio" : 11 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "precio" : 17.23 }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "precio" : 15.9}

**Comparaciones con fechas**

Los operadores de comparación son especialmente útiles cuando trabajamos con fechas, ya que normalmente no buscamos una fecha y hora exactas, sino documentos anteriores, posteriores o comprendidos entre dos fechas.

Es importante tener en cuenta que las comparaciones deben realizarse siempre entre valores del mismo tipo, por lo que la fecha con la que queremos comparar debe estar en** formato fecha (ISODate)**.


    > var d = new ISODate("2013-01-01T00:00:00Z")  
    
    > db.libro.find( {fecha:{$gte:d} } , {fecha:1} )  
 
    { "_id" : "9788408117117", "hecha" : ISODate("2013-08-29T00:00:00Z") }  
    { "_id" : "9788401342158", "hecha" : ISODate("2014-03-01T00:00:00Z") }  
    { "_id" : "9788408113331", "hecha" : ISODate("2013-06-04T00:00:00Z") }  
    { "_id" : "9788468738895", "hecha" : ISODate("2014-02-06T00:00:00Z") }

#### Operadores lógicos

Los operadores lógicos permiten combinar varias condiciones dentro de un mismo filtro. Gracias a ellos, podemos construir consultas más complejas en las que se evalúen varias condiciones a la vez.

Estos operadores se utilizan dentro de los filtros de las sentencias find(), update() y delete(), y se expresan mediante documentos JSON.

Operadores: 

* **`$not`** → devuelve los documentos que **no cumplen una condición concreta**
* **`$or`** → devuelve los documentos que **cumplen alguna** de las condiciones
* **`$nor`** → devuelve los documentos que **no cumplen ninguna** de las condiciones
* **`$and`** → devuelve los documentos que **cumplen todas** las condiciones

Hay que tener en cuenta:

- El operador $not se aplica a un **campo** concreto y siempre envuelve a otro operador.
- Los operadores $or, $nor y $and trabajan con **arrays de condiciones**, no se asocian a un campo, sino que combinan condiciones completas.


**`$not`**{.azul}

El operador $not se utiliza para negar una condición. Devuelve los documentos que no cumplen la condición indicada.

Sintaxis:

        clave : { $not: { operador: valor } }
        
Veamos el ejemplo de la consulta que muestra los libros que no pertenecen a la editorial “Planeta”:
           
       >  db.libro.find(
          { editorial: { $not: { $eq: "Planeta" } } },
          { titulo: 1, editorial: 1 }
        )
 

    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "editorial" : "Plaza & Janes" }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1", "editorial" : "Gigamesh" }  
    { "_id" : "9788499088075", "titulo" : "El ladrón de libros", "editorial" : "Debolsillo" }  
    { "_id" : "9788415140054", "titulo" : "La princesa de hielo", "editorial" : "Embolsillo" }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego" }  

Nota: En este caso sería más sencillo utilizar el operador $ne (distinto), pero el ejemplo sirve para comprender el funcionamiento del operador $not. Esta sentencia sería equivalente.

        db.libro.find(
          { editorial: { $ne: "Planeta" } },
          { titulo: 1, editorial: 1 }
        )

**`$or`**{.azul}

El operador **`$or`** permite que la consulta sea válida si se cumple al menos una de las condiciones indicadas.

Sintaxis:

El operador $or trabaja siempre con un **array de condiciones**, donde cada elemento es un filtro independiente:

        {
          $or: [
            { campo1: valor1 },
            { campo2: valor2 }
          ]
        }


Por ejemplo, la siguiente consulta muestra los libros que no están en stock o que no tienen editorial:


        db.libro.find(
          { $or: [ { enstock: false }, { editorial: null } ] },
          { titulo: 1, enstock: 1, editorial: 1 }
        )
 
    { "_id" : "9788499088075", "titulo" : "El ladrón de libros", "editorial" : "Debolsillo", "enstock" : false }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "editorial" : "Planeta", "enstock" : false }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "enstock" : true}

En este caso, el documento se devuelve si se cumple al menos una de las condiciones del operador $or.

**`$nor`**{.azul}

El operador $nor se utiliza para combinar varias condiciones y devolver únicamente los documentos que no cumplen ninguna de ellas. Es decir, un documento será seleccionado solo si todas las condiciones indicadas resultan falsas.

El operador $nor resulta útil cuando queremos: excluir documentos que cumplan cualquiera de varias condiciones, evitar combinaciones complejas de $not y $or, expresar de forma clara que ninguna condición debe cumplirse. 

Sintaxis

El operador $nor trabaja siempre con un array de condiciones:

        {
          $nor: [
            { campo1: valor1 },
            { campo2: valor2 },
            ...
          ]
        }

Un documento será devuelto solo si no cumple ninguna de las condiciones del array.

Ejemplo:  La siguiente consulta muestra los libros que no están en stock ni pertenecen a la editorial “Planeta”:

        db.libro.find(
          {
            $nor: [
              { enstock: true },
              { editorial: "Planeta" }
            ]
          },
          { titulo: 1, enstock: 1, editorial: 1 }
        )

En este caso, MongoDB devolverá únicamente los documentos que no estén en stock y tampoco tengan como editorial “Planeta”. Si un libro cumple alguna de esas condiciones, no aparecerá en el resultado.




**`$and`**{.azul}

El operador $and se utiliza para combinar varias condiciones dentro de un mismo filtro. MongoDB solo devolverá los documentos que cumplan todas las condiciones indicadas. 

Sintaxis:

El operador $and trabaja siempre con un **array de condiciones**, donde cada elemento es un filtro independiente:


        {
          $and: [
            { campo1: valor1 },
            { campo2: valor2 },
            ...
          ]
        }

Un documento será devuelto solo si se cumplen todas las condiciones del array.

En este ejemplo, la consulta muestra los libros que tienen un precio superior a 10 € y están en stock:

        db.libro.find(
          {
            $and: [
              { precio: { $gt: 10 } },
              { enstock: true }
            ]
          },
          { titulo: 1, precio: 1, enstock: 1 }
        )

**Uso implícito de $and utilizando la coma**

MongoDB permite omitir el operador $and cuando las condiciones afectan a campos distintos, ya que lo aplica de forma implícita.

Por ejemplo, la consulta anterior se puede escribir también así:

        db.libro.find(
          { precio: { $gt: 10 }, enstock: true },
          { titulo: 1, precio: 1, enstock: 1 }
        )

Ambas consultas son equivalentes desde el punto de vista del resultado. No obstante, la forma implícita (separando las condiciones mediante comas) suele resultar más legible en consultas sencillas.

Como recomendación general, es aconsejable utilizar el operador $and de forma explícita cuando: se desea mejorar la claridad de la consulta, se combinan operadores lógicos como $or, $not o $nor, o se trabajan condiciones más complejas que pueden dificultar la lectura si se escriben de forma implícita.

#### Operadores de campo

Los operadores de campo se utilizan para **validar la estructura de los documentos** o el **tipo de datos** de un campo. 

Los operadores disponibles son: **`$exists`** y **`$type`**

**`$exists`{.azul}**

El operador **`$exists`** permite saber qué documentos **contienen o no un campo determinado**, independientemente de su valor.

Sintaxis:

        clave: { $exists: boolean }

Dependiendo del valor _boolean_ , el funcionamiento será:

  * **true** : devuelve los documentos en los que existe el campo, aunque su valor sea nulo
  * **false** : devuelve los documentos donde el campo no existe

Veamos el ejemplo de consulta que muestra los **libros que tienen el campo paginas**:

    > db.libro.find( { paginas: {$exists:true} } , {titulo:1 , paginas:1} )  

    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "paginas" : 1100 }  
    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "paginas" : 480 }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1", "paginas" : 793 }  
    { "_id" : "9788499088075", "titulo" : "El ladrón de libros", "paginas" : 544 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "paginas" : 290 }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "paginas" : null }

 Observa que el último libro aparece porque el campo paginas existe, aunque su valor sea **null**.

En cambio, si buscamos los libros con** páginas distintas de null**, no aparecerá este último libro:

    > db.libro.find( { paginas: {$ne:null} } , {titulo:1 , paginas:1} )  

    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "paginas" : 1100 }  
    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "paginas" : 480 }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1", "paginas" : 793 }  
    { "_id" : "9788499088075", "titulo" : "El ladrón de libros", "paginas" : 544 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "paginas" : 290 }

Y si usamos **$exists: false**, solo aparecerán los documentos que **no tienen el campo paginas**:

    > db.libro.find( { paginas: {$exists:false} } , {titulo:1 , paginas:1} )  

    { "_id" : "9788415140054", "titulo" : "La princesa de hielo" }

Por último, si realizamos la búsqueda directamente con **paginas: null** MongoDB devolverá tanto documentos **que no tienen el campo** como aquellos que **sí lo tienen con valor nulo**:

    > db.libro.find( { paginas: null } , {titulo:1 , paginas:1} )  

    { "_id" : "9788415140054", "titulo" : "La princesa de hielo" }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "paginas" : null}

Por lo que para muchos casos prácticos, es preferible utilizar el operador $exists en lugar de comparar directamente con null.

**`$type`{.azul}**

El operador $type permite filtrar documentos en función del tipo de dato de un campo.

Sintaxis:

        clave: { $type: tipo }

Donde tipo indica el tipo de dato que debe tener el campo para que el documento sea seleccionado. Los tipos de datos más usados son:  **"int", "double", "string", "bool", "date", "array", "object", "objectId", "null".**

Veamos el ejemplo que selecciona los documentos donde el campo paginas es de tipo entero.

        > db.libro.find(
                { paginas: { $type: "int" } },
                { titulo: 1, paginas: 1 }
                )

#### Expresiones regulares

MongoDB admite expresiones regulares de forma nativa, lo que permite realizar búsquedas de texto flexibles y potentes dentro de los documentos de una colección.

Las expresiones regulares en MongoDB utilizan la misma sintaxis que Perl, muy similar a la que se emplea en la mayoría de lenguajes de programación. Gracias a ello, podemos definir patrones de búsqueda para localizar textos que cumplan determinadas condiciones.

Las expresiones regulares se utilizan directamente en el filtro de las sentencias find(), update y delete.

Veamos algunos ejemplos:

**Búsqueda de una palabra dentro de un texto**

El siguiente ejemplo muestra los libros cuyo título contiene la palabra “juego”:

    > db.libro.find( { titulo: /juego/ } , {titulo:1} )  

    { "_id" : "9788401342158", "titulo" : "El juego de Ripper" }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego" }

En este caso, utiliza la **barra inclinada (slash) /**, en este caso la búsqueda distingue entre mayúsculas y minúsculas.

**Búsqueda sin distinguir mayúsculas y minúsculas**

Para realizar una búsqueda sin tener en cuenta las mayúsculas y minúsculas, se utiliza el modificador **i (ignore case)**:

    > db.libro.find( { titulo: /juego/i } , {titulo:1} )  

    { "_id" : "9788401342158", "titulo" : "El juego de Ripper" }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1" }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego" }

**Búsqueda al inicio del texto**

El **símbolo ^** indica que el patrón debe encontrarse al comienzo del texto.

Por ejemplo, para obtener los libros cuyo título empieza por la palabra “juego”:

    > db.libro.find( { titulo: /^juego/i } , {titulo:1} )  

    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1" }

**Definir alternativas dentro de un patrón**

Las expresiones regulares permiten definir patrones más avanzados. Como la utilización de los **corchetes []** permiten definir alternativas dentro de un patrón.

En el siguiente ejemplo se buscan los libros cuyo resumen contiene la palabra “amiga” o “amigo”, es decir, la cadena amig seguida de una a o una o:

    > db.libro.find( { resumen: /amig[ao]/i } , {titulo:1} )  

    { "_id" : "9788415140054", "titulo" : "La princesa de hielo" }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego" }


### 📚 **Ejercicio 1 (parte 2)**

Siguiendo con la base de datos cine, realiza los siguientes ejercicios:

- 11- Encontrar las películas estrenadas entre 2000 y 2010.
- 12- Encontrar las películas que en la sinopsis contengan la palabra "Bilbo".
- 13- Encontrar las películas que en la sinopsis contengan la palabra "Gandalf".
- 14- Encontrar las películas que en la sinopsis contengan la palabra "Bilbo" y no la palabra "Gandalf". Se aconseja utilizar el operador $and.
- 15- Encontrar las películas que en la sinopsis contengan la palabra "enanos" o "hobbit".
- 16- Encontrar las películas que en la sinopsis contengan las palabras "oro" y "dragón".    
