# 7. Operaciones CRUD

En este punto vamos a ver las operaciones más básicas, para la **creación, consulta, actualización y eliminación** de **documentos** de una colección. 

### Crear una Colección

Hay dos formas de crear una colección:

1) Utilizando createCollection():

        db.createCollection("ejemplo")

2) Con el comando insert, creará la colección **ejemplo** si todavía no existe:

        > db.ejemplo.insertOne(object)


### Creación: insert

La sentencia **insert()** se ha comparado tradicionalmente con la sentencia **INSERT INTO ... VALUES de SQL**. MongoDB proporciona los siguientes métodos para insertar documentos en una colección:
  
        db.coleccion.insertOne({documento})  

        db.coleccion.insertMany([{documento1},{documento2},...])​

​**insertOne()​**: Inserta un único documento en una colección.​ Se utiliza cuando se quiere añadir un solo registro de forma puntual.​

**insertMany([])**: Inserta varios documentos simultáneamente en una colección. Los documentos deben indicarse dentro de un array de objetos []. Es más eficiente cuando se necesita insertar múltiples registros.​

![](T8_insert.png)

La sentencia **insert** añadirá documentos a una colección. En el parámetro ponemos el documento directamente, o una variable que contenga el documento. Si la colección no existía, la creará y después añadirá el documento.

        > db.ejemplo.insertOne({ msg : "Hola, ¿qué tal?"})  
      
Acabamos de insertar un nuevo documento, y así nos lo avisa ( **{ "nInserted" : 1
}** , se ha insertado un documento). Automáticamente habrá creado un elemento **_id**
de tipo **ObjectId** , ya que le hace falta para identificar el documento entre
todos los demás de la colección.

Insertamos otro documento:

        > db.ejemplo.insertOne({ msg2 : "¿Cómo va la cosa?"})  

Y en este ejemplo nos guardamos el documento en la **variable doc**, y después
lo insertamos

        > doc = { msg3 : "Por aquí no podemos quejarnos..."}  

        > db.ejemplo.insertOne(**doc**)  
    

También nos indica que ha insertado un documento. Y habrá creado también la clave
**_id** como veremos en el siguiente punto.

**Inserción especificando el id**{.azul}

En el documento que hemos insertado hasta el momento, no hemos especificado la clave
**_id** , y Mongo lo ha generado automáticamente de tipo **ObjectId**.

Pero nosotros podremos poner esta clave **_id** con el valor que queramos. Esto
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
       

Nos avisa que estamos duplicando la _clave_ _principal_ , es decir
el identificador.

**Inserción múltiple**{.azul}

Cuando los documentos que queremos insertar son sencillos, podemos insertar más de uno en la
vez, poniendo dentro del **insertMany()** un **array []** con todos los elementos. 

En el siguiente ejemplo creamos varios números primos en la colección del mismo
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

La sentencia **find()** se ha comparado tradicionalmente con la sentencia **SELECT de SQL**. 
Siempre devolverá un conjunto de documentos, que pueden variar desde no devolver ningún documento, a devolver todos los de la colección.

![](T8_find.png)

La sentencia **find()** puede tener dos parámetros: el **filtro** y la **proyección**, que no son obligatorios. Cada uno de estos paŕametros viene dada en forma de documento (u objeto) JSON. 
Esta sería la sintaxis:

        db.coleccion.find(FILTRO,PROYECCIÓN)
  
**- FILTRO:**
  
  El primero indica un **filtro**, y devolverá aquellos documentos de la colección que **cumplan con los criterios de búsqueda indicado**. Viene a ser la parte del WHERE dentro de un SELECT. El filtro también se utiliza en las sentencias **update() y delete()**.
  
En este ejemplo, devolverá todos los documentos de la colección alumnos que tengan la clave nombre y que en él tengan el valor Rebeca. 

        > db.alumnos.find( { nombre : "Rebeca" } )

En este ejemplo, el filtro está utilizando únicamente un criterio de busqueda, pero el parámtro filtro puede tener más de un criterio de búsqueda, para ello se utilizará los diferentes **operadores**, como veremos más adelante. 

Si queremos que **devuelva todos los documentos**, no ponemos nada como parámetro de filtro **find()** , o aún mejor, le pasamos un documento (objeto) vacío **find({})** .

En este ejemplo, devolverán todos los documentos de la colección ejemplo.

    > db.ejemplo.find()  
    { "_id" : ObjectId("56ce310bc61e04ba81def50b"), "msg" : "Hola, ¿qué tal?" }  
    { "_id" : ObjectId("56ce31f6c61e04ba81def50c"), "msg2" : "¿Cómo va la cosa?" }  
    { "_id" : ObjectId("56ce3237c61e04ba81def50d"), "msg3" : "Por aquí no podemos quejarnos ..." }  
    >

**- PROYECCIÓN:**
  
  El segundo parámetro, nos servirá para **delimitar las claves de los documentos que se devolverán**. Los valores que pondremos a las distintos claves será, según si queremos que aparezcan será **1** o un **0** para que no aparezca.
Viene a ser la parte de la cláusula SELECT, donde indicamos qué columnas queremos visualizar en la consulta SELECT.
  
Si ponemos alguna clave a que sí que aparezca (es decir, con el valor 1), los únicos que aparecerán serán éstos, además del **_id** que por defecto siempre aparece.

    > db.alumnos.find({},{nombre:1})  
  
    { "_id" : ObjectId("56debe3017bf4ed437dc77c8"), "nombre" : "Abel" }  
    { "_id" : ObjectId("56dfdbd136d8b095cb6bd57a"), "nombre" : "Berta" }

Por tanto si no queremos que aparezca **_id** pondremos **_id:0**:

    > db.alumnos.find({},{_id:0})  
   
    { "nombre" : "Abel", "apellidos" : "Bernat Cantera", "edad" : 22, "dirección" : {"calle" : "Mayor", "numero" : 7, "cp" : "12502" }, "nota" : [ 9.5, 9 ] }  
    { "nombre" : "Berta", "apellidos" : "Bernat Cantero" }

Por ejemplo, si queremos mostrar únicamente el nombre:

    > db.alumnos.find({},{nombre:1,_id:0})  
  
    { "nombre" : "Abel" }  
    { "nombre" : "Berta" }


### Eliminación: delete

Para borrar un documento de una colección utilizaremos la sentencia **deleteOne()** o **deleteMany()** para eliminar más de uno. 

Esta sentencia, sólo admite como único parámetro el **filtro**, que hará de criterio de búsqueda para encontrar los documentos a eliminar. En el caso de que no se pase ningún filtro, se eliminarán todos los documentos de la colección.

![](T8_delete.png)

MongoDB ofrece los siguientes métodos para eliminar documentos de una colección:

        db.coleccion.deleteOne(FILTRO)

        db.coleccion.deleteMany(FILTRO)
    
**deleteOne()​**: Elimina un único documento que cumpla el criterio indicado en el filtro. Si hay varios documentos que coinciden, solo se borra el primero que encuentre MongoDB.

**deleteMany()​**: Elimina todos los documentos que cumplan el criterio del filtro. Pero no elimina la colección.​

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

### Actualización - update

La sentencia **update** servirá para actualizar sobre una colección ya creada.

![](T8_update.png)

Tendrá dos parámetros:

1) FILTRO: El primer parámetro será el criterio de búsqueda para encontrar el documento a actualizar. Ya visto en sentencias find() y delete().
2) MODIFICADOR: Define los cambios que se aplicarán a los documentos seleccionados.​ Se utiliza operadores de actualización o modificadores como: $set, $inc, $unset​ que veremos más adelante. 

MongoDB ofrece los siguientes métodos para actualizar los documentos de una colección:

        db.coleccion.updateOne(FILTRO,MODIFICADOR)

        db.coleccion.updateMany(FILTRO,MODIFICADOR)

**updateOne()​** : Actualiza un único documento que cumpla la condición indicada en el filtro. Si varios documentos coinciden, solo se modifica el primero que encuentra MongoDB.

**updateMany()​**: Actualiza todos los documentos que cumplan el criterio del filtro. Modifica varios documentos​


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

### 📚 **Ejercicio 1**

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
  


  
  
