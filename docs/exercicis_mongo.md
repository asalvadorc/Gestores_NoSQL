# Ejercicios

## 📚 Ejercicio 1

Sobre tu Base de Datos **MONGODB** trabajaremos sobre la colección
**libro**, la misma que hemos utilizado en los ejemplos. Si no la tienes
creada, ejecuta las sentencias del principio de la pregunta **3.8 - Operadores de consulta/ Operadores**. Realiza las siguientes consultas. Cópialas en un único archivo de texto, de forma numerada. Es este archivo el que tendrás que subir.

  1. Busca los libros con más de 500 páginas. Ver _id, título y número de páginas.
  2. Busca los libros del año 2014. Ver únicamente título y fecha.
  3. Busca los libros de la editorial Planeta. Ver únicamente título y editorial.
  4. Busca los libros de la editorial Planeta de más de 500 páginas. Ver únicamente título, editorial y páginas.
  5. Busca los libros sin editorial. Ver únicamente título y editorial.
  6. Busca los libros que en el resumen contienen la palabra **caballo**. Visualiza el resumen para comprobarlo. Tienen que salir 2 libros, **Circo máximo** y **Las carreras de Escorpio**.
  7. Utilizando la función **aggregate** , saca la editorial y la media de páginas de aquellas editoriales que tienen una media de páginas superior a 500. Saldrán 3 editoriales.

  8. Incrementar el precio de los libros de la editorial Planeta en 2€ (recuerde que para modificar más de un documento, debemos poner como tercer parámetro la opción **{multi:true}**).
  9. Crear el campo editorial con el valor nulo, para todos aquellos documentos que carezcan del campo editorial.
  10. Realizar la operación inversa: eliminar el campo editorial para todos aquellos que lo tengan nulo.
  11. Sacar el año del libro, a partir de la **fecha** (será un campo calculado llamado **año**).
  12. Aprovecha el campo anterior para sacar los libros estrictamente anteriores al año 2013. Visualiza **titulo** , **fecha** y **año**.



## 📚 Ejercicio 2

Este ejercicio debes realizarlo sobre tu BD de MongoDB (colección **pelicula**).
    
    
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

  1. Insertar todos los documentos anteriores. Debe ser **obligatoriamente** con una única sentencia, para lo que puedes utilizar variables, una para cada documento.
  2. Consultar todos los documentos
  3. Obtener los documentos con **writer** igual a **"Quentin Tarantino"**
  4. Obtener los documentos con **actores** que incluyan a **"Brad Pitt"**
  5. Obtener los documentos con **franchise** igual a **"The Hobbit"**
  6. Obtener todas las películas de los años 90.
  7. Obtener las películas estrenadas entre 2000 y 2010.
  8. Agregar sinopsis a **"The Hobbit: An Unexpected Journey"** : 
     * "Un hobbit reacio, Bilbo Baggins, se dirige a Lonely Mountain con un enérgico grupo de enanos para reclamar su hogar en la montaña, y el oro que contiene, del dragón Smaug".
  9. Agregar sinopsis a **"The Hobbit: The Desolation of Smaug**": 
     * "Los enanos, junto con Bilbo Baggins y Gandalf the Grey, continúan su búsqueda para recuperar a Erebor, su tierra natal, de manos de Smaug. Bilbo Baggins está en posesión de un anillo misterioso y mágico".
  10. Agregar a un actor llamado **"Samuel L. Jackson"** en la película "Pulp Fiction"
  11. Encontrar las películas que en la sinopsis contengan la palabra **"Bilbo"**
  12. Encontrar las películas que en la sinopsis contengan la palabra **"Gandalf"**
  13. Encontrar las películas que en la sinopsis contengan la palabra **"Bilbo"** y no la palabra **"Gandalf"**. Se aconseja utilizar el operador **$and**
  14. Encontrar las películas que en la sinopsis contengan la palabra **"enanos"** o **"hobbit"**
  15. Encontrar las películas que en la sinopsis contengan las palabras **"oro"** y **"dragón"**
  16. Eliminar la película **"Pee Wee Herman's Big Adventure"**
  17. Eliminar la película **"Avatar"**
    
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
