

En el apartado anterior hemos visto la actualización de documentos ya
existentes en la Base de Datos. Esta actualización la hacíamos modificando todo
el documento, aunque tenemos la variante de guardar el documento en una variable,
modificar esta variable y después realizar la actualización con esta variable.
Pero observe que es una sustitución del documento antiguo por un documento nuevo.

En este apartado veremos la utilización de unos modificadores (_modifiers_) de
la operación **update()**, que nos permitirán modificar documentos de forma
potente: creando y eliminando claves (elementos) de un documento, o cambiándolos, y
incluso añadir o eliminar elementos de un array.

Todos los modificadores pueden actuar sobre varios campos y pueden combinarse en una misma actualización​.

- **`$set`** Asigna un valor a un campo de un documento existente. ​
- **`$unset​`** Elimina un campo del documento existente.
- **`$rename​`** Cambia el nombre de uno o de varios campos. No se puede renombrar un campo a otro que ya exista con el mismo nombre (conflicto).
- **`$inc`** Incrementa (o decrementa) el valor de un campo numérico.​ Puede sumar o restar (valor positivo o negativo).​
- **`$mul`** Multiplica el valor de un campo numérico por una cantidad.​
- **`$min`** Actualiza un campo solo si el nuevo valo es MENOR que el valor actual. Funciona con números, fechas (ISODate) y cadenas.​
- **`$max`** Actualiza un campo solo si el nuevo valor  es MAYOR que el valor actual. Funciona con números, fechas (ISODate) y cadenas.​

### $set {.azul}

El modificador **$set** asigna un valor a un campo del documento seleccionado de
la Base de Datos. Si el campo ya existía, modificará el valor, y si no existía
lo creará.

La sintaxis del modificador **$set** es la siguiente:

    { $set : { clave : valor} }

Pero recuerde que es un modificador, y debemos utilizarlo dentro de una operación
de actualización. Irá en el segundo parámetro del **update()** , y por tanto con
estos modificadores ya no ponemos todo el documento en el segundo parámetro, sino
únicamente el operador de modificación.

Miremos mejor en un ejemplo:

    > db.alumnos.insertOne( {nombre:"Abel", apellidos:"Bernat Carrera"} )  
     
    
    > db.alumnos.find()  
    {  
      "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
      "nombre" : "Abel",  
      "apellidos" : "Bernat Carrera"  
    }  
    >

Supongamos ahora que le queremos añadir la edad. Antes lo haríamos guardando el documento
en una variable, y añadiendo el campo, para guardarlo después. Ahora lo tenemos más
fácil:

    > db.alumnos.updateOne( {nombre:"Abel"} , { $set: {edad:21} } )  
    
Ha encontrado uno, y lo ha modificado. Evidentemente, si hubiera más de un alumno con el nombre Abel, los modificaría todos.

    > db.alumnos.find()  
    {  
      "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
      "nombre" : "Abel",  
      "apellidos" : "Bernat Carrera",  
      "edad" : 21  
    }

Puede especificar más de un campo con los valores correspondientes. Si no existían
se crearán, y si ya existían se modificarán:

    > db.alumnos.updateOne( {nombre:"Abel"} , { $set: {nota: 8.5 , edad:22} } )  
    
    > db.alumnos.find()  
    {  
      "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
      "nombre" : "Abel",  
      "apellidos" : "Bernat Carrera",  
      "edad" : 22,  
      "nota" : 8.5  
    }

E incluso se puede cambiar el tipo de un campo determinado, y utilizar arrays,
y objetos, ...

    > db.alumnos.updateOne( {nombre:"Abel"} , { $set: {nota: [8.5,7.5,9], dirección:{calle:"Major",numero:7,cp:"12001"} } } )  


    > db.alumnos.find()  
    {  
      "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
      "nombre" : "Abel",  
      "apellidos" : "Bernat Carrera",  
      "edad" : 22,  
      "nota" : [  
          8.5,  
          7.5,  
          9  
      ],  
      "dirección" : {  
          "calle" : "Major",  
          "numero" : 7,  
          "cp" : "12001"  
      }  
    }  


Podemos incluso modificar ahora sólo el valor de un campo de un objeto del
documento. Por ejemplo, vamos a modificar el código postal del anterior alumno.
La forma de llegar al código postal será **direción.cp** , pero deberemos ir con
cuidado que vaya entre comillas para que lo encuentre:

    > db.alumnos.updateOne( {nombre:"Abel"} , { $set: {dirección.cp:"12502"} } )  
    
    uncaught exception: SyntaxError: missing : after property id :  
    @(shell):1:49  
  
    > db.alumnos.updateOne( {nombre:"Abel"} , { $set: {"dirección.cp":"12502"} } )  

    > db.alumnos.find()  
    {  
      "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
      "nombre" : "Abel",  
      "apellidos" : "Bernat Carrera",  
      "edad" : 22,  
      "nota" : [  
            8.5,  
            7.5,  
            9  
      ],  
      "dirección" : {  
            "calle" : "Mayor",  
            "numero" : 7,  
            "cp" : "12502"  
      }  
    }

### $unset {.azul}

El modificador **$unset** servirá para **eliminar** elementos (campos) de uno o
unos documentos. Si el campo existía, lo eliminará, y si no existía, no dará
error (avisará que se han modificado 0 documentos).

La sintaxis es:

    { $unset : {campo : 1 } }

Deberemos poner un valor en el campo que vamos a borrar para mantener la sintaxis
correcta, y ponemos **1** que equivale a true. También podríamos poner **-1**, que equivale a
false, pero entonces no la borraría, y por tanto no haríamos nada. Siempre
pondremos **1**.

Veamos el siguiente ejemplo. Añadimos un campo, que será el número de orden, y
después lo quitaremos.

    > db.alumnos.updateOne( {nombre:"Abel"} , { $set: {num_orden:10} } )  
    
    > db.alumnos.find()  
    {  
      "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
      "nombre" : "Abel",  
      "apellidos" : "Bernat Carrera",  
      "edad" : 22,  
      "nota" : [  
            8.5,  
            7.5,  
            9  
      ],  
      "dirección" : {  
            "calle" : "Mayor",  
            "numero" : 7,  
            "cp" : "12502"  
      },  
      "num_orden" : 10  
    }  
      
    > db.alumnos.updateOne( {nombre:"Abel"} , { $unset: {num_orden:1} } )  
    
    > db.alumnos.updateOne( {nombre:"Abel"} , { $unset: {puntuacion:1} } )  
    

Hemos añadido primero el campo **num_orden** , y hemos mostrado el documento para
comprobar que existe. Luego borramos el campo **num_orden** (y nos confirma
que ha modificado un documento). Después intentamos borrar un campo que no
existe, **puntuacion**. No da error, pero nos avisa de que ha modificado 0
documentos. Podemos comprobar al final cómo el documento ha quedado como esperábamos.

    > db.alumnos.find()  
    {  
        "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
        "nombre" : "Abel",  
        "apellidos" : "Bernat Carrera",  
        "edad" : 22,  
        "nota" : [  
            8.5,  
            7.5,  
            9  
        ],  
        "dirección" : {  
            "calle" : "Mayor",  
            "numero" : 7,  
            "cp" : "12502"  
        }  
    }

### $rename {.azul}

El modificador **$rename** cambiará el nombre de un campo. Si no existía, no dará
error y sencillamente no lo va a modificar. Debemos cuidar de poner el nuevo nombre del
campo entre comillas, para que no dé error.

La sintaxis es:

    { $rename : { campo1 : "nuevo_nombre1" , campo2 : "nuevo_nombre2" , ... } }

Por ejemplo, cambiamos el nombre del campo **nota** a **notas** :

    > db.alumnos.updateOne( {nombre:"Abel"} , { $rename: {nota:"notas"} } )  
     
    > db.alumnos.find()  
    {  
        "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
        "nombre" : "Abel",  
        "apellidos" : "Bernat Carrera",  
        "edad" : 22,  
        "dirección" : {  
              "calle" : "Mayor",  
              "numero" : 7,  
              "cp" : "12502"  
        },  
        "notas" : [  
              8.5,  
              7.5,  
              9  
        ]  
    }

Observe que lo ha cambiado de sitio, lo que nos hace pensar que al cambiar de
nombre un campo, lo que hace es volver a crearlo con el nuevo nombre, y borrar el campo
antiguo.

En este ejemplo volvemos a cambiar el nombre a **nota** e intentamos cambiar el nombre
a un campo inexistente, **campo1**. No dará error.

    > db.alumnos.updateOne( {nombre:"Abel"} , { $rename: {campo1: "campo2" , notas:"nota"} } )  
    
    > db.alumnos.find()  
    {  
      "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
      "nombre" : "Abel",  
      "apellidos" : "Bernat Carrera",  
      "edad" : 22,  
      "dirección" : {  
          "calle" : "Mayor",  
          "numero" : 7,  
          "cp" : "12502"  
      },  
      "nota" : [  
          8.5,  
          7.5,  
          9  
      ]  
    }

### $inc {.azul}

Como cabría esperar, el modificador **$inc** servirá para incrementar un campo
numérico. Si el campo existía, lo incrementará en la cantidad indicada. Si no
existía, creará el campo con un valor inicial de 0, e incrementará el valor con
la cantidad indicada. La cantidad puede ser positiva, negativa o incluso
con parte fraccionaria. Siempre funcionará bien, excepto cuando el campo en
incrementar no sea numérico, que dará error.

La sintaxis es ésta:

    { $inc : {campo : cantidad } }

En los siguientes ejemplos, incrementamos un campo nuevo (por lo tanto lo creará con el
valor especificado), y después lo incrementamos en cantidades positivas, negativas
y fraccionarias, concretamente lo iniciamos con un **2** , y después
lo incrementamos en **5** , en **-4** y en **2.25** , por tanto el resultado final
será **5.25** :

    > db.alumnos.updateOne( {nombre:"Abel"} , { $inc: {puntuacion:2} } )  
      
    > db.alumnos.find()  
    {  
        "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
        "nombre" : "Abel",  
        "apellidos" : "Bernat Carrera",  
        "edad" : 22,  
        "nota" : [  
            8.5,  
            7.5,  
            9  
        ],  
        "dirección" : {  
            "calle" : "Mayor",  
            "numero" : 7,  
            "cp" : "12502"  
        },  
        "puntuación" : 2  
    }  

    > db.alumnos.updateOne( {nombre:"Abel"} , { $inc: {puntuacion:5} } )  
   
    > db.alumnos.updateOne( {nombre:"Abel"} , { $inc: {puntuacion:-4} } )  
   
    > db.alumnos.updateOne( {nombre:"Abel"} , { $inc: {puntuacion:2.25} } )  
    
    > db.alumnos.find()  
    {  
        "_id" : ObjectId("56debe3017bf4ed437dc77c8"),  
        "nombre" : "Abel",  
        "apellidos" : "Bernat Carrera",  
        "edad" : 22,  
        "nota" : [  
            8.5,  
            7.5,  
            9  
        ],  
        "dirección" : {  
            "calle" : "Mayor",  
            "numero" : 7,  
            "cp" : "12502"  
        },  
        "puntuación" : 5.25  
    }

### $mul {.azul}
 
Multiplica el valor de un campo por un número. 
 
Ejemplo:

        db.alumnos.updateOne({ nombre:"Abel"},{ $mul: {puntuacion: 2}})

El operador $mul multiplica el valor del campo puntuación por 2.  Ahora la puntuación tendrá un valor de 10.5.


### $min {.azul}

El operador $min se utiliza para actualizar el valor de un campo solo si el nuevo valor es menor que el valor actual almacenado en el documento. MongoDB realiza internamente una comparación previa entre el valor actual del campo y el valor indicado.

- Si el valor indicado es menor, el campo se actualiza.
- Si el valor indicado es mayor o igual, el campo no se modifica.

Ejemplo:

    db.alumnos.updateOne( { nombre:"Abel"}, { $min: { puntuacion: 1 } } )

En este caso, el campo puntuacion **se actualiza a 1** porque dicho valor es menor que el valor actual (10.5). Si el valor actual hubiera sido menor o igual que 1, la actualización no se habría realizado.

En resumen, el operador $min no sustituye siempre el valor, solo lo cambia si el nuevo es más pequeño.

### $max {.azul}

El operador $max se utiliza para actualizar el valor de un campo únicamente si el nuevo valor es mayor que el valor actual almacenado en el documento. AL igual que en el operador $min, MongoDB realiza internamente una comparación previa entre el valor actual del campo y el valor indicado:

- Si el valor indicado es mayor, el campo se actualiza.
- Si el valor indicado es menor o igual, el campo no se modifica.

Ejemplo:

    db.alumnos.updateOne( { nombre:"Abel"}, { $max: { puntuacion: 7 } } )

En este caso, el campo puntuacion **se actualiza a 7** porque dicho valor es mayor que el valor actual (1). Si el valor actual hubiera sido mayor o igual que 7, la actualización no se habría realizado.

En resumen, $max no sustituye siempre el valor, solo lo cambia si el nuevo es más grande.

### 📚 **Ejercicio 1 (parte 4)**

- 23. Actualizar el año de estreno de la película "Fight Club" para que pase a ser 2000.
- 24. Añadir a la película "Pulp Fiction" un nuevo campo llamado **_rating_** con el valor 9.
- 25. Incrementar en una unidad (+1) el año de estreno de todas las películas de "The Hobbit".
- 26. Eliminar el campo rating de la película "Pulp Fiction".
- 27. Añadir el campo genero a todas las películas de la colección.
- 28. Corregir el nombre del autor "J.R.R. Tolkein", sustituyéndolo por "J.R.R. Tolkien" en los documentos donde aparezca.
