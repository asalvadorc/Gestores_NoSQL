# 2. Estructura JSON

Con JSON podremos representar:

  * **Valores** , de tipo **carácter** (entre comillas dobles), **numérico** (sin comillas) , **booleano** (true o false) o **null**.
  * **Parejas clave valor** , es decir un nombre simbólico acompañado de un valor asociado.. Se representan así: **"nombre" : valor**
  * **Objetos** , que es una colección de miembros, cada uno de los cuales puede ser una pareja clave valor, u otros objetos (incluso arrays): se representan entre claves, y con los elementos separados por comas: **{ "nombre1" : "valor1" , "nombre2": valor2 , valor 3 , ...}**
  * **Arrays** , que son listas de elementos. Los elementos no tienen por qué tener la misma estructura, pero nosotros intentaremos que sí que la tengan por coherencia. Cada elemento puede ser un valor, una pareja clave valor, un objeto o un array.

**Véame algunos ejemplos**:

Objeto, que tiene 5 miembros, todos ellos parejas clave-valor.

    { "p1" : 2 , "p2" : 4 , "p3" : 6 , "p4" : 8 , "p5" : 10 }

Objeto, también con 5 miembros que son parejas clave-valor.
Observe cómo la clave siempre la ponemos entre comillas, y el valor cuando es un
string también, pero cuando es numérico, no.

    {  
      "num": 1 ,  
      "nombre": "Andreu" ,  
      "departamento": 10 ,  
      "edad": 32 ,  
      "sueldo": 1000.0  
    }

Objeto, que consta de un único objeto, **empleado** , el cual consta de 5 miembros clave-valor.

    { "empleado" :  
      { "num": 1 ,  
        "nombre": "Andreu" ,  
        "departamento": 10 ,  
        "edad": 32 ,  
        "sueldo": 1000.0  
      }  
    }


Veamos ahora un ejemplo con un array: donde tenemos el elemento raíz que consta de un único objeto, **notes**, que es un array.

    { "notas" :  
      [5, 7, 8, 7]  
    }



También sería correcto de esta forma, para ver que el elemento raíz no tiene
porque ser un objeto, sino también un array

    [5, 7, 8, 7]

Y ahora uno más completo. Tendremos un objeto raíz, con sólo un objeto,
**empresa** , que tiene un único elemento **empleado** que es un array con 4
elementos, cada uno de los empleados:

    { "empresa":  
      { "empleado":  
        [ {  
              "num": "1",  
              "nombre": "Andreu",  
              "departamento": "10",  
              "edad": "32",  
              "sueldo": "1000.0"  
            },  
            {  
              "num": "2",  
              "nombre": "Bernat",  
              "departamento": "20",  
              "edad": "28",  
              "sueldo": "1200.0"  
            },  
            {  
              "num": "3",  
              "nombre": "Claudia",  
              "departamento": "10",  
              "edad": "26",  
              "sueldo": "1100.0"  
            },  
            {  
              "num": "4",  
              "nombre": "Damián",  
              "departamento": "10",  
              "edad": "40",  
              "sueldo": "1500.0"  
            }
        ]  
      }  
    }

Vamos a ver un par de casos más reales. Ésta es la contestación que hace el
WebService de **Bicicas** al solicitar el estado actual de bicicletas en los
diferentes puntos (en el momento de hacer los apuntes se consulta en la dirección
<http://gestiona.bicicas.es/apps/apps.php>):

    [  
      {"ocupacion":  
        [  
          {
          "id":"01",
          "punto":"UJI - FCHS",
          "puestos":27,
          "ocupados":12,
          "latitud":"39.99533",
          "longitud":"-0.06999", 
          "porcentajeAltaOcupacion":"80",
          "porcentajeBajaOcupacion":"20"
          },  
          {
          "id":"02",
          "punto":"ESTACIÓN DE FERROCARRIL Y AUTOBUSES",
          "puestos":24,
          "ocupados":7,
          "latitud":"39.98765",
          "longitud":"-0.05281",
          "porcentajeAltaOcupacion":"80",
          "porcentajeBajaOcupacion":"20"
          },  
          {
          "id":"03",
          "punto":"PLAZA DE PESCADERÍA",
          "puestos":28,
          "ocupados":4,
          "latitud":"39.98580",
          "longitud":"-0.03798",
          "porcentajeAltaOcupacion":"80",
          "porcentajeBajaOcupacion":"20"
          },  
          ...  
        ]  
      }  
    ]

Como puede comprobar, la raíz no es un objeto, sino un **Array**. En el array
sólo nos interesa el primer elemento que es un objeto con un único miembro, 
**ocupacion** (en el ejemplo no hay más elementos, pero pueden haber más en
momento determinado, cuando quieren hacer avisos). Y **ocupacion es un array** ,
con **un objeto por cada estación de bicicas** , con las parejas clave valor
**id** , **punto** , **puestos** (las bicicletas que caben), **ocupados**
(cuantas bicicletas hay colocadas en ese momento), **latitud** y
**longitud** (las coordenadas), ...

!!!Note "Nota"
    En realidad nos aparecerá toda la información mucho más pegada, porque
    realmente está en una única línea.

    Para poder observar mejor la estructura podemos utilizar un visor de json.
    Normalmente el navegador Firefox los visualiza bien, aunque también depende de
    la versión. Si tenemos instalada una versión que admite la visualización de JSON,
    lo intentará interpretar, aunque seguramente la mejor forma de ver el
    formato JSON es, tirar las opciones ** Datos sin procesar -- > Formato
    de impresión**, que es la que vemos a la derecha:

      ![](T3_5_1_0_1.png) | ![](T3_5_1_0_2.png)  
      ---|---  
  
    Si nuestra versión de Firefox no visualiza el formato JSON, podemos buscar un
    visor de los muchos que existen por internet. En la figura hemos utilizado uno, y se
    puede observar cómo facilita mucho la lectura.

      ![](T3_5_1_1.png)
