

![alto texto](image-1.png)

La agregación nos permitirá realizar consultas muy avanzadas. Es un proceso un poco
complicado pero muy potente. Nos dará una potencia casi como la del SQL cuando
empezamos a utilizar el GROUP BY y HAVING.

La técnica que se utiliza es la del _**pipeline**_ , es decir hacer una serie de
comandos, cada uno toma los datos que proporciona el anterior y a su
vez proporciona los datos al siguiente comando. De esta forma se tratará
un conjunto de documentos y se harán "operaciones" sobre ellos secuencialmente en
bloques: filtrado, proyección, agrupaciones, ordenación, limitación y _skipping_
(saltar algunos).

    db.collectionName.aggregate(pipeline, options),

donde:  
- collectionName - es el número de una colección,  
- pipeline - es un array que contiene las etapas de agregación,  
- options - parámetros opcionales para la agregación   

    pipeline=  
      _operador $match_,
      _operador $project_,
      _operador $group_ , 
      _operador $sort_ , 
      _operador $limit_ , 
      _operador $skip_ 
        
Cada parámetro del aggregate, es decir, cada operador tendrá formato JSON, y por tanto siempre será del estilo:


    { $operador : { clave: valor , ... } }

El orden de los operadores puede cambiar, pero debemos tener en cuenta que los
comandos se ejecutan en el orden en que los ponemos (de izquierda a derecha). Así,
por ejemplo, puede ser muy conveniente poner el primer operador el $match, que
es el de seleccionar documentos, así las demás operaciones se realizarán sobre
menos documentos e irán más rápidas.



#### $match {.azul}

Servirá para filtrar los documentos. Entonces, la agregación sólo afectará a los
documentos seleccionados. Se pueden utilizar todos los operadores que hemos ido
estudiante.

El siguiente ejemplo selecciona los documentos de la editorial Planeta. Lo hace por
medio de **aggregate** , pero como no hacemos nada más, sencillamente selecciona los
documentos.

    > db.libro.aggregate({$match:{editorial:"Planeta"}})

En el siguiente ejemplo, además de seleccionar los de la editorial Planeta después
aplicamos una proyección sobre los campos título y editorial, para poder
visualizar mejor el resultado.


    > db.libro.aggregate({$match:{editorial:"Planeta"}},{$project:{titulo:1,editorial:1}})  

    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "editorial" : "Planeta"}  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "editorial": "Planeta" }

#### $project {.azul}

Nos permite proyectar sobre determinados campos del documento, pero es mucho más
completo que en la proyección "normal" que habíamos hecho hasta ahora, puesto que permite
también renombrar campos, realizar cálculos, etc.

 **Proyección**

La forma más sencilla, evidentemente es proyectar sobre algunos campos de los
existentes, y el funcionamiento es idéntico al de la otra vez (valores 1 para
que aparezcan, 0 para que no aparezcan; por defecto**_id** siempre aparece):

    > db.libro.aggregate({$project:{titulo:1,editorial:1}})  

    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "editorial" : "Planeta" }  
    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "editorial" : "Plaza & Janes" }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1", "editorial" : "Gigamesh" }  
    { "_id" : "9788499088075", "titulo" : "El ladrón de libros", "editorial" : "Debolsillo" }  
    { "_id" : "9788415140054", "titulo" : "La princesa de hielo", "editorial" : "Embolsillo" }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "editorial" : "Planeta" }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego" }

 **Renombrar**{.azul}

**$project** también nos permite renombrar campos existentes (después veremos que también
cálculos). La forma será poner de este modo:


    { $project : { "nombre_nuevo" : "$camp_viejo" }}


El secreto está en el dólar que va frente al campo viejo, ya que de ésta
modo nos referimos al valor de este campo. Así por ejemplo renombramos el campo
**enstock** a **disponible** , aparte de sacar el título:


    > db.libro.aggregate({$project:{titulo:1 , disponible:"$enstock"}})  

    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "disponible" : true }  
    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "disponible" : true }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1" disponible" : true }  
    { "_id" : "9788499088075", "titulo" : "El ladrón de libros", "disponible" : false }  
    { "_id" : "9788415140054", "titulo" : "La princesa de hielo", "disponible" : true }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "disponible" : false }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "disponible" : true }


  **Campos calculados**{.azul}

Con este nombre genérico nos referiremos a todos los cálculos, expresiones y más
cosas que podremos poner para transformar lo que ya tenemos. Como vemos, esto es
mucho más potente que la proyección normal.

  * **Expresiones matemáticas** : Podremos aplicar fórmulas para sumar (**$add**), restar (**$subtract**), multiplicar (**$multiply**), dividir (**$divide**) y más cosas (potencia, raíz cuadrada, valor absoluto, módulo, ...). Cada operación tiene su operador que será una palabra precedida por el dólar, y con la sintaxis de JSON, donde pondremos a los operandos en un array. 

Por ejemplo, sacaremos título del libro, precio y precio en pesetas (multiplicante
por 166.386)

    > db.libro.aggregate({$project:{titulo:1 , precio:1 , precio_pesetas:{$multiply:["$precio" , 166.386]}}})  

    { "_id" : "9788408117117", "titulo" : "Circo Máximo", "precio" : 21.75, "precio_pesetas" : 3618.8955 }  
    { "_id" : "9788401342158", "titulo" : "El juego de Ripper", "precio" : 21.75, "precio_pesetas" : 3618.8955 }  
    { "_id" : "9788496208919", "titulo" : "Juego de tronos: Canción de hielo y fuego 1", "precio" : 9.5, "precio_pesetas" : 1580.667 }  
    { "_id" : "9788499088075", "titulo" : "La ladrona de libros", "precio" : 9.45, "precio_pesetas" : 1572.34769999999998 }  
    { "_id" : "9788415140054", "titulo" : "La princesa de hielo", "precio" : 11, "precio_pesetas" : 1830.24599999999999 }  
    { "_id" : "9788408113331", "titulo" : "Las carreras de Escorpio", "precio" : 17.23, "precio_pesetas" : 2866.83078 }  
    { "_id" : "9788468738895", "titulo" : "Las reglas del juego", "precio" : 15.9, "precio_pesetas" : 2645.5374 }

 
  * **Expresiones de fechas** : Ya veremos y ya podemos ir intuyendo que muchas agregaciones estarán basadas en el tiempo, para poder realizar consultas de documentos de la semana pasada, o el mes pasado, ... Para poder realizar estas agregaciones, hay un conjunto de expresiones que permiten extraer fácilmente de una fecha su día, mes, año, ... en forma de número

Son las expresiones: **$year, $month, $week, $dayOfMonth, $DayOfWeek,
$dayOfYear, $hour, $minute** y **$second**.

En el siguiente ejemplo sacaremos todos los documentos, proyectando por la fecha, año
y mas:

    > db.libro.aggregate({$project : {fecha:1 , año:{$year:"$fecha"} , mes:{$month:"$fecha"}}})  

    { "_id" : "9788408117117", "hecha" : ISODate("2013-08-29T00:00:00Z"), "año" : 2013, "mes" : 8 }  
    { "_id" : "9788401342158", "hecha" : ISODate("2014-03-01T00:00:00Z"), "año" : 2014, "mes" : 3 }  
    { "_id" : "9788496208919", "hecha" : ISODate("2011-11-24T00:00:00Z"), "año" : 2011, "mes" : 11 }  
    { "_id" : "9788499088075", "hecha" : ISODate("2009-01-09T00:00:00Z"), "año" : 2009, "mes" : 1 }  
    { "_id" : "9788415140054", "hecha" : ISODate("2012-10-30T00:00:00Z"), "año" : 2012, "mes" : 10 }  
    { "_id" : "9788408113331", "hecha" : ISODate("2013-06-04T00:00:00Z"), "año" : 2013, "mes" : 6 }  
    { "_id" : "9788468738895", "hecha" : ISODate("2014-02-06T00:00:00Z"), "año" : 2014, "mes" : 2 }

  
  * **Expresiones de strings** : Nos permiten manipular los strings para extraer subcadenas, concatenar, pasar a mayúsculas o minúsculas. Éstas son algunas de las funciones:

    > * **$substr : [exp , inicio , longitud]** : extrae una subcadena del string del primer parámetro, desde la posición que indica el segundo parámetro (o primer carácter) y tantos caracteres como el tercer parámetro
    > * **$concat : [ exp1 , exp2 , ...]** : concatena las expresiones que hay en el array
    > * **$toLower : exp** y **$toUpper : exp** : convierten la expresión a mayúsculas y minúsculas respectivamente

Por ejemplo, vamos a sacar el título de los libros con el autor entre paréntesis:

    > db.libro.aggregate({$project: { "Libro:" : {$concat : ["$titulo" , " (" , "$autor" , ")"]}}})  

    { "_id" : "9788408117117", "Libro:" : "Circo Máximo (Santiago Posteguillo)" }  
    { "_id" : "9788401342158", "Libro:" : "El juego de Ripper (Isabel Allende)" }  
    { "_id" : "9788496208919", "Libro:" : "Juego de tronos: Canción de hielo y fuego 1 (George R.R. Martin)" }  
    { "_id" : "9788499088075", "Libro:" : "El ladrón de libros (Markus Zusak)" }  
    { "_id" : "9788415140054", "Libro:" : "La princesa de hielo (Camilla Lackberg)" }  
    { "_id" : "9788408113331", "Libro:" : "Las carreras de Escorpio (Maggie Stiefvater)" }  
    { "_id" : "9788468738895", "Libro:" : "Las reglas del juego (Anna Casanovas)"}

Y ahora lo mismo, pero con el título en mayúsculas:

    > db.libro.aggregate({$project: { "Libro:" : {$concat : [{$toUpper:"$titulo"}, " (" , "$autor" , ")"]}}})  

    { "_id" : "9788408117117", "Libro:" : "CIRCO MáXIMO (Santiago Posteguillo)" }  
    { "_id" : "9788401342158", "Libro:" : "EL JUEGO DE RIPPER (Isabel Allende)" }  
    { "_id" : "9788496208919", "Libro:" : "JUEGO DE TRONOS: CANCIóN DE HIELO Y FUEGO 1 (George R.R. Martin)" }  
    { "_id" : "9788499088075", "Libro:" : "LA LADRONA DE LIBROS (Markus Zusak)" }  
    { "_id" : "9788415140054", "Libro:" : "LA PRINCESA DE HIELO (Camilla Lackberg)" }  
    { "_id" : "9788408113331", "Libro:" : "LAS CARRERAS DE ESCORPIO (Maggie Stiefvater)" }  
    { "_id" : "9788468738895", "Libro:" : "LAS REGLAS DEL JUEGO (Anna Casanovas)" }

#### $group {.azul}

Realiza grupos sobre los documentos seleccionados previamente, para valores
iguales del campo o expresiones que determinemos. Posteriormente, con los grupos,
podremos realizar operaciones, como sumar o sacar la media de alguna cantidad
de los documentos del grupo, o el máximo o mínimo, ...

Para poder agrupar, deberemos definir como **_id** del grupo el campo o campos
por cuyos valores queremos agrupar. Por ejemplo, si queremos agrupar los
libros para la editorial, deberemos definir el **_id** del grupo el campo
editorial


    $group : { "_id" : _campo o campos_ }

Si agrupamos por un único campo, sencillamente lo ponemos con un dólar frente y entre
comillas. Si es más de un campo, los ponemos como objeto. Por ejemplo, agrupamos
por editorial:

    > db.libro.aggregate( { $group : { "_id" : "$editorial" } } )  

    { "_id" : "Debolsillo" }  
    { "_id" : null }  
    { "_id" : "Gigamesh" }  
    { "_id" : "Embolsillo" }  
    { "_id" : "Plaza & Janes" }  
    { "_id" : "Planeta" }

Podemos observar cómo existe algún libro que no tiene editorial.

Ahora agrupamos por año de publicación (lo extraeremos del campo **fecha**):

    > db.libro.aggregate( { $group : { "_id" : { "año" : { $year : "$fecha" } } }} ) 

    { "_id" : { "año" : 2012 } }  
    { "_id" : { "año" : 2009 } }  
    { "_id" : { "año" : 2011 } }  
    { "_id" : { "año" : 2014 } }  
    { "_id" : { "año" : 2013 } }

Y ahora agrupamos por editorial y año de publicación (los dos libros de Planeta
son del 2013)

    > db.libro.aggregate( { $group : { "_id" : { "Editorial" : "$editorial" , "año" : { $year : "$fecha" } } } } )  

    { "_id" : { "Editorial" : "Embolsillo", "año" : 2012 } }  
    { "_id" : { "año" : 2014 } }  
    { "_id" : { "Editorial" : "Debolsillo", "año" : 2009 } }  
    { "_id" : { "Editorial" : "Gigamesh", "año" : 2011 } }  
    { "_id" : { "Editorial" : "Plaza & Janes", "año" : 2014 } }  
    { "_id" : { "Editorial" : "Planeta", "año" : 2013 } }

 **Operadores de agrupación**{.azul}

Nos permitirán realizar alguna operación sobre los documentos del grupo. Se ponen como
segundo parámetro del grupo (después de la definición del **_id**).

  * **$sum : valor** : sumará el valor de todos los documentos del grupo. El valor puede ser un campo numérico, o algo más complicado.
  * **$avg : valor** : calculará la media de los valores para los documentos del grupo
  * **$max : valor** : máximo
  * **$min : valor** : mínimo
  * **$first : exp** : tomará el primer valor de la expresión del grupo, ignorando las demás del grupo
  * **$last : exp** : cogerá el último

La documentación dice que también existe el operador **$count** , pero a partir
de una determinada versión. Se puede sustituir su utilización por el operador
**$sum** , sumando la cantidad 1.

Por ejemplo, la suma de los precios de los libros de cada editorial:

    > db.libro.aggregate( { $group : { "_id" : "$editorial" , "suma_precios" : {$sum : "$precio"} } } )  

    { "_id" : "Debolsillo", "suma_precios" : 9.45 }  
    { "_id" : null, "suma_precios" : 15.9 }  
    { "_id" : "Gigamesh", "suma_precios" : 9.5 }  
    { "_id" : "Embolsillo", "suma_precios" : 11 }  
    { "_id" : "Plaza & Janes", "suma_precios" : 21.75 }  
    { "_id" : "Planeta", "suma_precios" : 38.980000000000004 }

O la media de los precios de cada año:

    > db.libro.aggregate( { $group : { "_id" : { "año" : { $year : "$fecha" } } , "media precios" : { $avg : "$precio" } } } )  

    { "_id" : { "año" : 2012 }, "media precios" : 11 }  
    { "_id" : { "año" : 2009 }, "media precios" : 9.45 }  
    { "_id" : { "año" : 2011 }, "media precios" : 9.5 }  
    { "_id" : { "año" : 2014 }, "media precios" : 18.825 }  
    { "_id" : { "año" : 2013 }, "media precios" : 19.490000000000002 }

Y ahora intentamos contar la cantidad de libros de cada editorial:

    > db.libro.aggregate( { $group : { "_id" : "$editorial" , "cuántos" : { $sum : 1} } } )  

    { "_id" : "Debolsillo", "cuántos" : 1 }  
    { "_id" : null, "cuántos" : 1 }  
    { "_id" : "Gigamesh", "cuántos" : 1 }  
    { "_id" : "Embolsillo", "cuántos" : 1 }  
    { "_id" : "Plaza & Janes", "cuántos" : 1 }  
    { "_id" : "Planeta", "cuántos" : 2 }

#### $sort {.azul}

Sirve para ordenar y sigue la misma sintaxis que en las consultas normal
(1: orden ascendente; -1: orden descendente). Podremos ordenar por los campos normales
o por campos clalculados.

Por ejemplo ordenamos por la suma de precios de cada editorial:

    > db.libro.aggregate( { $group : { "_id" : "$editorial" , "suma_precios" : { $sum : "$precio"} } } , { $sort : { suma_precios : 1 } })  

    { "_id" : "Debolsillo", "suma_precios" : 9.45 }  
    { "_id" : "Gigamesh", "suma_precios" : 9.5 }  
    { "_id" : "Embolsillo", "suma_precios" : 11 }  
    { "_id" : null, "suma_precios" : 15.9 }  
    { "_id" : "Plaza & Janes", "suma_precios" : 21.75 }  
    { "_id" : "Planeta", "suma_precios" : 38.980000000000004 }

Y ahora ordenamos de forma descendente por la media de precios de cada año:

    > db.libro.aggregate( { $group : { "_id" : {"año":{$year:"$fecha"}} , "media precios":{$avg:"$precio"} } } , {$sort:{"media precios":-1}})  

    { "_id" : { "año" : 2013 }, "media precios" : 19.490000000000002 }  
    { "_id" : { "año" : 2014 }, "media precios" : 18.825 }  
    { "_id" : { "año" : 2012 }, "media precios" : 11 }  
    { "_id" : { "año" : 2011 }, "media precios" : 9.5 }  
    { "_id" : { "año" : 2009 }, "media precios" : 9.45 }

#### $limit {.azul}

Limita el resultado del agregado al número indicado.

Por ejemplo, los tres años en promedio de precios más cara. Es como el último
ejemplo, añadiendo el límite:

    > db.libro.aggregate({$group:{"_id":{"año":{$year:"$fecha"}},"media precios":{$avg:"$precio"}}} , {$sort:{"media precios":-1}} , {$limit:3}) 

    { "_id" : { "año" : 2013 }, "media precios" : 19.490000000000002 }  
    { "_id" : { "año" : 2014 }, "media precios" : 18.825 }  
    { "_id" : { "año" : 2012 }, "media precios" : 11 }

#### $skip {.azul}

Salta el número indicado

En el ejemplo anterior, ahora saltamos los 3 primeros:

    > db.libro.aggregate({$group:{"_id":{"año":{$year:"$fecha"}},"media precios":{$avg:"$precio"}}} , {$sort:{"media precios":-1}} , {$skip:3})  
    
    { "_id" : { "año" : 2011 }, "media precios" : 9.5 }  
    { "_id" : { "año" : 2009 }, "media precios" : 9.45 }


### 📚 **Ejercicio 2**

Sobre tu Base de Datos **MONGODB** trabajaremos sobre la colección
**libro**, la misma que hemos utilizado en los ejemplos. Realiza las siguientes consultas. Cópialas en un único archivo de texto, de forma numerada. Es este archivo el que tendrás que subir.

  1.  Busca los libros de la editorial Planeta. Ver únicamente título y editorial.
  2. Busca los libros con más de 500 páginas. Ver _id, título y número de páginas.
  3. Busca los libros del año 2014. Ver únicamente título y fecha.
  4. Busca los libros de la editorial Planeta de más de 500 páginas. Ver únicamente título, editorial y páginas.
  5. Busca los libros sin editorial. Ver únicamente título y editorial.
  6. Busca los libros que en el resumen contienen la palabra **caballo**. Visualiza el resumen para comprobarlo. Tienen que salir 2 libros, **Circo máximo** y **Las carreras de Escorpio**.
  7. Utilizando la función **aggregate** , saca la editorial y la media de páginas de aquellas editoriales que tienen una media de páginas superior a 500. Saldrán 3 editoriales.

  8. Incrementar el precio de los libros de la editorial Planeta en 2€ (recuerde que para modificar más de un documento, debemos poner como tercer parámetro la opción **{multi:true}**).
  9. Crear el campo editorial con el valor nulo, para todos aquellos documentos que carezcan del campo editorial.
  10. Realizar la operación inversa: eliminar el campo editorial para todos aquellos que lo tengan nulo.
  11. Sacar el año del libro, a partir de la **fecha** (será un campo calculado llamado **año**).
  12. Aprovecha el campo anterior para sacar los libros estrictamente anteriores al año 2013. Visualiza **titulo** , **fecha** y **año**.
