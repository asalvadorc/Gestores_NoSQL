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

