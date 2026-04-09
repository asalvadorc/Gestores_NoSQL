---
title: "Bases de Datos NoSQL"
---

Seguramente **MongoDB** es el más famoso de los Sistemas Gestoras de Bases de Datos
**NoSQL**.
 
El número de **MongoDB** proviene de la palabra inglesa _hu**mongo**us_, que
significa enorme, que es el propósito de esta Base de Datos: guardar grandes
cantidades de información. Es de código abierto y está programada en C++. Lo va
crear la empresa **10gen** (actualmente **MongoDB Inc.**)

Es un SGBD **Documental** , es decir, que servirá para guardar documentos. La
forma interna de guardarlos es en formato **BSON** (Binary JSON) que en
esencia es una variante del JSON para poder guardar físicamente las datos
de forma más eficiente.

En un servidor Mongo puede haber más de una Base de Datos, aunque nosotros
solo gastaremos uno: **prueba**.

  * En cada Base de Datos la información se guardará en **colecciones**.
  * Cada colección constará de varios **documentos**.
  * Y cada documento serán una serie de datos guardados en forma de **clave-valor** , de los tipos soportados por MongoDB, y con el formato JSON (en realidad BSON)

Por tanto, Mongo no hay tablas. Veamos unos ejemplos de documentos JSON para
guardar la información de libros y autoras. Dependen de cómo se tenga que acceder a
la información podemos plantearnos guardar los libros con sus autores, o
guardar a los autores, con sus libros. Incluso nos podríamos guardar los
dos, para poder acceder de todos los modos, aunque es a costa de doblar
la información.

De la primera forma, guardando los libros con su autor, podríamos tener
documentos con esta estructura, que podrían guardarse en una colección
llamada **Libros** :

      {  
        _id:101,  
        titulo:"El secreto de Khadrell",  
        autor: {  
        número:"Pep",  
        cogidos:"Castellano Puchol",  
        año_nacimiento:1960  
        },  
        isbn:"84-95620-72-3"  
      },  
      {  
        _id:102,  
        titulo:"La Sombra del Viento",  
        autor: {  
        número:"Carlos",  
        cogidos:"Ruiz Zafon",  
        país:"España"  
        },  
        paginas:490,  
        editorial:"Planeta"  
      }

Observe cómo los objetos no tienen por qué tener la misma estructura. La
modo de acceder al número de un autor sería ésta: **_objeto.autor.nombre_**

Una forma alternativa de guardar la información, como habíamos comentado antes
sería organizar por autoras, con sus libros. De esta forma podríamos
ir llenando la colección **Autores** con uno o más documentos de este estilo:

    {  
        _id: 201,  
        número:"Pep",  
        cogidos:"Castellano Puchol",  
        año_nacimiento:1960,  
        libros: [  
        {  
          titulo:"El secreto de Khadrell",  
          isbn:"84-95620-72-3"  
        },  
        {  
          titulo:"Habitación 502",  
          editorial:"Tabarca"  
        }  
      ]  
    },  
    {  
        _id:202,  
        número:"Carlos",  
        cogidos:"Ruiz Zafon",  
        país:"España",  
        libros: [  
          {  
            titulo:"La Sombra del Viento",  
            paginas:490,  
            editorial:"Planeta"  
          }  
      ]  
    }

Observe como para un autor, ahora tenemos un array ( los corchetes: **[ ]**) con
sobre libros.

¿Cuál de las dos formas es mejor para guardar la información? Pues depende
del acceso que deba realizarse a las datos. La mejor será seguramente aquella
que dependiendo de los accesos a realizar, devuelva la información de forma
más rápida.


Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
SinObraDerivada 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/)

