# 5. Utilización de variables

Especialmente interesante son las variables que pueden contener un documento
JSON.

Podremos utilizarlas durante la sesión, pero evidentemente no perdurarán de una
sesión en la otra.

Para definir una variable podemos poner opcionalmente delante de la palabra
reservada **var** , pero no es necesario. Pondremos el nombre de la variable, el
signo igual, ya continuación el valor de la variable, que puede ser una
constante, o una expresión utilizando constantes, operadores, otras variables,
funciones de Javascript, ...


    Por ejemplo:
      > a = 30  
      30  
      > b = a/4  
      7.5  
      > Math.sqrt(b)  
      2.7386127875258306  
      > doc = {campo1: "Hola", campo2: 45, campo3: new Date()}  
      {  
        "campo1" : "Hola",  
        "camp2" : 45,  
        "camp3" : ISODate("2022-01-16T18:07:51.118Z")  
      }  
      >

Una variable de tipo JSON podrá modificarse muy fácilmente, toda ella, o
alguno de los elementos. Para llegar a los elementos pondremos
**_nombre_variable.nombre_campo** :

    > doc.camp4 = 3.141592  
    3.141592


    > doc.camp5 = [ 2 , 4 , 6 , 8]  
    [ 2, 4, 6, 8 ]

Y si ahora intentamos sacar el contenido de la variable:

    > doc  
    {  
      "campo1" : "Hola",  
      "camp2" : 45,  
      "camp3" : ISODate("2022-01-16T18:07:51.118Z"),  
      "campo4" : 3.141592,  
      "camp5" : [  
                  2,  
                  4,  
                  6,  
                  8  
        ]  
    }  
    >

También debemos hacer constar que en un documento, que será de tipo JSON
(prácticamente), será un conjunto de parejas clave-valor, con algunas
restricciones:

  * El documento (que muchas veces lo asociaremos a objeto de JSON) va entre claves ( **{ }** )
  * Los elementos de un objeto van separados por comas, y son parejas clave-valor.
  * La clave no puede ser nula, ni repetirse en el mismo objeto (sí en diferentes objetos, claro)
  * Los valores son de los tipos que veremos en el apartado siguiente.
  * Un documento guardado debe contener obligatoriamente un campo llamado **_id** , y que contendrá un valor único en la colección y servirá para identificarlo. Si al guardar un documento no le hemos puesto campo **_id** , lo generará automáticamente MongoDB.
