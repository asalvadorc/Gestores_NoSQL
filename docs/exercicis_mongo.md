# Ejercicios

## 📚 Ejercicio 1

Estos ejercicios debes realizarlos sobre una BD llamada **cine** (colección **pelicula**).

1. Crear la BD cine
2. Insertar los siguientes datos. Debe ser **obligatoriamente** con una única sentencia, para lo que puedes utilizar variables, una para cada documento.
    
    
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

  
  3. Consultar todos los documentos.
  4. Obtener los documentos con **writer** igual a **"Quentin Tarantino"**.
  5. Obtener los documentos con **actores** que incluyan a **"Brad Pitt"**.
  6. Obtener los documentos con **franchise** igual a **"The Hobbit"**.
  7. Añadir sinopsis a **"The Hobbit: An Unexpected Journey"** : 
     * "Un hobbit reacio, Bilbo Baggins, se dirige a Lonely Mountain con un enérgico grupo de enanos para reclamar su hogar en la montaña, y el oro que contiene, del dragón Smaug".
  8. Añadir sinopsis a **"The Hobbit: The Desolation of Smaug**": 
     * "Los enanos, junto con Bilbo Baggins y Gandalf the Grey, continúan su búsqueda para recuperar a Erebor, su tierra natal, de manos de Smaug. Bilbo Baggins está en posesión de un anillo misterioso y mágico".
  9. Eliminar la película **"Pee Wee Herman's Big Adventure"**.
  10. Eliminar la película **"Avatar"**.
  11. Obtener las películas estrenadas entre 2000 y 2010.  
  12. Encontrar las películas que en la sinopsis contengan la palabra **"Bilbo"**.  
  13. Encontrar las películas que en la sinopsis contengan la palabra **"Gandalf"**.  
  14. Encontrar las películas que en la sinopsis contengan la palabra   
   **"Bilbo"** y no la palabra **"Gandalf"**. Se aconseja utilizar el operador **$and**.  
  15. Encontrar las películas que en la sinopsis contengan la palabra **"enanos"** o **"hobbit"**.  
  16. Encontrar las películas que en la sinopsis contengan las palabras **"oro"** y **"dragón"**.  
  17. Obtener todas las películas ordenadas por año ascendente
  18. Mostrar solo las 3 primeras películas
  19. Saltar las 2 primeras películas y mostrar el resto
  20. Películas de Tarantino ordenadas por año
  21. Últimas 2 películas más recientes
  22. Buscar "Hobbit", ordenar y limitar a 2.
  23. Cambiar el año de Fight Club a 2000
  24. Añadir el campo rating con valor 9 a Pulp Fiction
  25. Incrementar el año en +1 a todas las películas de The Hobbit 
  26. Añadir un actor a Fight Club
  27. Eliminar el campo rating de Pulp Fiction
  28. Añadir varios actores a Inglorious Basterds
  29. Añadir campo genero a todas las películas
  30. Cambiar "J.R.R. Tolkein" por "J.R.R. Tolkien"
  31. Agregar un actor llamado "Samuel L. Jackson" en la película "Pulp Fiction".  
  32. Agregar los actores “Martin Freeman” y “Ian McKellen” en todas las películas del The Hobbit
  33. Mostrar las películas en las que actúe “Brad Pitt”.
  34. Mostrar las películas donde actúen “Brad Pitt” y “Edward Norton”.
  35. Mostrar películas donde actúe “Brad Pitt” o “Uma Thurman”.
  36. Mostrar el último actor de cada película.
  37. Mostrar el segundo actor de cada película (si existe).
  38. Mostrar las películas que no tienen el campo actores.
  39. Mostrar las películas que tengan exactamente dos actores.
  40. Mostrar solo: título, año, y actores (solo los dos primeros)
  41. Añadir el actor “Helena Bonham Carter” a la película “Fight Club”.
  42. Eliminar el último actor de la película “Inglorious Basterds”.
  43. Eliminar al actor “Brad Pitt” de todas las películas en las que aparezca. 
  44. Eliminar el primer actor de la película “Pulp Fiction”.




## 📚 Ejercicio 2

Sobre tu Base de Datos **MONGODB** trabajaremos sobre la colección **libro**, la misma que hemos utilizado en los ejemplos. 

    db.libro.insertOne({  
            "_id":"9788408117117",  
              "titulo":"Circo Máximo",  
            "autor":"Santiago Posteguillo",  
            "editorial":"Planeta",  
            "enstock":true,  
            "paginas":1100,  
            "precio":21.75,  
            "fecha":new ISODate("2013-08-29T00:00:00Z"),          
            "resumen":"Circo Máximo, de Santiago Posteguillo, que ha escrito otras obras de narrativa histórica como Las Legiones Malditas o La traición de Roma, es la segunda parte de la trilogía de Trajano, que comenzó con Los asesinos del emperador, un relato impactante, descomunal, descrito con un trepidante pulso narrativo destinado a trasla dar al lector a la Roma imperial de los césares. Santiago posteguillo se ha convertido en el autor español de referencia de la novela histórica sobre Roma y el mundo antiguo. Bienvenidos al mundo de Marco Ulpio Trajano. Circo Máximo es la historia de Trajano y su gobierno, guerras y traiciones, lealtades insobornables e historias de amor imposibles. Hay una vestal, un juicio, inocentes acusados, un abogado especial, mensajes cifrados, códigos secretos, batallas campales, fortalezas inexpugnables, asedios sin fin, dos aurigas rivales, el Anfiteatro, los gladiadores y tres carreras de cuadrigas. Hay también un caballo especial, diferente a todos, leyes antiguas olvidadas, sacrificios humanos, amargura y terror, pero también destellos de nobleza y esperanza, como la llama de Vesta, que mientras arde preserva a Roma. Sólo que hay noches en las que la llama del Templo de Vesta tiembla. La rueda de la Fortuna comienza entonces a girar. En esos momentos, todo puede pasar y hasta la vida del propio Trajano, aunque él no lo sepa, corre peligro. Y, esto es lo mejor de todo, ocurrió: hubo un complot para asesinar a Marco Ulpio Trajano."  
        })  
      
    db.libro.insertOne({  
         "_id":"9788401342158",  
          "titulo":"El juego de Ripper",  
          "autor":"Isabel Allende",  
          "editorial":"Plaza & Janes",  
          "enstock":true,  
          "paginas":480,  
          "precio":21.75,  
        "fecha":new ISODate("2014-03-01T00:00:00Z"),          
          "resumen":"Tal como predijo la astróloga más reputada de San Francisco, una oleada de crímenes comienza a sacudir la ciudad. En la investigación sobre los asesinatos, el inspector Bob Martín recibirá la ayuda inesperada de un grupo de internautas especializados en juegos de rol, Ripper. 'Mi madre todavía está viva, pero la matará el Viernes Santo a medianoche', le advirtió Amanda Martín al inspector jefe y éste no lo puso en duda, porque la chica había dado pruebas de saber más que él y todos sus colegas del Departamento de Homicidios. La mujer estaba cautiva en algún punto de los dieciocho mil kilómetros cuadrados de la bahía de San Francisco, tenían pocas horas para encontrarla con vida y él no sabía por dónde empezar a buscarla",  
     })  
       
    db.libro.insertOne({  
        "_id":"9788496208919",  
       "titulo":"Juego de tronos: Canción de hielo y fuego 1",  
       "autor":"George R.R. Martin",  
       "editorial":"Gigamesh",  
       "enstock":true,  
       "paginas":793,  
       "precio":9.5,  
       "fecha":new ISODate("2011-11-24T00:00:00Z"),       
       "resumen":"Tras el largo verano, el invierno se acerca a los Siete Reinos. Lord Eddars Stark, señor de Invernalia, deja sus dominios para unirse a la corte del rey Robert Baratheon el Usurpador, hombre díscolo y otrora guerrero audaz cuyas mayores aficiones son comer, beber y engendrar bastardos. Eddard Stark desempeñará el cargo de M ano del Rey e intentará desentrañar una maraña de intrigas que pondrá en peligro su vida... y la de los suyos. En un mundo cuyas estaciones duran décadas y en el que retazos de una magia inmemorial y olvidada surgen en los rincones más sombrios y maravillosos, la traición y la lealtad, la compasión y la sed de venganza, el amor y el poder hacen del juego de tronos una poderosa trampa que atrapa en sus fauces a los personajes... y al lector. 'El regreso triunfal de Martin a la fantasía de más alta calidad... con personajes desarrollados con maestría, prosa hábil y pura obstinación.'"  
    })  
      
    db.libro.insertOne({  
      "_id":"9788499088075",  
      "titulo":"La ladrona de libros",  
      "autor":"Markus Zusak",  
      "editorial":"Debolsillo",  
      "enstock":false,  
      "paginas":544,  
      "precio":9.45,  
      "fecha":new ISODate("2009-01-09T00:00:00Z"),        
      "resumen":"En plena II Guerra Mundial, la pequeña Liesel hallará su salvación en la lectura. Una novela preciosa, tremendamente humana y emocionante, que describe las peripecias de una niña alemana de nueve años desde que es dada en adopción por su madre hasta el final de la guerra. Su nueva familia, gente sencilla y nada afecta al na zismo, le enseña a leer y a través de los libros Rudy logra distraerse durante los bombardeos y combatir la tristeza. Pero es el libro que ella misma está escribiendo el que finalmente le salvará la vida.",  
    })  
      
    db.libro.insertOne({  
      "_id":"9788415140054",  
      "titulo":"La princesa de hielo",  
      "autor":"Camilla Lackberg",  
      "editorial":"Embolsillo",  
      "enstock":true,  
      "precio":11,  
      "fecha":new ISODate("2012-10-30T00:00:00Z"),      
      "resumen":"Misterio y secretos familiares en una emocionante novela de suspense Erica vuelve a su pueblo natal tras el fallecimiento de sus padres, pero se va a encontrar con un nuevo drama. Aparentemente su amiga de la infancia, Alex, se ha suicidado. Pronto se descubre que no solamente fue asesinada sino que estaba embarazada. El primer sospechoso es Anders, un artista fracasado con quien Alex mantenía una relación especial. Pero poco después de ser liberado por falta de pruebas, Anders aparece muerto en su domicilio. Con la ayuda del comisario Patrik, Erica investigará el pasado de su amiga Alex."  
    })  
      
    db.libro.insertOne({  
      "_id":"9788408113331",  
      "titulo":"Las carreras de Escorpio",  
      "autor":"Maggie Stiefvater",  
      "editorial":"Planeta",  
      "enstock":false,  
      "paginas":290,  
      "precio":17.23,  
      "fecha":new ISODate("2013-06-04T00:00:00Z"),    
      "resumen":"En la pequeña isla de Thisby, cada noviembre los caballos de agua de la mitología celta emergen del mar. Y cada noviembre, los hombres los capturan para participar en una emocionante carrera mortal. En las carreras de Escorpio, algunos compiten para ganar. Otros para sobrevivir. Los jinetes intentan dominar a sus caballos de agua el tiempo suficiente para acabar la carrera. Algunos lo consiguen. El resto, muere en el intento. Sean Kendrick es el favorito, y necesita ganar la carrera para ganar, también, su libertad. Pero Puck Connolly está dispuesta a ser su más dura adversaria. Ella nunca quiso participar en las carreras. Pero no tiene elección: o compite y gana o… lo pierde todo.",  
    })  
      
    db.libro.insertOne({  
      "_id":"9788468738895",  
      "titulo":"Las reglas del juego",  
      "autor":"Anna Casanovas",  
      "enstock":true,  
      "paginas":null,  
      "precio":15.90,  
      "fecha":new ISODate("2014-02-06T00:00:00Z"),  
      "resumen":"Susana Lobato tiene la vida perfectamente planeada y está a punto de conseguir todo lo que quiere: va a tener su propio programa de noticias económicas y en dos meses va a casarse con un hombre maravilloso. Pero una noche Tim anula la boda y la abandona para perseguir un sueño que no la incluye a ella.Kev MacMurray acaba de cumplir treinta y cinco años y siente que ha llegado el momento de dar un cambio a su vida. No sabe por qué, pero últimamente se está asfixiando y está convencido de que no puede seguir donde está. Lo único que lo retiene es la boda de Tim, su mejor amigo.Pero Tim anula la boda y una noche Kev coincide con Susana y respira por primera vez en mucho tiempo.¿Por qué no le había sucedido antes? Se suponía que él y Susana no se soportaban ¿Desde cuándo siente que si no besa a la prometida de su mejor amigo no podrá seguir respirando?Susana nunca había reaccionado así con nadie. ¿Puede correr el riesgo de averiguar qué pasará si se entrega a Kev?Y qué pasará si vuelve Tim, ¿podrán dar un paso atrás?.",  
    })
    


Realiza las siguientes consultas. Cópialas en un único archivo de texto, de forma numerada. Es este archivo el que tendrás que subir.

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



## 📚 Ejercicio 3

Intenta implementar en MongoDB parte de la Base de Datos relacional [**facturas**](https://asalvadorc.github.io/BBDD_PostgreSQL_DML/exercicis_de_tot_el_tema/), concretamente, comienza por las tablas CATEGORÍA y ARTÍCULO, que las tendrás que
representar como documentos de 2 colecciones (colección **categoría** y colección **articulo**).
En los documentos de la colección **categoría**, el código de categoría será el
**_id** , mientras que en los documentos de la colección **articulo**, el código de
el artículo será el **_id**.

  1. Inserta los documentos correspondiente a las categorías del ejercicio **Ex_1** ([**facturas**](https://asalvadorc.github.io/BBDD_PostgreSQL_DML/exercicis_de_tot_el_tema/)).
  2. Inserta los documentos correspondiente a los artículos del ejercicio **Ex_2** ([**facturas**](https://asalvadorc.github.io/BBDD_PostgreSQL_DML/exercicis_de_tot_el_tema/)).
  3. Haz una consulta en la que aparezcan todos los artículos con su descripción y también la descripción de su categoría.
  4. Modifica lo anterior para que aparezcan sólo las descripciones del artículo y de la categoría.
    * Debido a que las datos del documento reunido, que en este caso es categoría, podemos utilizar **$unwind** para "desconstruir" este array.
    * Una vez deconstruido el array es cuando podremos proyectar sobre la descripción del artículo (directamente) y sobre la descripción de la categoría renombrando el campo y subcampo.
  5. Realiza una consulta donde aparezca la descripción de cada categoría, con el número de artículos de cada categoría y el precio medio.
  6. Inserta los documentos correspondiente a los clientes del ejercicio **Ex_3** ([**facturas**](https://asalvadorc.github.io/BBDD_PostgreSQL_DML/exercicis_de_tot_el_tema/)). No nos importará el código de población.
  7. Inserta las facturas correspondiente a los ejercicios **Ex_4** ([**facturas**](https://asalvadorc.github.io/BBDD_PostgreSQL_DML/exercicis_de_tot_el_tema/)) y **Ex_5** ([**facturas**](https://asalvadorc.github.io/BBDD_PostgreSQL_DML/exercicis_de_tot_el_tema/)). Observa que la mejor forma de introducir las líneas de factura está dentro de la misma, en un array.
  8. Haz una consulta para sacar el número de factura y su total.

      ![](T8_Exer_8_1.png)

  9. Modifica lo anterior para sacar también el número del cliente de la factura

      ![](T8_Exer_8_2.png)

  10. Saca un listado de clientes, al menos con su número, y de los artículos que ha comprado, al menos con la descripción del artículo

    ![](T8_Exer_8_3.png)


   

