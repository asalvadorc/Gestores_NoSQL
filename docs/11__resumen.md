# 11. Resumen Comandos

Para cualquier operación debe ponerse **db** seguido del nombre de la colección,
y después la operación que queremos realizar.

**Operaciones sobre el servidor MongoDB**{.azul}  

- Conectar a MongoDB => `mongo`  
- Seleccionar la base de datos => `use miBaseDeDatos`  
- Mostrar todas las bases de datos en tu servidor MongoDB => `show dbs`  
- Mostrar a los usuarios de la base de datos actual => `show users`  
- Mostrar los roles definidos en la base de datos actual => `show roles`  
- Mostrar la versión del servidor MongoDB => `db.version()`  
- Mostrar el nombre de la BD del servidor MongoDB => `db.getName()`  
- Mostrar las operaciones que se están ejecutando en el servidor => `db.currentOp()`  
- Mostrar información de la base de datos actual => `db.stats()`  

**Operaciones sobre colecciones**{.azul}  

- Mostrar todas las colecciones en la base de datos seleccionada => `show collections`  
- Crear una colección dentro de la base de datos donde estemos situados => `db.createCollection("nom_de_la_col·lecció")`  

**Otras funciones sobre una colección**{.azul} `db.nom_de_la_col·lecció.XXXXXXX`  

- Eliminar la colección => `drop()`  
- Formatear la salida => `pretty()`  
- Contar de forma precisa el número de documentos de la colección => `countDocuments()` 
- Realizar un recuento para una estimación rápida => `estimatedDocumentCount()`  

**Operaciones CRUD dentro de la colección**{.azul} `db.nom_de_la_col·lecció.XXXXXXX`

- **Create (crear documento/s)** => `insertOne()`, `insertMany()`  
- **Read (leer, buscar documento/s)** => `findOne()`, `find()`, `group()`, `sort()`, `limit()`, `skip()`  
- **Update (modificar documento/s)** => `updateOne()`, `updateMany()`, `replaceOne()`  
- **Delete (eliminar documento/s)** => `deleteOne()`, `deleteMany()`  

**Operaciones avanzadas**{.azul}  

- Pipeline o agregación => `aggregation()`  
