# Ejercicios

## 📚 Ejercicio 1

 Este ejercicio debes realizarlo sobre la BD cine (colección **pelicula**).

1. Crear la BD cine
2. Insertar todos los siguientes datos. Debe ser **obligatoriamente** con una única sentencia, para lo que puedes utilizar variables, una para cada documento.
    
    
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

  
  3. Consultar todos los documentos
  4. Obtener los documentos con **writer** igual a **"Quentin Tarantino"**
  5. Obtener los documentos con **actores** que incluyan a **"Brad Pitt"**
  6. Obtener los documentos con **franchise** igual a **"The Hobbit"**
  7. Añadir sinopsis a **"The Hobbit: An Unexpected Journey"** : 
     * "Un hobbit reacio, Bilbo Baggins, se dirige a Lonely Mountain con un enérgico grupo de enanos para reclamar su hogar en la montaña, y el oro que contiene, del dragón Smaug".
  8. Añadir sinopsis a **"The Hobbit: The Desolation of Smaug**": 
     * "Los enanos, junto con Bilbo Baggins y Gandalf the Grey, continúan su búsqueda para recuperar a Erebor, su tierra natal, de manos de Smaug. Bilbo Baggins está en posesión de un anillo misterioso y mágico".
  9. Eliminar la película **"Pee Wee Herman's Big Adventure"**
  10. Eliminar la película **"Avatar"**
  11. Obtener las películas estrenadas entre 2000 y 2010.
  12. Encontrar las películas que en la sinopsis contengan la palabra **"Bilbo"**
  13. Encontrar las películas que en la sinopsis contengan la palabra **"Gandalf"**
  14. Encontrar las películas que en la sinopsis contengan la palabra **"Bilbo"** y no la palabra **"Gandalf"**. Se aconseja utilizar el operador **$and**
  15. Encontrar las películas que en la sinopsis contengan la palabra **"enanos"** o **"hobbit"**
  16. Encontrar las películas que en la sinopsis contengan las palabras **"oro"** y **"dragón"**
  17. Agregar a un actor llamado **"Samuel L. Jackson"** en la película "Pulp Fiction"


## 📚 Ejercicio 2

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


   



    
## 💻Actividad

1️⃣ **Diseño de la base de datos MongoDB:**

Diseña una base de datos MongoDB que sea adecuada para un escenario de tu elección. Describe la estructura de la base de datos, incluyendo las colecciones y los documentos que la componen (al menos 3 colecciones relacionadas). Incorpora una imagen ilustrando la BD.

2️⃣ **Creación y población de la base de datos MongoDB:**
    
Crea la base de datos y las colecciones necesarias en MongoDB, utilizando los comandos adecuados. 
Inserta datos en la base de datos, asegurándose de que los documentos cumplan con la estructura definida en el diseño. 

3️⃣ **Operaciones CRUD en MongoDB:** 
   
Muestra y realiza ejemplos concretos de cómo realizar operaciones de inserción, consulta, actualización y eliminación de documentos en la base de datos. 

4️⃣ **Consultas y filtros en MongoDB:** 

Realiza consultas en la base de datos MongoDB para obtener información mediante el uso de la función aggregate.

Por tanto, Mongo no tiene tablas. Veamos algunos ejemplos de documentos JSON para
guardar información del libro y del autor. Dependen de cómo tengas que acceder
la información que podemos considerar guardar los libros con sus autores, o
salvar a los autores, con sus libros. Incluso podríamos salvarlos
dos, para poder acceder de todos modos, aunque sea a costa de duplicar
la información 

5️⃣ **Gestión de índices en MongoDB:** 

Investiga sobre la importancia de los índices en MongoDB y cómo pueden mejorar el rendimiento de las consultas.  
Crea y gestiona índices en la base de datos MongoDB, utilizando los comandos adecuados. 
  

6️⃣ **Entrega**
   
Deberás entregar un documento en formato digital que funcionará como tutorial. Puedes utilizar cualquier recurso educativo abierto, incluso puedes utilizar varios, por ejemplo pdf, infografía, presentación, ebook, mapa mental, mural digital, vídeo, etc. Cada apartado contendrá una explicación de lo que se pide y vendrá acompañado de capturas de pantalla o el código que has utilizado para su consecución.



Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
SinObraDerivada 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/)
