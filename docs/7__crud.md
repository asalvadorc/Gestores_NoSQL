En este punto vamos a ver las operaciones más básicas, para la **creación, consulta, actualización y eliminación** de **documentos** de una colección. 

### Colección

Hay dos formas de crear una colección:

1) Utilizando createCollection():

        db.createCollection("ejemplo")

2) Con el comando insert, creará la colección **ejemplo** si todavía no existe:

        > db.ejemplo.insertOne(object)


### Create: insert

La sentencia **insert()** se ha comparado tradicionalmente con la sentencia **INSERT de SQL**. 


![](T8_insert.png)

MongoDB proporciona los siguientes métodos para insertar documentos en una colección.

Sintaxis:
  
        db.coleccion.insertOne({documento})  

        db.coleccion.insertMany([{documento1},{documento2},...])​

- **insertOne()​**: Inserta un único documento en una colección.​ Se utiliza cuando se quiere añadir un solo registro de forma puntual.​

- **insertMany([])**: Inserta varios documentos simultáneamente en una colección. Los documentos deben indicarse dentro de un array de objetos []. Es más eficiente cuando se necesita insertar múltiples registros.​

Ambos métodos utilizan un único parámetro:

1) DOCUMENTO o ARRAY DE DOCUMENTOS (obligatorio): En este parámetro se indica el documento que se desea insertar o un array de documentos. El documento puede escribirse directamente en la sentencia o almacenarse previamente en una **variable**. Si la colección no existía previamente, MongoDB la creará automáticamente y, a continuación, insertará el documento o los documentos indicados.

Veamos a continuación varios ejemplos de inserción de documentos en una colección utilizando el método insertOne().


        > db.ejemplo.insertOne({ msg : "Hola, ¿qué tal?"})  
      
Acabamos de insertar un nuevo documento en la colección ejemplo. El resultado de la ejecución nos indica que la operación se ha realizado correctamente, mostrando que se ha insertado un documento. ( **{ "nInserted" : 1 }**  

A continuación, insertamos un segundo documento en la misma colección:

        > db.ejemplo.insertOne({ msg2 : "¿Cómo va la cosa?"})  

En este caso, el resultado también indica que se ha insertado un documento correctamente.

Por último, insertamos un tercer documento, pero esta vez guardamos previamente el contenido en una **variable** llamada _**doc**_ y después lo insertamos utilizando insertOne():

        > doc = { msg3 : "Por aquí no podemos quejarnos..."}  

        > db.ejemplo.insertOne(doc)  
    
En este caso, también nos indica que ha insertado un documento. 

Sin embargo, cuando los documentos que queremos insertar son sencillos, podemos insertar varios a la vez utilizando el método **insertMany()**, pasando como argumento un array ([]) que contenga todos los documentos.

En el siguiente ejemplo insertamos varios números primos en la colección del mismo nombre:

    > db.numerosprimos.insertMany( [ {_id:2} , {_id:3} , {_id:5} , {_id:7} , {_id:11}
    > , {_id:13} , {_id:17} , {_id:19} ] )  
    
    BulkWriteResult({  
        "writeErrors" : [ ],  
        "writeConcernErrors" : [ ],  
        "nInserted" : 8,  
        "nUpserted" : 0,  
        "nMatched" : 0,  
        "nModified" : 0,  
        "nRemoved" : 0,  
        "upserted" : [ ]  
    })  
 
Nos avisa que ha realizado 8 inserciones, y aquí los tenemos:

    > db.numerosprimos.find()  
    { "_id" : 2 }  
    { "_id" : 3 }  
    { "_id" : 5 }  
    { "_id" : 7 }  
    { "_id" : 11 }  
    { "_id" : 13 }  
    { "_id" : 17 }  
    { "_id" : 19 }  
    >

**Clave _id automática**{.azul}

Durante el proceso de inserción de documentos, MongoDB crea automáticamente la clave **_id** para cada documento insertado cuando no se especifica explícitamente.

Esta clave toma un valor de tipo **_ObjectId_** y actúa como identificador único, lo que permite distinguir cada documento del resto dentro de la colección.

Este comportamiento es automático y obligatorio, ya que MongoDB necesita siempre un identificador para gestionar los documentos.

**Clave _id manual**{.azul}

No obstante, también podemos definir manualmente la clave _id y **asignarle el valor que queramos**. En este caso, debemos asegurarnos de que dicho valor no esté repetido en ningún otro documento de la colección, ya que el **clave _id debe ser único**. Si se repite, MongoDB devolverá un error.

Veamos un ejemplo: 

Vamos a insertar información de varios alumnos en una nueva colección llamada alumnos, asignando manualmente un _id personalizado (por ejemplo, valores numéricos: 51, 52, 53, …):

        > db.alumnos.insertOne ({_id: 51 , nombre: "Rebeca" , apellidos: "Martí Peral"})  
    
La inserción se realiza correctamente. Si consultamos ahora los documentos de la colección, comprobaremos que MongoDB ha respetado el valor de la clave _id indicado:

        > db.alumnos.find()  
         { "_id" : 51, "nombre" : "Rebeca", "apellidos" : "Martí Peral" }  
    
Sin embargo, si intentamos insertar otro documento utilizando el mismo _id (51), MongoDB devolverá un error:

            > db.alumnos.insertOne ({_id: 51 , nombre: "Raquel" , apellidos: "Gomis Arnau"})  
           
            WriteResult({  
            "nInserted" : 0,  
            "writeError" : {  
                "code" : 11000,  
                "errmsg" : "E11000 duplicate key error collection: test.alumnos index: _id_
                dup key: { : 51.0 }"  
              }  
            })  
       

MongoDB nos indica que se ha producido un error por **clave duplicada**, ya que estamos intentando repetir la clave principal, es decir, el identificador único del documento.

### Read: find

La sentencia **find()** se ha comparado tradicionalmente con la sentencia **SELECT de SQL**. 

Siempre devolverá un conjunto de documentos, que pueden variar desde no devolver ningún documento, a devolver todos los de la colección.

![](T8_find.png)

Como se puede observar, la sentencia find() admite dos parámetros opcionales: el filtro (query criteria) y la proyección (projection). Ambos parámetros se especifican en forma de documentos JSON (objetos).

La sintaxis general es la siguiente:

        db.coleccion.find(FILTRO,PROYECCIÓN)

A continuación, veremos en detalle la función de cada uno de estos parámetros:
  
1) FILTRO (opcional): Determina qué documentos de la colección se devolverán. MongoDB solo mostrará aquellos documentos que cumplan los criterios de búsqueda indicados. Este parámetro equivale a la **cláusula WHERE** de una sentencia SELECT en SQL. Además, el filtro también se utiliza en otras operaciones como **update() y delete()**.
  
Por ejemplo, la siguiente consulta devuelve todos los documentos de la colección alumnos cuya clave nombre tenga el valor "Rebeca":

        > db.alumnos.find( { nombre : "Rebeca" } )

En este caso, el filtro contiene un único criterio de búsqueda. Sin embargo, el parámetro filtro puede incluir varios criterios, utilizando los distintos operadores de comparación y lógicos, que veremos más adelante.

Si queremos que la consulta **devuelva todos los documentos de la colección**, podemos:  

- No indicar ningún filtro **find()**, o
- Pasar un documento vacío como filtro: **find({})**

Ambas opciones producen el mismo resultado. Por ejemplo:

    > db.ejemplo.find()  
    { "_id" : ObjectId("56ce310bc61e04ba81def50b"), "msg" : "Hola, ¿qué tal?" }  
    { "_id" : ObjectId("56ce31f6c61e04ba81def50c"), "msg2" : "¿Cómo va la cosa?" }  
    { "_id" : ObjectId("56ce3237c61e04ba81def50d"), "msg3" : "Por aquí no podemos quejarnos ..." }  
    >

2) PROYECCIÓN (opcional): Se utiliza para indicar qué claves de los documentos se mostrarán en el resultado. Para cada clave se indica **1** si la clave se muestra, o un **0** si no se muestra. Hay que tener en cuenta que la clave **_id** aparece siempre por defecto, por lo que si no queremos que se muestre, debemos indicarlo explícitamente con **{_id: 0}**. Este parámetro equivale a la cláusula **SELECT** de una sentencia SELECT en SQL, donde indicamos qué columnas queremos visualizar.
  
Por ejemplo, la siguiente consulta devuelve únicamente la clave nombre de los documentos de la colección alumnos:

    > db.alumnos.find({},{nombre:1})  
  
    { "_id" : ObjectId("56debe3017bf4ed437dc77c8"), "nombre" : "Abel" }  
    { "_id" : ObjectId("56dfdbd136d8b095cb6bd57a"), "nombre" : "Berta" }

Como se observa, la clave _id aparece siempre por defecto, por tanto si no queremos que aparezca **_id** pondremos **_id:0**:

    > db.alumnos.find({},{_id:0})  
   
    { "nombre" : "Abel", "apellidos" : "Bernat Cantera", "edad" : 22, "dirección" : {"calle" : "Mayor", "numero" : 7, "cp" : "12502" }, "nota" : [ 9.5, 9 ] }  
    { "nombre" : "Berta", "apellidos" : "Bernat Cantero" }

Por último, si queremos mostrar únicamente la clave nombre, sin que aparezca el _id, podemos combinar ambas opciones:

    > db.alumnos.find({},{nombre:1,_id:0})  
  
    { "nombre" : "Abel" }  
    { "nombre" : "Berta" }

### Update: update

La sentencia **update** servirá para actualizar sobre una colección ya creada.

![](T8_update.png)

MongoDB ofrece los siguientes métodos para actualizar los documentos de una colección.

Sintaxis:

        db.coleccion.updateOne(FILTRO,MODIFICADOR)

        db.coleccion.updateMany(FILTRO,MODIFICADOR)

- **updateOne()​** : Actualiza un único documento que cumpla la condición indicada en el filtro. Si varios documentos coinciden, solo se modifica el primero que encuentra MongoDB.

- **updateMany()​**: Actualiza todos los documentos que cumplan el criterio del filtro. Modifica varios documentos​

Tendrá dos parámetros:

1) FILTRO (opcional): El primer parámetro será el criterio de búsqueda para encontrar el documento a actualizar. Si no se utiliza filtro, se actualizará sobre toda la colección. Ya visto en sentencias find() y delete().

2) MODIFICADOR (obligatorio): Define los cambios que se aplicarán a los documentos seleccionados.​ Se utiliza operadores de actualización o modificadores como: $set, $inc, $unset​ que veremos más adelante. 

Por ejemplo, si miramos los datos actuales:

    > db.ejemplo.find()  
    { "_id" : ObjectId("56ce310bc61e04ba81def50b"), "msg" : "Hola, ¿qué tal?" }  
    { "_id" : ObjectId("56ce31f6c61e04ba81def50c"), "msg2" : "¿Cómo va la cosa?" }

Podemos comprobar el contenido del segundo documento, el que tiene **msg2**. Vamos a
modificarlo: en el primer parámetro ponemos condición de búsqueda (sólo habrá
uno) y en el segundo ponemos el nuevo documento que sustituirá al anterior con el parámetro **$set**.

    > db.ejemplo.updateOne( {msg2:"¿Cómo va la cosa?"} , {$set: {msg2:"¿Qué? ¿Cómo va la cosa?"}}) 

Observe que la contestación del **update****()** es que ha hecho **match** (
ha habido coincidencia) con un documento, y que ha modificado uno. Si no encuentra
ninguna, no dará error, sencillamente dirá que ha hecho match con 0 documentos, y
que ha modificado 0 documentos. Miramos cómo efectivamente ha cambiado el segundo
documento

    > db.ejemplo.find()  
    { "_id" : ObjectId("56ce310bc61e04ba81def50b"), "msg" : "Hola, ¿qué tal?" }  
    { "_id" : ObjectId("56ce31f6c61e04ba81def50c"), "msg2" : "¿Qué? ¿Cómo va la cosa?" }

Nos vendrán muy bien las variables para las actualizaciones, ya que en muchas
ocasiones será modificar ligeramente el documento, cambiando o añadiendo alguno
elemento. Podremos hacerlo cómodamente con la variable: primero guardamos el documento
a modificar en una variable; después modificamos la variable; y por último hacemos
la operación de actualización. Evidentemente si tenemos alguna variable con el
contenido del documento podríamos ahorrarnos el primer paso.

    > doc1 = db.ejemplo.find()  
    { "_id" : ObjectId("56ce310bc61e04ba81def50b"), "msg" : "Hola, ¿qué tal?" }

    > doc1.titol = "Mensaje 1"  
    Mensaje 1

    > db.ejemplo.updateOne( {msg:"Hola, ¿qué tal?"} , doc1)  
    WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })  
    
    > db.ejemplo.findOne()  
    {  
      "_id" : ObjectId("56ce310bc61e04ba81def50b"),  
      "msg" : "Hola, ¿qué tal?",  
      "título" : "Mensaje 1"  
    }  
    >

### Delete: delete

Para borrar un documento de una colección utilizaremos la sentencia **deleteOne()** o **deleteMany()** para eliminar más de uno. 

Esta sentencia, sólo admite como único parámetro el **filtro**, que hará de criterio de búsqueda para encontrar los documentos a eliminar. En el caso de que no se pase ningún filtro, se eliminarán todos los documentos de la colección.

![](T8_delete.png)

MongoDB ofrece los siguientes métodos para eliminar documentos de una colección.

Sintaxis:

        db.coleccion.deleteOne(FILTRO)

        db.coleccion.deleteMany(FILTRO)
    
- **deleteOne()​**: Elimina un único documento que cumpla el criterio indicado en el filtro. Si hay varios documentos que coinciden, solo se borra el primero que encuentre MongoDB.

- **deleteMany()​**: Elimina todos los documentos que cumplan el criterio del filtro. Pero no elimina la colección.​

Utiliza un único parámetro:

1) FILTRO (opcional): Será el criterio de búsqueda para encontrar el documento a eliminar. Si no se utiliza filtro, se eliminarán todos los documentos de la colección. Ya visto en sentencias find().
   
Por ejemplo, si realizamos esta ejecución:

    > db.numerosprimos.deleteOne( {"_id" : 19} )  
    
Nos avisa de que ha borrado un documento.

La condición no debe ser sobre la clave **_id**. Puede ser sobre cualquiera
clave, **y borrará todos los que coinciden**.

    > db.ejemplo.deleteMany( {"msg3" : "Por aquí no podemos quejarnos ..."} )  
    
También tenemos la posibilidad de **borrar toda una colección, NO SOLO LOS DOCUMENTOS** con la sentencia
**drop()**. Presta atención porque es muy sencilla de eliminar, y por tanto, potencialmente muy peligrosa.

    > db.numerosprimos.drop()  
    true  
    >

***

### 📚 **Ejercicio 1 (parte 1)**

Estos ejercicios debes realizarlos sobre una BD llamada **cine** (colección **pelicula**).

1- Crear la BD cine.  
2- Insertar los siguientes datos. Debe ser **obligatoriamente** con una única sentencia, para lo que puedes utilizar variables, una para cada documento.  
    
    
        title : Fight Club
        writer : Chuck Palahniuk
        year : 1999
        actores : [
        Brad Pitt
        Edward Norton ]
        
        
        title : Pulp Fiction
        writer : Quentin Tarantino
        year : 1994
        actores : [
        John Travolta
        Uma Thurman ]
        
        
        
        title : Inglorious Basterds
        writer : Quentin Tarantino
        year : 2009
        actores : [
        Brad Pitt
        Diane Kruger
        Eli Roth ]
        
        
        title : The Hobbit: An Unexpected Journey
        writer : J.R.R. Tolkein
        year : 2012
        franquicia : The Hobbit
        
        
        title : The Hobbit: The Desolation of Smaug
        writer : J.R.R. Tolkein
        year : 2013
        franquicia : The Hobbit
        
        
        title : The Hobbit: The Battle of the Five Armies
        writer : J.R.R. Tolkein
        year : 2012
        franquicia : The Hobbit
        synopsis : Bilbo y compañía se vende obligados a participar en una guerra contra una serie de combatientes y evitar que la Lonely Mountain caiga en manos de una oscuridad creciente.
        
                
        title : Pee Wee Herman's Big Adventure
        
        
        title : Avatar

  
  - 3- Consultar todos los documentos.  
  - 4- Obtener los documentos con **writer** igual a **"Quentin Tarantino"**.  
  - 5- Obtener los documentos con **actores** que incluyan a **"Brad Pitt"**.  
  - 6- Obtener los documentos con **franchise** igual a **"The Hobbit"**.  
  - 7- Añadir sinopsis a **"The Hobbit: An Unexpected Journey"** :   
        "Un hobbit reacio, Bilbo Baggins, se dirige a Lonely Mountain con un enérgico grupo de enanos para reclamar su hogar en la montaña, y el oro que contiene, del dragón Smaug".  
  - 8- Añadir sinopsis a **"The Hobbit: The Desolation of Smaug**":   
        "Los enanos, junto con Bilbo Baggins y Gandalf the Grey, continúan su búsqueda para recuperar a Erebor, su tierra natal, de manos de Smaug. Bilbo Baggins está en posesión de un anillo misterioso y mágico".  
  - 9- Eliminar la película **"Pee Wee Herman's Big Adventure"**.  
  - 10- Eliminar la película **"Avatar"**.  
  
***

### Filtros avanzados

Hasta ahora, en las sentencias find(), update() y delete() hemos utilizado filtros basados principalmente en comparaciones de igualdad, es decir, hemos comprobado si el valor de un campo coincide con un valor concreto.

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

* **`$not`** → devuelve los documentos que **no cumplen la condición** concreta
* **`$or`** → devuelve los documentos que cumplen **alguna** de las condiciones
* **`$nor`** → devuelve los documentos que no cumplen **ninguna** de las condiciones
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

