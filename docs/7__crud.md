# 7. Operaciones CRUD

En este punto vamos a ver las operaciones más básicas, para poder trabajar
sobre ejemplos prácticos, y así disponer ya de unos datos iniciales para
practicar.

### Colección

Hay dos formas de crear una colección:

- Utilizando createCollection():

        db.createCollection("ejemplo")

- Con el comando insert:

        db.ejemplo.insertOne(object)

Esto creará la colección **ejemplo** si todavía no existe.  

### Creación: insert

MongoDB proporciona los siguientes métodos para insertar documentos en una colección:
  
  - db.collection.**insertOne()**, para insetar un solo documento.

  - db.collection.**insertMany()**, para insertar un conjunto de documentos.

![](T8_insert.png)

La función **insert** añadirá documentos a una colección. En el parámetro ponemos
el documento directamente, o una variable que contenga el documento. Si la
colección no existía, la creará y después añadirá el documento.

    > db.ejemplo.insertOne({ msg : "Hola, ¿qué tal?"})  
      

Acabamos de insertar un nuevo documento, y así nos lo avisa ( **{ "nInserted" : 1
}** , se ha insertado un documento). Automáticamente habrá creado un elemento **_id**
de tipo **ObjectId** , ya que le hace falta para identificar el documento entre
todos los demás de la colección.

Insertamos otro documento:

        > db.ejemplo.insertOne({ msg2 : "¿Cómo va la cosa?"})  

Y en este ejemplo nos guardamos el documento en la variable **doc**, y después
lo insertamos

    > doc = { msg3 : "Por aquí no podemos quejarnos..."}  

    > db.ejemplo.insertOne(doc)  
    

También nos indica que ha insertado un documento. Y habrá creado también el campo
**_id** como veremos en el siguiente punto.

**Inserción especificando el id**{.azul}

En el documento que hemos insertado hasta el momento, no hemos especificado el campo
**_id** , y Mongo lo ha generado automáticamente de tipo **ObjectId**.

Pero nosotros podremos poner este campo **_id** con el valor que queramos. Esto
sí, deberemos estar seguros de que este valor no lo coge ningún otro documento de la
colección, o nos va a dar un error.

Así por ejemplo vamos a insertar la información de unos alumnos. Los pondremos en
una colección nueva llamada **alumnos** , y les intentaremos poner un **_id**
personal. Por ejemplo pondremos los números 51, 52, 53, ...

    > db.alumnos.insertOne ({_id: 51 , nombre: "Rebeca" , apellidos: "Martí Peral"})  
    

Ha ido bien, y si miramos los documentos que tenemos en la colección, comprobaremos
que nos ha respetado el **_id** :

    > db.alumnos.find()  

    { "_id" : 51, "nombre" : "Rebeca", "apellidos" : "Martí Peral" }  
    

Pero si intentamos insertar otro documento con el mismo **_id** (51), nos
dará error:

    > db.alumnos.insertOne ({_id: 51 , nombre: "Raquel" , apellidos: "Gomis Arnau"})  
   
    WriteResult({  
    "nInserted" : 0,  
    "writeError" : {  
        "code" : 11000,  
        "errmsg" : "E11000 duplicate key error collection: test.alumnos index: _id_
        dup key: { : 51.0 }"  
      }  
    })  
    >

Nos avisa que estamos duplicando la _clave_ _principal_ , es decir
el identificador.

**Inserción múltiple**{.azul}

Cuando los documentos que queremos insertar son sencillos, podemos insertar más de uno en la
vez, poniendo dentro del **insertMany()** un **array** con todos los elementos. En el
siguiente ejemplo creamos varios números primos en la colección del mismo
nombre:

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
    >

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


### Lectura: find

MongoDB ofrece los siguientes métodos para leer documentos de una colección:

  - db.collection.**find()**
 
recupera todos los documentos de la colección. No obstante, es posible especificar criterios de búsqueda para obtener únicamente aquellos documentos que los cumplan (lo veremos más adelante).
 

![](T8_find.png)

Ejemplo:

    > db.ejemplo.find()  
    { "_id" : ObjectId("56ce310bc61e04ba81def50b"), "msg" : "Hola, ¿qué tal?" }  
    { "_id" : ObjectId("56ce31f6c61e04ba81def50c"), "msg2" : "¿Cómo va la cosa?" }  
    { "_id" : ObjectId("56ce3237c61e04ba81def50d"), "msg3" : "Por aquí no podemos quejarnos ..." }  
    >


En todos los casos podemos comprobar que es cierto lo que veníamos afirmando, que se ha
creado automáticamente el elemento **_id** para cada documento guardado.
Evidentemente, cada uno de nosotros tendrá unos valores diferentes.


### Eliminación: delete

Para borrar un documento de una colección utilizaremos la función **deleteOne**
, pasándole como parámetro la condición del documento o documentos a borrar. MongoDB ofrece los siguientes métodos para eliminar documentos de una colección:

  - db.collection.**deleteOne()**

  - db.collection.**deleteMany()**

![](T8_delete.png)

    > db.numerosprimos.deleteOne( {"_id" : 19} )  
    

Nos avisa de que ha borrado un documento.

La condición no debe ser sobre el campo **_id**. Puede ser sobre cualquiera
campo, **y borrará todos los que coinciden**.

    > db.ejemplo.deleteMany( {"msg3" : "Por aquí no podemos quejarnos ..."} )  
    

También tenemos la posibilidad de borrar toda una colección con la función
**drop()**. Presta atención porque es muy sencilla de eliminar, y por tanto,
potencialmente muy peligrosa.

    > db.numerosprimos.drop()  
    true  
    >

### Actualización - update

La función _**update**_ servirá para actualizar un documento ya guardado.
Tendrá dos parámetros:

  * El primer parámetro será la condición para encontrar el documento a actualizar.
  * El segundo parámetro será el nuevo documento que sustituirá al anterior

MongoDB ofrece los siguientes métodos para actualizar los documentos de una colección:

  - db.collection.**updateOne()**

  - db.collection.**updateMany()**

  - db.collection.**replaceOne()**

![](T8_update.png)

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

**Reemplazar un documento**{.azul}

Para reemplazar todo el contenido de un documento excepto el _id, pasa un documento completamente nuevo como segundo argumento en Collection.**replaceOne()**.

Al reemplazar un documento, éste debe constar únicamente de pares campo-valor. No puede incluir expresiones de operadores de actualización.  

El documento de sustitución puede tener campos distintos de los del documento original. En el documento de reemplazo, puede omitir el _id, ya que _id es inmutable. Sin embargo, si lo incluye _id, debe tener el mismo valor que el actual.

    db.ejemplo.replaceOne(
      { "msg" : "Hola, ¿qué tal?" },
      { "msg" : "Hola, ¿qué tal?" , "título2" : "Mensaje 2" }
    )



### 📚 **Ejercicios**

Estos ejercicios debes realizarlos sobre una BD llamada **cine** (colección **pelicula**).

1- Crear la BD cine  
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

  
  3- Consultar todos los documentos  
  4- Obtener los documentos con **writer** igual a **"Quentin Tarantino"**  
  5- Obtener los documentos con **actores** que incluyan a **"Brad Pitt"**  
  6- Obtener los documentos con **franchise** igual a **"The Hobbit"**  
  7- Añadir sinopsis a **"The Hobbit: An Unexpected Journey"** :   
        "Un hobbit reacio, Bilbo Baggins, se dirige a Lonely Mountain con un enérgico grupo de enanos para reclamar su hogar en la montaña, y el oro que contiene, del dragón Smaug".  
  8- Añadir sinopsis a **"The Hobbit: The Desolation of Smaug**":   
        "Los enanos, junto con Bilbo Baggins y Gandalf the Grey, continúan su búsqueda para recuperar a Erebor, su tierra natal, de manos de Smaug. Bilbo Baggins está en posesión de un anillo misterioso y mágico".  
  9- Eliminar la película **"Pee Wee Herman's Big Adventure"**  
  10- Eliminar la película **"Avatar"**  
  


  
  