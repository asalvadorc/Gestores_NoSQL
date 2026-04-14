# 📚 Ejercicios

Sobre la Base de Datos **REDIS** del Servidor del Instituto (dirección
**89.36.214.106**) realizar las siguientes operaciones, tanto para guardar una serie
de datos, como para recuperarlos. Siempre pondremos en las llavas el prefijo
**9999x_** , donde como siempre debe sustituir 9999 por las 4 últimas cifras del
su DNI, y la x por la letra del NIF. Copialas en un único archivo de texto,
de forma numerada. Es este archivo el que tendrás que subir.

  1. Crea la clave **9999x_Número** con tu número
  2. Crea la clave **9999x_Apellidos** con tus apellidos. Una de las dos al menos, número o cogidos, debe constar de más de una palabra.
  3. Muestra todas las claves tuyas, y únicamente las tuyas.
  4. Da un tiempo de vida en la clave **9999x_Número** de **200 segundos**. Comprueba el tiempo de vida que le queda. Posteriormente hazla **permanente**.
  5. Crea la clave **9999x_Adreca** , de tipo Hash, con los subcampos **calle** , **numero** y **cp**. No importa que las datos sean falsas. Puedes realizarlo en una o más sentencias.
  6. Añade a lo anterior el subcampo **poblacio**
  7. Muestra toda la información de tu dirección (solo la información, no las subclaves)****
  8. Crea la clave **9999x_Moduls_ASIX** o **9999x_Moduls_DAM** o **9999x_Moduls_DAW** , dependiendo de ti ciclo. Debe ser de tipo Set, con todos los módulos de tu ciclo, que se detallan a continuación. Puedes realizarlo en una o más de una sentencia. 
     * **ASIX** : ISO, PAX, FH, GBD, LM, FOL, ASO, SXI, IAW, ASGBD, SAD, EIE, PROJ y FCT
     * **DAW** : SI, BD, PR, LM, ED, FOL, DWEC, DWES, DAW, DIW, EIE, PROJ y FCT
     * **DAM** : SI, BD, PR, LM, ED, FOL, AD, PMDM, DI, PSP, SGE, EIE, PROJ y FCT.
  9. Crea la clave **9999x_Moduls_meus** , de tipo Set, con todos los módulos en los que estás matriculado. Puedes realizarlo en una o más de una sentencia.
  10. Guarda en la clave **9999x_Moduls_altres** los módulos en los que no estás matriculado actualmente. Debe ser mediante operaciones de conjuntos. Puedes comprobar que el resultado es correcto con **smembers**
  11. Crea una lista con el número **9999x_Notes_BD** con la nota de 4 ejercicios de BD. Las notas serán: 7, 9, 6, 10. Deben quedar en este orden (no en orden inverso)
  12. Modifica la tercera nota, que pasa de 6 a 8.
  13. Crea un **Set Ordenado** (**zset**) llamado **9999x_Carrera** con los siguientes valores. Puedes realizarlo en una o más de una sentencia. Y ten cuidado porque los tiempos deben ser numéricos  

    
        Sandra 12'52
        Isabel 12'25
        Marta 12'10
        María 12'07
        Rosa 11'95
        Bea 11'97
        Balma 11'90
        Anna 12'74

  14. Saca a las participantes de la carrera ordenadas por el tiempo
  15. Penaliza el tiempo de Bea con 2 décimas (0'2), y vuelve a sacar a las participantes ordenadas (Bea debe haber perdido 2 posiciones, pasando de tercera a quinta posición)





Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
SinObraDerivada 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/)



Licenciado bajo la [Licencia Creative Commons Reconocimiento NoComercial
SinObraDerivada 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/)
