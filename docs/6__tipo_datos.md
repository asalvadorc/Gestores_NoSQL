# 6. Tipos de datos

Los valores de los elementos, es decir de las parejas clave valor, pueden ser de unos cuántos tipos. Hagamos un rápido repaso.

En los ejemplos que van a continuación definimos sencillamente parejas clave-valor de los distintos tipos, o en todo caso nos lo guardamos en variables, pero no guardaremos aún en la Base de Datos (lo haremos en la siguiente pregunta).


**NULL**{.azul}

Más que un tipo de datos es un valor, mejor dicho, la ausencia de valor

    { "x" : null }

**BOOLEAN**{.azul}

El tipo booleano, que puede tomar los valores true o false.

    { "x" : true }

    { "y" : false }

**NUMBER**{.azul}

Por defecto, el tipo de datos numéricos será el de coma flotante (**float**),
simple precisión. Si queremos otro tipo (entero, doble precisión, ...) lo
deberemos indicar expresamente. Así los dos siguientes valores son float:

    { "x" : 3.14 }

    { "y" : 3 }

Si queremos que sea estrictamente entero, por ejemplo, deberemos utilizar una
función de conversión:

    { "x" : Double(3.14) }

    { "y" : Int32(3) }

    { "z" : Long(1) }

**STRING**{.azul}

Se puede guardar cualquier cadena con caracteres de la codificación UTF-8

    { x : "Hola, ¿qué tal?"}

**DATE**{.azul}

Se guarda fecha y hora, e internamente se guardan en milisegundos desde el año
inicial. No se guarda el **_Time zone_** , es decir, la desviación respecto a
la hora internacional.

    { x : ISODate("2022-01-16T11:15:27.471Z") }

Normalmente utilizaremos funciones de tratamiento de la fecha-hora. Lo anterior erapara convertir el string en fecha hora. La siguiente es para obtener la fecha-hora actual:

    { x : new Date() }

Es decir, que si no ponemos parámetro, nos da la fecha hora actual. Pero le
podemos poner como parámetro la fecha hora que queremos que genere. En este
ejemplo, sólo ponemos fecha, por tanto la hora será las 00:00:

    > z = new Date("2022-01-16")  
    ISODate("2022-01-16T00:00:00Z")

En este sí que ponemos una determinada hora, y observe cómo debemos deponer la T
(Time) entre el día y la hora:

    > z = new Date("2022-02-16T18:00")  
    ISODate("2022-01-16T18:00:00Z")

Es muy importante que ponemos siempre **New Date()** para generar una fecha-hora.
Si ponemos únicamente **Date()** , lo que estamos generando es un string (seguramente
con la fecha y hora actual, pero un string):

    > z = Date("2022-01-16")  
    Sun Jan 16 2022 22:20:09 GMT+0100 (CET)

**ARRAY**{.azul}

Es un conjunto de elementos, cada uno de cualquier tipo, aunque el más
habitual es que sean del mismo tipo. Van entre corchetes (**[ ]**) y los
elementos separados por comas.

    { x : [ 2 , 4 , 6 , 8 ] }

Como comentábamos, cada elemento del array puede ser de cualquier tipo:

    { y : [ 2 , 3.14 , "Hola" , new Date() ] }

En MongoDB podremos trabajar muy bien con arrays, y tendremos operaciones para
poder buscar dentro del array, modificar un elemento, crear índice, ...

**DOCUMENTOS (OBJETOS)**{.azul}

Los documentos pueden contener como elementos otros documentos (**objetos**)
en la terminología JSON, pero **documentos** en la terminología de MongoDB).

Van entre claves ( **{ }** ), y los elementos que contendrán van separados por
comas y serán parejas clave-valor de cualquier tipo (incluso otros
documentos).

    { x : { a : 1 , b : 2 } }

Poner documentos dentro de otros documentos (lo que se llama _embedded_
_document_) nos permite guardar la información de una manera más real, no tan
plana. Así por ejemplo, los datos de una persona los podríamos definir de la
siguiente modo. Las pondremos en una variable, para ver después cómo podemos
acceder a los diferentes elementos, aunque lo normal será guardarlo en la
Base de Datos (con **insert()**). Si copiamos lo que va a
continuación en el terminal de Mongo, nos aparecerá con un formato extraño. Es
porque la sentencia de asignación a la variable ocupa más de una línea, y
aparecerán 3 puntos al principio para indicar que sigue la sentencia. Pero
funcionará perfectamente:


    doc = {  
      nombre:"Joan Martí",  
      dirección: {  
      calle:"Mayor",  
      número:1,  
      población:"Castellón"  
      } ,  
      teléfonos : [964223344,678345123]  
    }

Observe cómo esta estructura que ha quedado tan clara, seguramente en una
Base de Datos Relacional nos habría tocado guardar en 3 tablas: **_la de personas_**,
**_la de direcciones_** y **_la de teléfonos_**.

Para acceder a los elementos de un documento poníamos el punto. Pues lo mismo por
a los elementos de un documento dentro de un documento. Y también podemos acceder a los
elementos de un array, poniendo el índice entre corchetes.

      > doc.nombre  
      Joan Martí  
        
      > doc.dirección  
      { "calle" : "Mayor", "número" : 1, "población" : "Castellón" }  
        
      > doc.dirección.calle  
      Mayor  
        
      > doc.teléfonos  
      [ 964223344, 678345123 ]  
        
      > doc.teléfonos[0]  
      964223344

**OBJECT ID**{.azul}

Es un tipo que define a MongoDB para poder obtener valores únicos. Es el valor
por defecto del elemento **_id** , necesario en todo documento (atención: en un
documento, no en un elemento de tipo documento que hemos dicho equivalente a
objeto de JSON). Es un número long, es decir, utiliza 24 bytes.

Haremos pruebas de su utilización en la siguiente pregunta, en el momento
de insertar distintos documentos.
